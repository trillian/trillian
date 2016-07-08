#!/usr/bin/env python

"""
This module is a starting point for utility functions. Will almost certainly by reorganized as it grows.

Created 2 May 2016
@author: Demitri Muna
"""

import os
import bz2
import gzip
import pathlib # Python 3.4+

import fitsio

def is_fits_file(filepath, read_compressed=False, robust_check=False):
	'''
	Check if this is a FITS file from the extension (by default).
	Set robust_check=True to actually read the start of the file.
	'''
	is_fits = False
	allowed_suffixes = [r'\.fits$', r'\.fts$']
	
	if read_compressed:
		allowed_suffixes = allowed_suffixes + [r'\.fits.gz$', r'\.fts.gz$', r'\.fits.bz2$', r'\.fts.bz2$']

	is_fits = any([re.search(suffix, filepath, re.IGNORECASE) for suffix in allowed_suffixes])
	
	if is_fits and robust_check:
		fits_start = "SIMPLE  =                    T" # start of every FITS file
		
		suffix = pathlib.Path(filepath).suffix.lower()[1:] # remove the leading '.'
		
		if suffix in ['fits', 'fts']: # 'suffix' returns the very last suffix
			with open(filepath) as f:
				is_fits = (f.read(30).decode('utf-8') == fits_start)
			
		elif read_compressed:
			if suffix == 'gz':
				is_fits = (gzip.open(filepath).read(30).decode('utf-8') == fits_start)
			elif suffix == 'bz2':
				is_fits = (bz2.open(filepath).read(30).decode('utf-8') == fits_start)
		
	return is_fits

def extract_FITS_header(filepath=None, HDU=None):
	'''
	Function to extract the header from a FITS file to a JSON object.
	
	In addition to the complete contents of the header, file metadata is also
	read into the returned JSON object, including the byte offsets and file size.
	
	:filepath: The full path + filename to the FITS file
	:HDU: The HDU number of the header to extract (default=all headers, 1=first header)
	:returns: ductionary containing all headers plus metadata
	'''
	
	# validation
	if filepath is None:
		raise Exception("A filepath must be specified (none provided)")
	
	if HDU == 0:
		raise Exception("An HDU value of '0' was given; note that HDU numbers start with 1.")
	
	# read the file
	try:
		hduList = fitsio.FITS(filepath)
	except OSError:
		raise Exception("The provided filepath ('{0}') could not be found.".format(filepath))
	
	data = dict() # dictionary that will be returned

	headers = list()	
	
	for i, hdu in enumerate(hduList):
	
		header_data = dict() # dictionary of all header data

		# read header
		header = hdu.read_header() # -> fitsio.FITSHDR
		cards = list()
		for record in header.records():
			cards.append(record["card"]) # only read the "raw" header line
		header_data["header"] = cards
		
		header_data["hdu"] = i+1
		
		# read byte offsets
		info = hdu.get_info()
		header_data["header_start"] = info["header_start"]
		header_data["data_start"] = info["data_start"]
		header_data["data_end"] = info["data_end"]
		
		headers.append(header_data)
	
	data["headers"] = headers
	
	# get file-level data
	# -------------------
	data["size"] = os.path.getsize(filepath)

	filepath = filepath.rstrip(".gz")
	data["filename"] = os.path.basename(filepath)
	data["filepath"] = os.path.dirname(filepath)
	
	return data
	