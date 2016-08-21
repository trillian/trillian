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
import multiprocessing
import sqlalchemy

from trillian.database.connections import LocalhostConnection as db
from trillian.database.trilliandb.TrillianModelClasses import DatasetRelease
from trillian.database.trilliandb.FileModelClasses import *
from trillian.utilities import memoize

# define caches
comment_cache = dict()
keyword_cache = dict()
paths_cache   = dict()
path_types_cache = dict()

def getCommentObject(session, comment):
	try:
		commentObject = comment_cache[comment]
	except KeyError:
		commentObject = FitsHeaderComment.objectFromString(session=session, commentString=comment)
		comment_cache[comment] = commentObject
	return commentObject

def getBasePathObject(session=None, base_path=None):
	# ---------------------------------------------------
	# Look up base path if provided - must be set by hand
	# ---------------------------------------------------
	#
	# remove any trailing "/" to standardize on base paths
	if base_path is None:
		return None
	if base_path[-1:] == "/":
		base_path = base_path[0:-1]
	basePath = DirectoryPath.basePathFromString(session=session, path=base_path, add=False)
	if basePath is None:
		errString = "The base path '{0}' was not found in the database".format(base_path)
		errString = errString + "\n" + "Create with 'INSERT INTO file.base_path (path) VALUES ('{0}');'".format(base_path)
		raise Exception("The base path '{0}' was not found in the database".format(base_path))
	return basePath

def initialize_process():
	'''
	Perform any initialization needed as each process starts.
	Use 'global' to make values available to other methods in the process
	(not pretty, but it works).
	Ref: http://stackoverflow.com/questions/10117073/how-to-use-initializer-to-set-up-my-multiprocess-pool
	'''
	db.engine.dispose() # force closing of all existing database connections
	
def process_files(file_list):
	
	session = db.Session()
	session.begin() # one session per directory / process
	
	datasetRelease = DatasetRelease.objectFromString(session=session, short_name=args.source)
	if args.base_path:
		basePath = getBasePathObject(session=session, base_path=args.base_path)
	else:
		basePath = None
	
	# Get some useful objects
	#
	relativePathType = session.query(DirectoryPathType).filter(DirectoryPathType.label=="relative path").one()
	basePathType = session.query(DirectoryPathType).filter(DirectoryPathType.label=="base path").one()
	path_types_cache["relative"] = relativePathType
	path_types_cache["base"] = basePathType
	
	for filepath in file_list:
		filename = os.path.basename(filepath)
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
			addFileRecordToDatabase(session=session,
									fits_dict=fits_dict,
									basePath=basePath,
									dataset_release=datasetRelease)

	#print("Finished with: {0}".format(file_list[-1]))
	session.commit()
	db.engine.dispose() # close all database connections

def addFileRecordToDatabase(session=None, fits_dict=None, basePath=None, dataset_release=None):
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
	
	# get relative path object
	#
	relative_path_string = os.path.relpath(path=fits_dict["filepath"], start=args.base_path)
	if relative_path_string.endswith("/"):
		relative_path_string = relative_path_string[0:-1]
		
	if relative_path_string in paths_cache:
		relativePath = paths_cache[relative_path_string]
	else:
		try:
			relativePath = session.query(DirectoryPath)\
								  .filter(DirectoryPath.path==relative_path_string)\
								  .one()
		except sqlalchemy.orm.exc.NoResultFound:
			relativePath = DirectoryPath(path=relative_path_string)
			relativePath.type = path_types_cache["relative"]
			session.add(relativePath)
			paths_cache[relative_path_string] = relativePath
	
	# create database object
	#
	newFile = FitsFile()
	session.add(newFile)
	if basePath:
		newFile.directoryPaths.append(basePath)
	newFile.datasetRelease = dataset_release
	newFile.filename = fits_dict["filename"]
	newFile.size = int(fits_dict["size"])
	newFile.directoryPaths.append(relativePath)
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
				newHeaderValue.comment = getCommentObject(session, value_and_comment.strip())
				line_parsed = True
				
			# look for string value + comment
			if not line_parsed:
				match = re.search("= ('([^']|'')*')\s*\/\s*(.*)", value_and_comment)
				if match:
					newHeaderValue.string_value = match.group(1)
					# match group 2 is the characters being excluded
					comment = match.group(3).strip()
					if len(comment):
						newHeaderValue.comment = getCommentObject(session, comment)
					line_parsed = True
			
			# look for string value with no comment
			if not line_parsed:
				match = re.search("= ('([^']|'')*')", value_and_comment)
				if match:
					newHeaderValue.string_value = match.group(1)
					line_parsed = True

			# look for int or float + comment
			match = re.search("=\s*([-+0-9Ee.]+).*?\/(.*)", value_and_comment)
			if match:
				newHeaderValue.string_value = match.group(1)
				newHeaderValue.numeric_value = float(match.group(1))
				comment = match.group(2).strip()
				if len(comment) > 0:
					newHeaderValue.comment = getCommentObject(session, comment)
				line_parsed = True
				
			# look for int or float alone
			if not line_parsed:
				match = re.search("([-+0-9Ee.]+)$", value_and_comment)
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
						newHeaderValue.comment = getCommentObject(session, comment)
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
			
def error_callback(exception):
	print (exception)
	
##############################

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="A script to import FITS JSON header files into the Trillian database.")
	parser.add_argument("-d", "--directory",
						 help="root directory to search for FITS files (may specify several)",
						 dest="source_directory",
						 default=".",
						 nargs="+",
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

	if args.recursive:

		pool = multiprocessing.Pool(processes=35, initializer=initialize_process) # initargs=(queue,)
		
		for dir in args.source_directory:
			for root, subdirs, files in os.walk(dir):
				# root: current path
				# subdirs: list of directories in current path
				# files: list of files in current path
			
				filepaths = list()

				for filename in files:
			
					# get path from the base path
					#relative_path = os.path.relpath(root, args.base_path)

					# read file containing JSON data
					filepaths.append(os.path.join(root, filename))
				
				#print("Adding to pool: {0}".format(root))
				if len(filepaths) > 0:
					#pool.apply_async(func=process_files, args=(filepaths,), error_callback=error_callback)
					pool.map_async(func=process_files, iterable=[filepaths], error_callback=error_callback)

		pool.close() # prevents any more tasks from being added
		pool.join()  # wait for all tasks to finish
		
	else:
   
		pool = multiprocessing.Pool(processes=35, initializer=initialize_process)

		for dir in args.source_directory:
			# only select files; recursive more not selected
			filepaths = [os.path.join(dir, f) for f in os.listdir(dir) if os.path.isfile(f)]
			if len(filepaths) > 0:
				pool.map_async(func=process_files, iterable=[filepaths], error_callback=error_callback)
				
		pool.close()
		pool.join()

db.engine.dispose()
sys.exit(0)
