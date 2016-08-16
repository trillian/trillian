#!/usr/bin/env python

"""
This script read FITS headers (and other file metadata) that have been extracted
from FITS files and loads them into the Trillian database.

The script fits2header.py extracts headers from FITS files into JSON
with the extension ".thdr" or, if compressed, ".thdr.gz". This script looks
for those extensions. 
"""

import os
import re
import sys
import json
import gzip
import os.path
import argparse

import sqlalchemy

from trillian.database.connections import LocalhostConnection as db
from trillian.database.trilliandb.TrillianModelClasses import DatasetRelease
from trillian.database.trilliandb.FileModelClasses import *
#from trillian.utilities import gzopen
from trillian.utilities import memoize

parser = argparse.ArgumentParser(description="A script to import FITS JSON header files into the Trillian database.")
parser.add_argument("-d", "--directory",
					 help="root directory to search for FITS files",
					 dest="source_directory",
					 default=".",
					 required=True)
parser.add_argument("-b", "--base-path",
					dest="base_path",
					help="specifies the base directory (i.e. only store path below what's given)",
					default=None,
					required=False)
parser.add_argument("-s", "--source",
					dest="source",
					help="Trillian short name identifier for this data source",
					default=None,
					required=True)
parser.add_argument("-r", "--recursive",
					help="search source directory recursively",
					action="store_true",
					default=False,
					required=False)

# Print help if no arguments are provided
if len(sys.argv) < 2:
	parser.print_help()
	parser.exit(1)

args = parser.parse_args()

# Set up session
session = db.Session()

# -------------------------------------------------------------------
# Set up data release - this script expects only one while being run.
# -------------------------------------------------------------------
try:
	datasetRelease = session.query(DatasetRelease)\
						 .filter(DatasetRelease.short_name==args.source)\
						 .one()
except sqlalchemy.orm.exc.NoResultFound:
	raise Exception("The data release short name '{0}' was not found in the database.".format(args.source))
except sqlalchemy.orm.exc.MultipleResultsFound:
	# missing constraint in the database
	raise Exception("More than one data release was found for '{0}' (shouldn't happen).".format(args.source))

# ---------------------------------------------------
# Look up base path if provided - must be set by hand
# ---------------------------------------------------
#
# remove any trailing "/" to standardize on base paths
if args.base_path and args.base_path[-1:] == "/":
	args.base_path = args.base_path[0:-1]
try:
	basePath = session.query(BasePath)\
					  .filter(BasePath.path==args.base_path)\
					  .one()
except sqlalchemy.orm.exc.NoResultFound:
	errString = "The base path '{0}' was not found in the database".format(args.base_path)
	errString = errString + "\n" + "Create with 'INSERT INTO file.base_path (path) VALUES ('{0}');'".format(args.base_path)
	raise Exception("The base path '{0}' was not found in the database".format(args.base_path))
except sqlalchemy.orm.exc.MultipleResultsFound:
	# missing constraint in the database
	raise Exception("More than one base path was found for '{0}' (shouldn't happen).".format(args.base_path))

# define caches
comment_cache = dict()
keyword_cache = dict()

def getCommentObject(sesssion, comment):
	try:
		commentObject = comment_cache[comment]
	except KeyError:
		commentObject = FitsHeaderComment.objectFromString(session=session, commentString=comment)
		comment_cache[comment] = commentObject
	return commentObject
	
