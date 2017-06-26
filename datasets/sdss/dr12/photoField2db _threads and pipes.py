#!/usr/bin/env python

from __future__ import print_function

'''
This script loads photoField-*.fits files into the SDSS photodb database.
This is effectively a stand-alone table and should be run before loading photoObj-*.fits files.

If the base directory is not provided, the script will look in the current directory for the data.
'''

import os
import sys
import glob
import numpy as np
import fitsio
import argparse
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.dialects.postgresql import array as pg_array

import psycopg2
from cStringIO import StringIO
import threading
from psycopg2.pool import ThreadedConnectionPool
from contextlib import contextmanager
from psycopg2.extensions import QuotedString

import trillian.database.connections import RemoteTunnelConnection as dsn
#from trillian.database.connections import LocalhostConnection import dsn
from trillian.database.photodb.ModelClasses import Field, Run
import trillian.database.NumpyAdaptors

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
#session = db.Session()

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

# columns removed: skyversion, run, rerun
column_names = ['fieldid', 'skyversion', 'run', 'rerun', 'camcol', 'field', 'ntotal',
				'nobjects', 'nchild', 'ngals', 'nstars', 'ncr', 'nbrightobj', 'nfaintobj',
				'quality', 'mjd', 'a', 'b', 'c', 'd', 'e', 'ff', 'drow0', 'drow1', 'drow2',
				'drow3', 'dcol0', 'dcol1', 'dcol2', 'dcol3', 'csrow', 'cscol', 'ccrow', 'cccol',
				'ricut', 'airmass', 'muerr', 'nuerr', 'pixscale', 'ra', 'dec', 'cx', 'cy', 'cz',
				'ramin', 'ramax', 'decmin', 'decmax', 'primaryarea', 'rowoffset', 'coloffset',
				'saturation_level', 'neff_psf', 'sky_psp', 'sky_frames', 'sky_frames_sub', 'sigpix',
				'dev_ap_correction', 'dev_ap_correctionerr', 'exp_ap_correction', 'exp_ap_correctionerr',
				'dev_model_ap_correction', 'dev_model_ap_correctionerr', 'exp_model_ap_correction',
				'exp_model_ap_correctionerr', 'median_fibercolor', 'median_psfcolor', 'q', 'u', 'sky',
				'skysig', 'skyerr', 'skyslope', 'lbias', 'rbias', 'psf_nstar', 'psf_ap_correctionerr',
				'psf_sigma1', 'psf_sigma2', 'psf_b', 'psf_p0', 'psf_beta', 'psf_sigmap', 'psf_width',
				'psf_psfcounts', 'psf_sigma1_2g', 'psf_sigma2_2g', 'psf_b_2g', 'psfcounts', 'prof_nprof',
				'prof_mean_nmgy', 'prof_med_nmgy', 'prof_sig_nmgy', 'gain', 'dark_variance', 'score',
				'aterm', 'kterm', 'kdot', 'ref_tai', 'tai', 'psp_status', 'photo_status', 'image_status',
				'calib_status', 'nstars_offset', 'field_offset', 'nmgypercount', 'nmgypercount_ivar',
				'ifield', 'mu_start', 'mu_end', 'nu_start', 'nu_end', 'ifindx', 'nbalkan']
col_idx = dict()
for idx, field in enumerate(column_names):
	col_idx[field] = idx

for excluded_field in ['skyversion', 'run', 'rerun']:
	column_names.remove(excluded_field)
#for extra_field in ['filename', 'run_pk']
#	column_names.append(extra_field)


@contextmanager
def database_cursor(pool):
	'''
	This function allows one to use a database connection without having to worry about
	returning it to the pool when we're done with it.
	
	Example usage:
	
	with database_cursor(pool) as cursor:
		# do stuff with cursor, can even return from block
		# will return connection to pool when block is done
	'''
	# --------------------------
	# ON ENTER OF WITH STATEMENT
	# --------------------------
	# perform any setup/initialization here
	dbconnection = pool.getconn()
	yield dbconnection.cursor()
	
	# -------------------------
	# ON EXIT OF WITH STATEMENT
	# -------------------------
	# this gets called on exit of the "with" block, no matter what
	#app.logger.debug("Returning connection to the pool")
	pool.putconn(dbconnection)	


