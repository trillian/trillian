#!/usr/bin/env python

"""
This module is a starting point for utility functions. Will almost certainly by reorganized as it grows.

Created 2 May 2016
@author: Demitri Muna
"""

import re
import os
import bz2
import json
import gzip
import pathlib # Python 3.4+
import subprocess
import logging

import fitsio

from ..files import sha256hash
from .remote import FITSMetadataRemoteReader

# bitpix values -> bitpix:bytes
bitpix2byteSize = {8:1, 16:2, 32:4, 64:8, -32:4, -64:8}

def is_fits_file(filepath, read_compressed=False, simple_check=False):
	'''
	Check if this is a FITS file from the extension (by default).
	Set simple_check=True to actually read the start of the file.
	'''
	is_fits = False
	allowed_suffixes = [r'\.fits$', r'\.fts$', r'\.fit$'] # will ignore case below
	
	if read_compressed:
		allowed_suffixes = allowed_suffixes + [r'\.fits\.gz$', r'\.fts\.gz$', r'\.fit\.gz$', r'\.fits\.bz2$', r'\.fts\.bz2$', r'\.fit\.bz2$']

	is_fits = any([re.search(suffix, filepath, re.IGNORECASE) for suffix in allowed_suffixes])
	
	if is_fits and simple_check:
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

def fitsmd_from_file(file=None):
	'''
	Create a FITS metadata structure from a FITS file (file or http).
	'''
	if file.startswith("http"):
		metadata = FITSMetadataRemoteReader(url=file)
		return metadata.jsonRepresentation
	else:
		metadata_dictionary = extract_FITS_header(file)
		return json.dumps(metadata_dictionary)

def extract_FITS_header(filepath=None):
	'''
	Function to extract the header from a FITS file to a JSON object.
	
	In addition to the complete contents of the header, file metadata is also
	read into the returned JSON object, including the byte offsets and file size.
	
	:filepath: The full path + filename to the FITS file
	:returns: dictionary containing all headers plus metadata
	'''
	
	# validation
	if filepath is None:
		raise Exception("A filepath must be specified (none provided)")
	
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
		# -----------
		header = hdu.read_header() # -> fitsio.FITSHDR
		cards = list()
		for record in header.records():
			cards.append(record["card_string"]) # only read the "raw" header line
		header_data["header"] = cards
		
		header_data["hdu_number"] = i+1
		
		# read byte offsets
		# -----------------
		# data_end includes the zero padding
		# data_end includes the next byte, e.g. reading [0:data_end]
		#   includes one more byte than needed. This means that data_end
		#   for one HDU is the same value as hdu_start for the next HDU.
		#   Subtract 1 to correct.
		info = hdu.get_info()
		header_data["hdu_start"] = info["header_start"]
		header_data["hdu_end"] = info["data_end"] - 1
		
		# calculate data length
		# ---------------------
		pcount = header.get('PCOUNT', 0) # default values that do not affect data length
		gcount = header.get('GCOUNT', 1)
		
		naxis = header['NAXIS']
		axes = list()
		for i in range(naxis):
			axes.append(header['NAXIS'+str(i+1)])
		if len(axes) == 0:
			data_length = 0
		else:
			naxes_product = axes[0]
			for axis in axes[1:]:
				naxes_product = axis * naxes_product
			naxes_product = naxes_product + pcount
			bitpix = header['BITPIX']
			data_length = naxes_product * bitpix2byteSize[bitpix] * gcount
		
		header_data["data_length"] = data_length
		if data_length > 0:
			header_data["data_start"] = info["data_start"]
		
		headers.append(header_data)
	
	data["headers"] = headers
	
	# get file-level data
	# -------------------
	data["size"] = os.path.getsize(filepath) # size of file as it is now
		
	# get the uncompressed and compressed sizes
	# 
	if filepath.endswith(".gz"):
		# gzip stores the original size of the file
		p = subprocess.Popen(['gzip', '-l', filepath], stdout=subprocess.PIPE)
		output = p.communicate()[0]
		output = output.decode("utf-8")
		
		# Output example:
	    # compressed uncompressed  ratio uncompressed_name
	    #   2913418     23056624  87.3% wise_metadata.txt
		try:
			m = re.search('\s([0-9]+)\s+([0-9]+)', str(output).split("\n")[1])
			data["size_compressed"] = int(m.groups()[0])
			data["size_uncompressed"] = int(m.groups()[1])
		except Exception as e:
			logging.warning("Size determination for gzip file failed: '{0}'".format(e))

	elif filepath.endswith(".bz2"):
		# have to do this manually, but this method doesn't write anything to disk
		p = subprocess.call(['bzip2', '-l', filepath], stdout=subprocess.PIPE)
		output = p.communicate()[0]
		output = output.decode("utf-8")
		
		try:
			data["size_uncompressed"] = int(output) # make sure it's a number
		except Exception as e:
			logging.warning("Size calculation for bzip2 file failed: '{0}'".format(e))
		
		data["size_compressed"] = data["size"]
		
	elif filepath.split(".")[-1].lower in ["fits", "fts"]:
		data["size_uncompressed"] = data["size"]

	# filename and path
	# 
	#filepath_without_ext = filepath.rstrip(".gz")
	data["filename"] = os.path.basename(filepath)
	data["filepath"] = os.path.dirname(filepath)
	
	# calculate the sha256 hash for the file
	data["sha256"] = sha256hash(filepath)
	
	return data
	
