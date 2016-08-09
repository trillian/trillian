#!/usr/bin/env python

"""
This is a collection of file handling utilities.

Created 9 August 2016
@author: Demitri Muna
"""

import hashlib

def hashfile(filepath=None, hasher=hashlib.sha256(), blocksize=1e7):
	'''
	Generate a hash for the given file of any size (reads file in blocks). 
	Uses the sha256 hash algortihm by default.
	Block size is 1MB by default.
	NOTE! The file must be opened in mode='rb', otherwise an attempt will
	      be made to interpret it as utf-8.
	'''
	with open(filepath, mode='rb') as f:
		buf = file_object.read(blocksize)
		while len(buf) > 0:
			hasher.update(buf)
			buf = file_object.read(blocksize)
	return hasher.hexdigest()