#db_connection = psycopg2.connect(args.database_connection_string)
pool = ThreadedConnectionPool(minconn=1, maxconn=10, dsn=db.dsn)
db_connection = pool.getconn()

def copy_into_db(copy_data=None, columns=None):
	with database_cursor(pool) as cursor:
		cursor.copy_from(file=os.fdopen(copy_data), table='sdssphoto.field', columns=columns, null="NULL")
		cursor.close()
		cursor.connection.commit()

def ndarray2pgcopy(a=None, convert_null=False):
	''' Convert an ndarray object to a string appropriate for use with the COPY command.
		Format is (including quotes!):
			{1,2,3,4}
			{{1,2,3,4}, {5,6,7,8}}
		convert_null converts -9999 values to NULL
	'''
	if len(value.shape) == 1: # 1-d array
		s = "{{{0}}}".format(",".join([str(x) for x in value]))
	else:
		#iterate over dimensions
		a = list()
		for dim in range(value.shape[-1]):
			a.append("{{{0}}}".format(",".join([str(x) for x in value[...,dim]])))
		s = "{{{0}}}".format(",".join(a))
	
	if convert_null:
		return s.replace("-9999.0", "NULL")
	else:
		return s
			
# COPY sdssphoto.field (<fields>) FROM stdin;\n
# <tab delimited list>

session = db.Session()

for photo_field_filepath in glob.glob(os.path.join(base_directory, "8162", "photoField-*.fits")):

	# The file contains a list of Field records.

	#photoFieldFile = PhotoFieldFile(photo_field_filepath)
	filename = os.path.basename(photo_field_filepath)

	dataHDU = fitsio.FITS(photo_field_filepath)[1]
	#row1 = dataHDU.read(rows=[0,0])
	#column_names = [x.lower() for x in row1.dtype.names]
	#print(column_names)
	
	if args.verbose:
		print("Processing {0}...".format(filename))
	
	#session.begin() # one session per file
	
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
	
	sql_copy_io = StringIO()
	(r_fd, w_fd) = os.pipe() # (read, write) file descriptors
	
	copy_thread = threading.Thread(target=copy_into_db, args=(sql_copy_io, column_names))
	copy_thread.start()

	# iterate over each row in the FITS file.
	for row in dataHDU[0:2]:
		
		#new_field = Field()
		#session.add(new_field)

		# handle metadata first
		#new_field.filename = filename

		#columns = list(column_names)
		#row_dict = dict(zip(column_names, row))
		
		# handle exceptions - names that are different between the FITS file and database
		#new_field.run = run
		
		# remove fields in "run" table
		#for field in ["skyversion", "run", "rerun"]:
		#	del row_dict[field]	
					
		#for column in row_dict.keys():
		#	if debug:
		#		if not hasattr(new_field, column):
		#			print("mismatched column name: {0}".format(column))
		#	
		#	setattr(new_field, column, row_dict[column])
		
		values = list() # final values to output
		for col in column_names:
			value = row[col_idx[col]]
			value_type = type(value)
			#print("======= processing col: {0} ({1})".format(col, type(value)))

			if value_type in [np.uint8, np.int32, np.int16, np.float64, np.float32]:
				value = str(value)
			elif value_type == np.string_:
				value = QuotedString(value).getquoted()
			elif value_type == np.ndarray:
				value = ndarray2pgcopy(value, convert_null=True)
			else:
				print("Unhandled data type: {0}".format(value_type))
				sys.exit(1)
			values.append(value)
		
		# extra fields
		values.append(QuotedString(filename).getquoted())
		values.append(str(run.pk))
		
		for idx, x in enumerate(values):
			if x == None:
				values[idx] = "NULL"
		
		print("\t".join(values))
		sql_copy_io.write("\t".join(values))
		sql_copy_io.write("\n")
		
		#print(sql_copy_io.getvalue())
		sql_copy_io.close()
	
	copy_thread.join()	
	#print (sql_copy_io.getvalue())
	sys.exit(1)
		
	#session.rollback()
	
	# just read one file for now
	#print("Exiting reading just one file.")
	#sys.exit(1)




