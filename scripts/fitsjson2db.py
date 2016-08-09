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
import gzip

import sqlalchemy

from trillian.database.connections import LocalhostConnection as db
from trillian.database.trilliandb.schema.TrillianModelClasses import DatasetRelease
from trillian.database.trilliandb.schema.FileModelClasses import *
from trillian.utilities import gzopen
from trillian.utilities import memoize

parser = argparse.ArgumentParser(description="A script to import FITS JSON header files into the Trillian database.")
parser.add_arguement("-d", "--directory",
					 help="root directory to search for FITS files",
					 dest="source_directory",
					 default=".",
					 required=True)
parser.add_argument("-b", "--base_dir",
					dest="base_dir",
					help="specifies the base directory (i.e. only store path below what's given)",
parser.add_argument("-s", "--source",
					dest="source",
					help="Trillian short name identifier for this data source",
					default=None,
					required=True)
parser.add_argument("-r", "--recursive",
					help="search source directory recursively",
					action="store_true")

args = parser.parse_args()

# Set up session
session = db.Session()

# Set up data release - this script expects only one while being run.
#
try:
	dataRelease = session.query(DatasetRelease)\
						 .filter(DatasetRelease.short_name==args.source)
						 .one()
except sqlalchemy.orm.exc.NoResultFound:
	raise Exception("The data release short name '{0}' was not found in the database.".format(args.source))
except sqlalchemy.orm.exc.MultipleResultsFound:
	# missing constraint in the database
	raise Exception("More than one data release was found for '{0}' (shouldn't happen).".format(args.source))

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

@memoize
def getFitsHeaderKeywordObject(keyword=None):
	''' Get (and cache) FITS header keyword objects from the 'fits_header_keyword' table. '''
	if keyword is None:
		raise Exception("keyword not specified!")
	try:
		theKeyword = session.query(FitsHeaderKeyword.label==keyword).one()
	except sqlalchemy.orm.exc.NoResultFound:
		# create it here
		theKeyword = FitsHeaderKeyword()
		theKeyword.label = keyword
		session.add(theKeyword)
	except sqlalchemy.orm.exc.MultipleResultsFound:
		raise Exception("Database integrity error: multiple keyword records with label '{0}' found.".format(keyword))

	return theKeyword

@memoize
def getFitsHeaderComment(comment=None):
	''' Get (and cache) FITS header commend objects from the 'fits_header_comment' table. '''
	if comment is None:
		raise Exception("comment not specified!")
	
	try:
		theComment = session.query(FitsHeaderComment.string==comment).one()
	except sqlalchemy.orm.exc.NoResultFound:
		# create it here
		theComment = FitsHeaderComment()
		theComment.string = comment
		session.add(theComment)
	except sqlalchemy.orm.exc.MultipleResultsFound:
		raise Exception("Database integrity error: multiple keyword records with label '{0}' found.".format(keyword))

	return theComment		

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
	newFile.dataSourceRelease = dataRelease
	newFile.filename = fits_dict["filename"]
	newFile.size = int(fits_dict["size"])
	newFile.relative_path = os.path.relpath(path=fits_dict["filepath"], start=args.base_dir)
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
		newHDU.number = hdu_dict["number"]
		newHDU.header_start_offset = hdu_dict["header_start"]
		newHDU.data_start_offset = hdu_dict["data_start"]
		newHDU.data_end_offset = hdu_dict["data_end"]
		newHDU.fitsFile = newFile

		for index, header_line in enumerate(hdu_dict["header"]):
			newHeaderValue = FitsHeaderValue()
			session.add(newHeaderValue)
			newHeaderValue.index = index
			
			# parse line
			keyword = header_line[0:8].rstrip() # remove trailing whitespace
			value_and_comment = line[8:].rstrip() # shorter strings will result in ''
			
			newHeaderValue.keyword = getFitsHeaderKeywordObject(keyword=keyword)

			line_parsed = False
			
			# Note: the order these blocks are executed in is important.
			
			if keyword in ["COMMENT", "HISTORY"]:
				newHeaderValue.string_value = value_and_comment.strip()
				newHeaderValue.comment = getFitsHeaderComment(keyword)
				line_parsed = True
				
			
			# look for int or float + comment
			match = re.search(value_and_comment, "([\-0-9.]+).+/(.+)")
			if match:
				newHeaderValue.string_value = match.group(1)
				newHeaderValue.numeric_value = float(match.group(1))
				newHeaderValue.comment = getFitsHeaderComment(match.group(2))
				line_parsed = True
				
			# look for int or float alone
			if not line_parsed:
				match = re.search(value_and_comment, "([\-0-9.]+).+$")
				if match:
					newHeaderValue.string_value = match.group(1)
					newHeaderValue.numeric_value = float(match.group(1))
					line_parsed = True
			
			# look for boolean field + comment
			if not line_parsed:
				match = re.search("= \s+([TF]{1})\s*/\s*(.+)")
				newHeaderValue.string_value = match.group(1)
				line_parsed = True

			# look for boolean value alone
			if not line_parsed:
				match = re.search("= \s+[TF]"

			# look for string value + comment
			if not line_parsed:
				match = re.search(value_and_comment, "= ('([^']|'')*')\s*/\s*(.+)")
				if match:
					newHeaderValue.string_value = match.group(1)
					# match group 2 is the characters being excluded
					newHeaderValue.comment = getFitsHeaderComment(match.group(3))
					line_parsed = True
			
			# look for string value
			if not line_parsed:
				match = re.search(value_and_comment, "= '([^']|'')*')
				if match:
					newHeaderValue.string_value = match.group(1)
					newHeaderValue.comment = getFitsHeaderComment(match.group(2))
					line_parsed = True
			
			if not line_parsed:
				raise Exception("Could not parse the header line: " + "\n\n" + header_line + "\n\n")
			
			newHDU.fitsHeaderValues.append(newHeaderValue)

if args.recursive:

	for root, subdirs, files in os.walk(args.source_directory):
		# root: current path
		# subdirs: list of directories in current path
		# files: list of files in current path
		
		for filename in files:
			
			# get path from the base path
			relative_path = os.path.relpath(root, args.base_dir)

			# read file containing JSON data
			filepath = os.join.(root, filename)
			if filename[-8:] == ".thdr.gz":
				with gzopen(filepath) as f:
					json_data = f.read()
			elif filename[-5] == ".thdr":
				with open(filepath) as f:
					json_data = f.read()
			else:
				continue

			# convert JSON data
			fits_dict = json.loads(json_data)

			addFileRecordToDatabase(fits_dict)
				
				
				
else:
	for filename in os.listdir(args.source_directory):
		














		
		