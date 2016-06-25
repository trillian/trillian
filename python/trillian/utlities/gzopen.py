# -*- coding:utf-8 -*-

'''
Utility to enable reading of gzip files in the same way as regular files.

Usage:

from gzopen import gzopen
with gzopen('tmp.txt.gz') as f:
    f.read()

Ref: http://www.genomearchitecture.com/2014/01/how-to-gunzip-on-the-fly-with-python

'''

import gzip

class gzopen(object):
	"""Generic opener that decompresses gzipped files
	if needed. Encapsulates an open file or a GzipFile.
	Use the same way you would use 'open()'.
	"""
	def __init__(self, fname):
		f = open(fname)
		# Read magic number (the first 2 bytes) and rewind.
		magic_number = f.read(2)
		f.seek(0)
		# Encapsulated 'self.f' is a file or a GzipFile.
		if magic_number == '\x1f\x8b':
			self.f = gzip.GzipFile(fileobj=f)
		else:
			self.f = f

	# Define '__enter__' and '__exit__' to use in
	# 'with' blocks. Always close the file and the
	# GzipFile if applicable.
	def __enter__(self):
		return self
	def __exit__(self, type, value, traceback):
		try:
			self.f.fileobj.close()
		except AttributeError:
			pass
		finally:
			self.f.close()

	# Reproduce the interface of an open file
	# by encapsulation.
	def __getattr__(self, name):
		return getattr(self.f, name)
	def __iter__(self):
		return iter(self.f)
	def next(self):
		return next(self.f)