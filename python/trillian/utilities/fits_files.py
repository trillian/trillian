#!/usr/bin/env python

"""
This module is a starting point for utility functions. Will almost certainly by reorganized as it grows.

Created 2 May 2016
@author: Demitri Muna
"""

import os
import fitsio

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
	