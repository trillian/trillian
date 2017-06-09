#!/usr/bin/env python

"""
This is a collection of file handling utilities.

Created 9 August 2016
@author: Demitri Muna
"""

import os
import mmap
import hashlib
import subprocess

def sha256hash(filepath=None):
	'''
	Generate a sha256 hash for the given file path.
	'''
	if os.path.exists("/usr/bin/sha256sum"):
		p = subprocess.Popen(['/usr/bin/sha256sum', filepath], stdout=subprocess.PIPE)
		output = p.communicate()[0]
		output = output.decode("utf-8")
		# output format: <hash> <filename>
		return output.split()[0]
		
	elif os.path.exists("/usr/bin/shasum"):
		# macOS version
		# --portable flag "produces same digest on Windows/Unix/Mac"
		#
		p = subprocess.Popen(['/usr/bin/shasum', '--portable', '--algorithm', '256', filepath], stdout=subprocess.PIPE)
		output = p.communicate()[0]
		output = output.decode("utf-8")
		# output format: <hash> <filename>
		return output.split()[0]

	else:
		# no shell command found - calculate with Python library
		#
		# TODO: this does not produce the same output as /usr/bin/shasum on macOS
		#
		hasher = hashlib.sha256()
		filesize = os.path.getsize(filepath)
		file = open(filepath, mode="rb")
		m = mmap.mmap(file.fileno(), length=filesize, prot=mmap.PROT_READ)
		hasher.update(m)
		return hasher.hexdigest()

		# alternate method:
		# with open(filename, mode='rb') as f:
		#	return hashlib.sha256(f.read()).hexdigest()