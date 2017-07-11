#!/usr/bin/env python

from __future__ import print_function

'''
This script loads photoField-*.fits files into the SDSS photodb database.
This is effectively a stand-alone table and should be run before loading photoObj-*.fits files.
The script "photoRun2db.py" must be run before this script.

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

import trillian.database.connections import RemoteTunnelConnection as dsn
#from trillian.database.connections import LocalhostConnection import dsn
from trillian.database.photodb.ModelClasses import Field, Run
import trillian.database.NumpyAdaptors

# NOTE: Some precision is being lost in the conversion from numpy numeric types
#       during str() (see NumpyAdaptors). As least that's one theory why it's happening.
#       A fix isn't completely clear.
# numpy.set_printoptions(precision=10) # this only adjusts display, not str()

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


parser = argparse.ArgumentParser(description="Script to load photoField FITS files into a database.",
								 usage="photoField2db.py -d data_directory_path")

# plateruns
parser.add_argument("-d", "--base-directory", default=None, help="directory containing reduction", required=False)
#parser.add_argument("-c", "--database-connection-string", default=None, help="database connection string", required=True)
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

# class PhotoFieldFile(object):
# 	
# 	def __init__(self, filepath=None):
# 		self.filepath = filepath
# 		self._column_names = None
# 		self.hdu_list = fitsio.FITS(filepath) #, iter_row_buffer=25)
# 	
# 	@property
# 	def dataHDU(self):
# 		return self.hdu_list[1]
# 	
# 	@property
# 	def column_names(self):
# 		if self._column_names == None:
# 			row1 = self.dataHDU.read(rows=[0,0])
# 			self._column_names = [x.lower() for x in row1.dtype.names]
# 		return self._column_names
	
#column_names = None

for photo_field_filepath in glob.glob(os.path.join(base_directory, "8162", "photoField-*.fits")):

	# The file contains a list of Field records.

	#photoFieldFile = PhotoFieldFile(photo_field_filepath)
	filename = os.path.basename(photo_field_filepath)

	dataHDU = fitsio.FITS(photo_field_filepath)[1]
	row1 = dataHDU.read(rows=[0,0])
	column_names = [x.lower() for x in row1.dtype.names]

	if args.verbose:
		print("Processing {0}...".format(filename))
	
	session.begin() # one session per file
	
	field_found = session.query(Field).filter(Field.filename == filename).limit(1).count() > 0
	if field_found:
		session.rollback()
		continue # already in database, go to next file

	# look up Run record
	run_value = dataHDU[0][0][2]
	try:
		run = session.query(Run).filter(Run.run == run_value).one()
	except sqlalchemy.orm.exc.NoResultFound:
		print("\nRecord for run '{0}' not found.\n").format(run_value)
		sys.exit(1)
	
	# handle metadata first
	#new_field.filename = filename
	
	# iterate over each row in the FITS file.
	for row in dataHDU:

		new_field = Field()
		session.add(new_field)

		# handle metadata first
		new_field.filename = filename

		#columns = list(column_names)
		row_dict = dict(zip(column_names, row))
		
		# handle exceptions - names that are different between the FITS file and database
		new_field.run = run
		
		# remove fields in "run" table
		for field in ["skyversion", "run", "rerun"]:
			del row_dict[field]	
					
		for column in row_dict.keys():
			if debug:
				if not hasattr(new_field, column):
					print("mismatched column name: {0}".format(column))
			
			setattr(new_field, column, row_dict[column])
	
	session.commit()
	
	# just read one file for now
	#print("Exiting reading just one file.")
	#sys.exit(1)




