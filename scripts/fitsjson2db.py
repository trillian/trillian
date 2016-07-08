#!/usr/bin/env python

"""
This script read FITS headers (and other file metadata) that have been extracted
from FITS files and loads them into the Trillian database.

"""

import os
import gzip

from trillian.database.datafiledb.ModelClasses import *
from trillian.utilities import gzopen

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

#parser.add_argument("-x", "--debug",
#					 help="debug mode", default=False)

args = parser.parse_args()

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
			if filename[-3:] == ".gz":
				with gzopen(filepath) as f:
					json_data = f.read()
			else:
				with open(filepath) as f:
					json_data = f.read()

			# convert JSON data
			fits_dict = json.loads(json_data)
		
			# format:
			#
			# filename : filename
			# filepath : full path to file (not including filename)
			# headers : array of header dictionaries
			# size : file size in bytes
			#
else:
	for filename in os.listdir(args.source_directory):
		














		
		