def addFileRecordToDatabase(fits_dict=None):
	''' Takes a dictionary describing a FITS header and adds it to the dictionary. '''
	if fits_dict is None:
		raise Exception("The parameter 'fits_dict' is not allowed to be None.")

	# format:
	#
	# filename : filename
	# filepath : full path to file (not including filename)
	# headers : array of header dictionaries <-- should have been called "HDUs"
	# size : file size in bytes
	# sha256 : sha256 has in hex format 
	#
	
	# create database object
	newFile = FitsFile()
	session.add(newFile)
	newFile.basePath = basePath
	newFile.datasetRelease = datasetRelease
	newFile.filename = fits_dict["filename"]
	newFile.size = int(fits_dict["size"])
	newFile.relative_path = os.path.relpath(path=fits_dict["filepath"], start=args.base_path)
	if 'sha256' in fits_dict:
		newFile.sha256_hash = fits_dict['sha256']
	
	for hdu_dict in fits_dict["headers"]:
		# format is dictionary with keys:
		#
		# data_start, data_end, header_start (byte offsets)
		# hdu (number)
		# header (array of full header lines)
		#
		newHDU = FitsHDU()
		session.add(newHDU)
		newHDU.number = int(hdu_dict["hdu"])
		newHDU.header_start_offset = hdu_dict["header_start"]
		newHDU.data_start_offset = hdu_dict["data_start"]
		newHDU.data_end_offset = hdu_dict["data_end"]
		newHDU.fitsFile = newFile

		for index, header_line in enumerate(hdu_dict["header"]):
			
			# parse line
			keyword = header_line[0:8].rstrip() # remove trailing whitespace
			value_and_comment = header_line[8:].rstrip() # shorter strings will result in ''

			#keywordObject = getFitsHeaderKeywordObject(keyword)
			try:
				keywordObject = keyword_cache[keyword]
			except KeyError:
				keywordObject = FitsHeaderKeyword.objectFromString(session=session, keywordString=keyword)
				keyword_cache[keyword] = keywordObject

			newHeaderValue = FitsHeaderValue()
			session.add(newHeaderValue)
			newHeaderValue.index = index
			newHeaderValue.hdu = newHDU
			
			newHeaderValue.keyword = keywordObject

			line_parsed = False
			
			# Note: the order these blocks are executed in is important.
			
			if keyword in ["COMMENT", "HISTORY"]:
				newHeaderValue.string_value = value_and_comment.strip()
				newHeaderValue.comment = getCommentObject(session, value_and_comment.strip()) #FitsHeaderComment.objectFromString(session=session, commentString=value_and_comment.strip())
				line_parsed = True
				
			# look for string value + comment
			if not line_parsed:
				match = re.search("= ('([^']|'')*')\s*\/\s*(.*)", value_and_comment)
				if match:
					newHeaderValue.string_value = match.group(1)
					# match group 2 is the characters being excluded
					comment = match.group(3).strip()
					if len(comment):
						newHeaderValue.comment = getCommentObject(session, comment) #FitsHeaderComment.objectFromString(session=session, commentString=comment)
					line_parsed = True
			
			# look for string value with no comment
			if not line_parsed:
				match = re.search("= ('([^']|'')*')", value_and_comment)
				if match:
					newHeaderValue.string_value = match.group(1)
					line_parsed = True

			# look for int or float + comment
			match = re.search("=\s*([\-0-9.]+).*\/(.*)", value_and_comment)
			if match:
				newHeaderValue.string_value = match.group(1)
				newHeaderValue.numeric_value = float(match.group(1))
				comment = match.group(2).strip()
				if len(comment) > 0:
					newHeaderValue.comment = getCommentObject(session, comment) # FitsHeaderComment.objectFromString(session=session, commentString=comment)
				line_parsed = True
				
			# look for int or float alone
			if not line_parsed:
				match = re.search("([\-0-9.]+)$", value_and_comment)
				if match:
					newHeaderValue.string_value = match.group(1)
					try:
						newHeaderValue.numeric_value = float(match.group(1))
					except ValueError:
						print("Could not convert value: '{0}'".format(value_and_comment))
						raise Exception("ValueError: Could not convert '{0}' to a number.".format(match.group(1)))
					line_parsed = True
			
			# look for boolean field + comment
			if not line_parsed:
				match = re.search("= \s+([TF]{1})\s*\/\s*(.*)", value_and_comment)
				if match:
					newHeaderValue.string_value = match.group(1)
					comment = match.group(2).strip()
					if len(comment) > 0:
						newHeaderValue.comment = getCommentObject(session, comment) # FitsHeaderComment.objectFromString(session=session, commentString=comment)
					line_parsed = True

			# look for boolean value alone
			if not line_parsed:
				match = re.search("= \s+([TF]{1})", value_and_comment)
				if match:
					newHeaderValue.string_value = match.group(1)
					line_parsed = True
			
			if not line_parsed:
				print("'{0}'".format(value_and_comment))
				raise Exception("Could not parse the header line: " + "\n\n" + header_line + "\n\n")
			

session.begin()

if args.recursive:

	for root, subdirs, files in os.walk(args.source_directory):
		# root: current path
		# subdirs: list of directories in current path
		# files: list of files in current path
		
		for filename in files:
			
			# get path from the base path
			relative_path = os.path.relpath(root, args.base_path)

			# read file containing JSON data
			filepath = os.path.join(root, filename)
			if filename[-8:] == ".thdr.gz":
				with gzip.open(filepath, mode="rt") as f:
					json_data = f.read()
			elif filename[-5] == ".thdr":
				with open(filepath, encoding="utf-8") as f:
					json_data = f.read()
			else:
				continue

			# convert JSON data
			fits_dict = json.loads(json_data)

			# check if we have this file already
			try:
				f = session.query(FitsFile)\
						   .join(DatasetRelease)\
						   .filter(FitsFile.filename==fits_dict["filename"])\
						   .filter(FitsFile.datasetRelease==datasetRelease)\
						   .one()
			except sqlalchemy.orm.exc.NoResultFound:
				addFileRecordToDatabase(fits_dict)
		
		session.commit() # commit for each directory
		session.begin()
else:
	for filename in os.listdir(args.source_directory):
		
		# read file containing JSON data
		filepath = os.path.join(args.source_directory, filename)
		if filepath[-8:] == ".thdr.gz":
			with gzip.open(filepath, mode="rt") as f: # explicitly open in text mode (default is "rb")
				json_data = f.read()
		elif filepath[-5] == ".thdr":
			with open(filepath, encoding='utf-8') as f:
				json_data = f.read()
		else:
			continue

		# convert JSON data
		fits_dict = json.loads(json_data)

		# check if we have this file already
		try:
			f = session.query(FitsFile)\
					   .join(DatasetRelease)\
					   .filter(FitsFile.filename==fits_dict["filename"])\
					   .filter(FitsFile.datasetRelease==datasetRelease)\
					   .one()
			continue # if found
		except sqlalchemy.orm.exc.NoResultFound:
			addFileRecordToDatabase(fits_dict)
			session.commit() # commit for each file
			session.begin()

		
session.commit()
db.engine.dispose()
sys.exit(0)