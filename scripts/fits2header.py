#!/usr/bin/env python3

"""

This script requires Python 3.2+.
Ref: http://stackoverflow.com/questions/12517451/python-automatically-creating-directories-with-file-output
"""

#from __future__ import absolute_import, division, print_function, unicode_literals

import re
import os
import sys
import json
import gzip
import fnmatch
import argparse
import multiprocessing
from trillian.utlities import extract_FITS_header

parser = argparse.ArgumentParser(description="A script to extract headers from FITS files.")
parser.add_argument("-d", "--directory",
					help="root directory to search for FITS files",
					dest="source_directory",
					default=".")
parser.add_argument("-r", "--recursive",
					help="search source directory recursively",
					action="store_true")
parser.add_argument("-o", "--output",
					help="output directory",
					dest="output_directory",
					default=".")
parser.add_argument("-z", "--gzip",
					help="include '.gz' FITS files if found",
					dest="gzip",
					default=True)
parser.add_argument("-c", "--compress",
					help="gzip output files (individually)",
					dest="compress",
					action="store_true")
parser.add_argument("-x", "--debug",
					help="debug mode: limit to n files",
					dest="debug",
					default=False)
# parser.add_argument("-m", "--multiprocessing",
# 					help="enable multiprocessing, up to n processes",
# 					dest="mp",
# 					action="store_true")

if len(sys.argv) < 2:
    parser.print_usage()
    parser.exit(1)

args = parser.parse_args()

source_dir = args.source_directory
#if args.output_directory is None:
#	output_dir = "."
#else:
output_dir = args.output_directory

def is_fits_file(filepath, allow_gz=False):
	'''
	Check if this is a FITS file. Not robust - only checks for extension.
	'''
	if re.search(r'\.fits$', filepath, re.IGNORECASE) or re.search(r'\.fts$', filepath, re.IGNORECASE):
		return True
	if allow_gz and (re.search(r'\.fits$', filepath, re.IGNORECASE) or re.search(r'\.fts$', filepathx, re.IGNORECASE)):
		return True
	return False

def extract_header(filepath, output_filepath):
	d = extract_FITS_header(filepath)
	
	# create directories if needed
	os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
	
	if (args.compress):
		with gzip.open(output_filepath+".gz", "wb") as out:
			out.write(bytes(json.dumps(d), 'UTF-8'))
	else:
		with open(output_filepath, 'w') as out:
			out.write(json.dumps(d))

i = 0

if args.recursive:
	for root, subdirs, files in os.walk(source_dir):
		# root: current path
		# subdirs: list of directories in current path
		# files: list of files in current path
		
		relative_directory = os.path.relpath(root, source_dir)
		
		for filename in files:
			if is_fits_file(filename) == False:
				continue
			
			extract_header(filepath=os.path.join(root, filename),
						   output_filepath=os.path.join(output_dir, relative_directory, filename.rstrip(".gz")+".thdr"))
			
			if args.debug:
				i = i + 1
				if i > args.debug:
					sys.exit(1)
							
else:
	for filename in os.listdir(source_dir):
		if is_fits_file(filename) == False:
			continue
			
		extract_header(filepath=os.path.join(source_dir, filename),
					   output_filepath=os.path.join(output_dir, filename.rstrip(".gz")+".thdr"))

