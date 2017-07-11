#!/usr/bin/env python

#from __future__ import print_function

'''
This script loads photoRun-*.fits files into the sdssphoto database.
This is effectively a stand-alone table and should be run before loading photoField-*.fits files.

If the base directory is not provided, the script will look in the current directory for the data.
'''

import os
import sys
import glob
import numpy
import fitsio
import argparse
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.dialects.postgresql import array as pg_array

import trillian.database.connections import RemoteTunnelConnection as db
#from trillian.database.connections import LocalhostConnection import db
from trillian.database.photodb.ModelClasses import Run
import sdss.database.NumpyAdaptors

debug = True # turn this on while debugging or in development

# -----------------------------------------------------------------
# This block of code tells Python to drop into the debugger
# if there is an uncaught exception when run from the command line.
def info(type, value, tb):
   if hasattr(sys, 'ps1') or not sys.stderr.isatty():
      # we are in interactive mode or we don't have a tty-like
      # device, so we call the default hook
      sys.__excepthook__(type, value, tb)
   else:
      import traceback, pdb
      # we are NOT in interactive mode, print the exception...
      traceback.print_exception(type, value, tb)
      print
      # ...then start the debugger in post-mortem mode.
      pdb.pm()
sys.excepthook = info
# -----------------------------------------------------------------


parser = argparse.ArgumentParser(description="Script to load photoRun FITS files into a database.",
								 usage="photoRun2db.py -d data_directory_path")

# plateruns
parser.add_argument("-d", "--base-directory", default=None, help="directory containing reduction", required=False)
parser.add_argument("-c", "--database-connection-string", default=None, help="database connection string", required=True)
parser.add_argument("-v", "--verbose", action="store_true", help="display progress messages", required=False)

args = parser.parse_args()

# Reduction directory structure:
#
# $BASE_DIRECTORY/<run>/photoField-<run>-<camcol>.fits
#                      /photoRun-<run>.fits
#                      /<camcol>/photoObj-<run>-<camcol>-<field>.fits
#

# -------------
# get directory
# -------------
if args.base_directory:
	base_directory = args.base_directory
else:
	# no directory given; use current directory
	base_directory = os.getcwd()

# -------------------
# database connection
# -------------------
session = db.Session()

class PhotoRunFile(object):
	
	def __init__(self, filepath=None):
		self.filepath = filepath
		self._column_names = None
		self.hdu_list = fitsio.FITS(filepath) #, iter_row_buffer=25)
	
	@property
	def dataHDU(self):
		return self.hdu_list[1]
	
	@property
	def column_names(self):
		if self._column_names == None:
			row1 = self.dataHDU.read(rows=[0,0])
			self._column_names = [x.lower() for x in row1.dtype.names]
		return self._column_names
	
#column_names = None

for filepath in glob.glob(os.path.join(base_directory, "8162", "photoRun-*.fits")):

	# The file contains a list of Field records.

	session.begin()

	photoRunFile = PhotoRunFile(filepath)
	filename = os.path.basename(filepath)

	if args.verbose:
		print("Processing {0}...".format(filename))
	
	try:
		session.query(Run).filter(Run.filename == filename).one()
		#print ("found")
		continue # already in database, go to next file
	except sqlalchemy.orm.exc.NoResultFound:
		pass # continue below
		# file not found - create a new one
	#	new_field = Field()
	#	session.add(new_field)

	# handle metadata first
	#new_field.filename = filename
	
	# iterate over each row in the FITS file.
	for row in photoRunFile.dataHDU[0:]:

		new_run = Run()
		session.add(new_run)

		# handle metadata first
		new_run.filename = filename

		row_dict = dict(zip(photoRunFile.column_names, row))
		
		# handle exceptions - names that are different between the FITS file and database

			# none
		
		for column in row_dict.keys():
			if debug:
				if not hasattr(new_run, column):
					print("mismatched column name: {0}".format(column))
			
			#print("{2} {0} : {1}".format(row_dict[column], type(row_dict[column]), column))
			
			#if type(row_dict[column]) == numpy.ndarray:
			#if isinstance(row_dict[column], numpy.ndarray):
				# don't use "isinstance(x, numpy.ndarray)" as numpy.string_ will match
			#	setattr(new_run, column, row_dict[column].tolist())
			#else:
			setattr(new_run, column, row_dict[column])
	
	session.commit()
	
	# just read one file for now
	#print("Exiting reading just one file.")
	#sys.exit(1)




