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
import queue
import multiprocessing as mp
#import threading

from trillian.utlities import extract_FITS_header

def is_fits_file(filepath, read_compressed=False):
	'''
	Check if this is a FITS file. Not robust - only checks for extension.
	'''
	allowed_suffixes = [r'\.fits$', r'\.fts$']
	
	if read_compressed:
		allowed_suffixes = allowed_suffixes + [r'\.fits.gz$', r'\.fts.gz$', r'\.fits.bz2$', r'\.fts.bz2$']

	return any([re.search(suffix, filepath, re.IGNORECASE) for suffix in allowed_suffixes])
	
def worker_main(queue):
	done = False
	while True and not done:
		# TODO: Handle a "done" signal placed on queue
		filepath, output = queue.get(True)
		done = filepath is None
		if not done:
			extract_header(filepath, output)

def extract_header(filepath, output_filepath):
	d = extract_FITS_header(filepath)
	
	# create directories if needed
	os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
	
	if (args.gzip_output):
		with gzip.open(output_filepath+".gz", "wb") as out:
			out.write(bytes(json.dumps(d), 'UTF-8'))
	else:
		with open(output_filepath, 'w') as out:
			out.write(json.dumps(d))

def producer(files):
	for filename in files:
		if is_fits_file(filepath=filename, read_compressed=args.compressed) == False:
			continue

		#print("Adding file to queue: {0}".format(os.path.basename(filename)))
		filepath = os.path.join(root, filename)
		output_filepath = os.path.join(output_dir, relative_directory, filename.rstrip(".gz")+".thdr")
		queue.put((filepath, output_filepath))
		if args.limit:
			file_count = file_count + 1
			if file_count > args.limit:
				sys.exit(1)

if __name__ == "__main__":

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
	parser.add_argument("-c", "--compressed",
						help="read compressed (gzip or bzip2) FITS files if found",
						dest="compressed",
						action="store_true",
						default=True)
	parser.add_argument("-g", "--gzip",
						help="gzip output files (individually)",
						dest="gzip_output",
						action="store_true")
	parser.add_argument("-l", "--limit",
						help="limit to n files",
						dest="limit",
						type=int,
						default=None)
	parser.add_argument("-p", "--processes",
						help="use threading with n threads (0 = no of cores)",
						dest="consumer_count",
						type=int,
						default=1)
					
	# parser.add_argument("-m", "--multiprocessing",
	#					help="enable multiprocessing, up to n processes",
	#					dest="mp",
	#					action="store_true")

	# Print help if no arguments are provided
	if len(sys.argv) < 2:
		parser.print_usage()
		parser.exit(1)

	args = parser.parse_args()

	source_dir = args.source_directory
	#if args.output_directory is None:
	#	output_dir = "."
	#else:
	output_dir = args.output_directory

	queue = mp.Queue(maxsize=10)
	n_processes = 2
	mp.Pool(processes=n_processes, initializer=worker_main, initargs=(queue,))
	
	file_count = 0
	
	if args.recursive:
		for root, subdirs, files in os.walk(source_dir):
			# root: current path
			# subdirs: list of directories in current path
			# files: list of files in current path
		
			relative_directory = os.path.relpath(root, source_dir)
		
			for filename in files:
				if is_fits_file(filepath=filename, read_compressed=args.compressed) == False:
					continue
			
				#print("Adding file to queue: {0}".format(os.path.basename(filename)))
				filepath = os.path.join(root, filename)
				output_filepath = os.path.join(output_dir, relative_directory, filename.rstrip(".gz")+".thdr")
				queue.put((filepath, output_filepath))
			
				if args.limit:
					file_count = file_count + 1
					if file_count > args.limit:
						sys.exit(1)
							
	else:
		for filename in os.listdir(source_dir):
			if is_fits_file(filepath=filename, read_compressed=args.compressed) == False:
				continue
			
			filepath = os.path.join(source_dir, filename)
			output_filepath = os.path.join(output_dir, filename.rstrip(".gz")+".thdr")
			queue.put((filepath, output_filepath))

	for i in range(n_processes):
		# An empty tuple signals we are done, one per worker.
		queue.put((None, None))

	# wait for all of the consumer threads to finish
	# ----------------------------------------------
	pool.close()
	pool.join()
	
