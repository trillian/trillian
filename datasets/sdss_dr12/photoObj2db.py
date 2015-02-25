#!/usr/bin/env python

from __future__ import print_function

'''
This script loads photoObj-*.fits files into the SDSS photodb database.
Is is expected that the field table is populated before running this (see: photoField2db.py).

If the base directory is not provided, the script will look in the current directory for the data.

Sample database connection strings:
postgresql://sdssdb_admin:xxxx@localhost:5500/utahdb

'''

#import cProfile
#import pstats

import os
import sys
import glob
import time
import numpy
import fitsio
import argparse
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.dialects.postgresql import array as pg_array

import trillian.database.connections import RemoteTunnelConnection as dsn
#from trillian.database.connections import LocalhostConnection import dsn
from trillian.database.photodb.ModelClasses import PhotoObj, Field, Run, Thing, FlagType, FlagValue, ObjectType, PhotoObjToFlag
import trillian.database.NumpyAdaptors

debug = True # turn this on while debugging or in development

parser = argparse.ArgumentParser(description="Script to load photoField FITS files into a database.",
								 usage="%% photoField2db.py ...")

# plateruns
parser.add_argument("-d", "--base-directory",  default=None, help="directory containing reduction", required=False)
#parser.add_argument("-c", "--database-connection-string",  default=None, help="database connection string", required=True)
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

def int2bits(value, bits=64):
	''' For a given integer, returns an array of the bit positions that are "on".
		The first bit is position 0, the second bit 1, etc.
		As a test, "21" should return bits [0, 2, 4].
	'''
	return [x for x in range(bits) if (value & (1 << x)) != 0]

idxToFilter = {0:'u', 1:'g', 2:'r', 3:'i', 4:'z'}

class PhotoObjFile(object):
	
	def __init__(self, filepath=None):
		self.filepath = filepath
		self._column_names = None
		self.hdu_list = fitsio.FITS(filepath) # note - not ever closed
		self.hdu_list[1].lower = True # returns lowercase column names - doesn't seem to work
		self._column_names = None
		self.filename = os.path.basename(filepath)
		
	# support for the "with" construct
	def __enter__(self):
		return self
		
	def __exit__(self, type, value, traceback):
		self.hdu_list.close()
	
	@property
	def dataHDU(self):
		return self.hdu_list[1]
	
	@property
	def column_names(self):
		if self._column_names == None:
			self._column_names = [x.lower() for x in self.dataHDU.get_colnames()]
		return self._column_names
		
	def first_objid(self):
		return self.dataHDU.read(rows=[0,0])[0][0]
		#row1 = self.dataHDU.read(rows=[0,0])
		#print(row1[0][0])
	
#def main():
if True:

	#column_names = None

	# dictionaries to cache objects
	object_types = dict()
	object1_flags = dict()
	object2_flags = dict()
	resolve_status_flags = dict()
	photo_flags = dict()
	photo_flags2 = dict()

	field = None

	for photoObj_filepath in glob.glob(os.path.join(base_directory, "*", "[1-6]", "photoObj-*.fits")):
	
		with PhotoObjFile(photoObj_filepath) as photoObjFile: # will close file when done

			# I expect "objid" values are unique across all files. Look for the first one to
			# see if this file has been loaded before. (This script won't import partial files.)
			if session.query(PhotoObj.objid).filter(PhotoObj.objid == photoObjFile.first_objid()).count() > 0:
				continue # already in database, go to next file
			
			start = time.time()
			
			col2idx = dict(zip(range(len(photoObjFile.column_names)), photoObjFile.column_names))
		
			if args.verbose:
				print("Processing {0}...".format(photoObjFile.filename))
			session.begin()

			# save previous photoObj records to tie child entries back to parents.
			photoObjDict = dict()

			# iterate over each row in the FITS file.
			for row_no, row in enumerate(photoObjFile.dataHDU):
				#print("    row {0}".format(row_no))

				new_obj = PhotoObj()
				session.add(new_obj)

				#columns = list(photoObjFile.column_names)
				row = dict(zip(photoObjFile.column_names, row))
		
				# Deal with columns that require special handling.
				# ------------------------------------------------
		
				# --------
				# parentid - note that empty values are 18 spaces...ugh.
				#
				# I'm assuming that parent objects are always first and always followed by their children.
				# Objects are hierarchical - children can have children.
				#print(row.keys())
				parent_id = str(row["parentid"]).strip() # is a numpy string
				objid = str(row['objid']).strip()
				if row["parent"] == -1:
					# this is a to-level parent object
					new_obj.parent = None # parent_id
					photoObjDict.clear()
				else:
					try:
						new_obj.parent = photoObjDict[parent_id]
					except KeyError:
						print("key error: {0}".format(parent_id))
						print(photoObjDict)
						for key in photoObjDict.keys():
							print(key)
						sys.exit(1)
				photoObjDict[objid] = new_obj

				del row["parentid"] # handled
				del row["parent"] # index internal to file

				# -----
				# field
				#
				# photoObj.field == photoField.field
				# all entries in this file are in the same field, so only look it up once
				if field == None:
					try:
						# a field is uniquely identified by run/camcol/rerun/field
						field = session.query(Field).join(Run).filter(Run.run == row["run"]) \
													.filter(Field.camcol == row["camcol"]) \
													.filter(Run.rerun == row["rerun"]) \
													.filter(Field.field == row["field"]).one()
					except sqlalchemy.orm.exc.NoResultFound:
						print("\nA photoObj field with an id of '{0}' could not be found!\n\n".format(row["field"]))
			
				new_obj.field = field
				del row["field"]

				# --------
				# thing_id
				#
				if row["thing_id"] != -1:
					try:
						thing = session.query(Thing).filter(Thing.thing_id == row["thing_id"]).one()
					except sqlalchemy.orm.exc.NoResultFound:
						thing = Thing(row["thing_id"])
						session.add(thing)
					new_obj.things.append(thing)
				del row["thing_id"]
		
				# -----------
				# object type
				#
				try:
					object_type = object_types[row["objc_type"]]
				except KeyError:
					try:
						object_type = session.query(ObjectType).filter(ObjectType.value == row["objc_type"]).one()
						object_types[row["objc_type"]] = object_type
					except sqlalchemy.orm.exc.NoResultFound:
						print("The table 'object_type' either hasn't been loaded or the value '{0}' wasn't found.".format(row["objc_type"]))
						sys.exit(1)
				new_obj.objectType = object_type
				del row["objc_type"]
			
				# ------------
				# object1 flag
				#
				if row["objc_flags"] < 0:
					# correct for negative values, see: http://www.phy.ornl.gov/csep/CSEP/RN/NODE15.html
					row["objc_flags"] = row["objc_flags"] & 0x7fffffff # 32 bit value
				for bit in int2bits(int(row["objc_flags"])):
					try:
						object1_flag = object1_flags[bit]
					except KeyError:
						try:
							object1_flag = session.query(FlagValue).join(FlagType).filter(FlagType.label == 'OBJECT1')\
																   .filter(FlagValue.bit == bit).one()
							#object1_flag = session.query(Object1Flag).filter(Object1Flag.bit == bit).one()
							object1_flags[bit] = object1_flag
						except sqlalchemy.orm.exc.NoResultFound:
							print("The FlagType or FlagValues tables either haven't been loaded or the bit value '{0}' wasn't found for type '{1}'.".format(row["objc_flags"], 'OBJECT1'))
							sys.exit(1)
					#new_obj.object1Flags.append(object1_flag)
					new_obj.flags.append(object1_flag)
				new_obj.objc_flags = row["objc_flags"]
				del row["objc_flags"]

				# ------------
				# object2 flag
				#
				if row["objc_flags2"] < 0:
					# correct for negative values, see: http://www.phy.ornl.gov/csep/CSEP/RN/NODE15.html
					row["objc_flags2"] = row["objc_flags2"] & 0x7fffffff # 32 bit value
				for bit in int2bits(int(row["objc_flags2"])):
					try:
						object2_flag = object2_flags[bit]
					except KeyError:
						try:
							object2_flag = session.query(FlagValue).join(FlagType).filter(FlagType.label == 'OBJECT2')\
																   .filter(FlagValue.bit == bit).one()
							#object2_flag = session.query(Object2Flag).filter(Object2Flag.bit == bit).one()
							object2_flags[bit] = object2_flag
						except sqlalchemy.orm.exc.NoResultFound:
							print("The FlagType or FlagValues tables either haven't been loaded or the bit value '{0}' wasn't found for type '{1}'.".format(row["objc_flags"], 'OBJECT2'))
							sys.exit(1)
					#new_obj.object2Flags.append(object2_flag)
					new_obj.flags.append(object2_flag)
				new_obj.objc_flags2 = row["objc_flags2"]
				del row["objc_flags2"]
			
				# -----------
				# photo_flags
				#
				# These flags are called "flags" and "flags1" in the file, renamed to "photo_flags" and "photo_flags2"
				# in the database. These are the same as the OBJECT[12] flags, but this field breaks them down by filter.
				#
				# Ref: http://www.sdss3.org/dr10/algorithms/bitmask_flags1.php
				#      http://www.sdss3.org/dr10/algorithms/bitmask_flags2.php
				for filter_idx, flags_by_filter in enumerate(row["flags"]):
					for bit in int2bits(int(flags_by_filter)):
						try:
							photo_flag_value = photo_flags[bit]
						except KeyError:
							try:
								photo_flag_value = session.query(FlagValue).join(FlagType).filter(FlagType.label == 'PHOTO_FLAGS')\
																	   .filter(FlagValue.bit == bit).one()
								photo_flags[bit] = photo_flag_value
							except sqlalchemy.orm.exc.NoResultFound:
								print("The FlagType or FlagValues tables either haven't been loaded or the bit value '{0}' wasn't found for type '{1}'.".format(bit, 'PHOTO_FLAGS'))
								sys.exit(1)
						new_photo_flag = PhotoObjToFlag()
						session.add(new_photo_flag)
						new_photo_flag.filter = idxToFilter[filter_idx]
						new_photo_flag.photoObj = new_obj
						new_photo_flag.flagValue = photo_flag_value
				new_obj.photo_flags = row["flags"]
				del row['flags']

				for filter_idx, flags_by_filter in enumerate(row["flags2"]):
					for bit in int2bits(int(flags_by_filter)):
						try:
							photo_flag2_value = photo_flags2[bit]
						except KeyError:
							try:
								photo_flag2_value = session.query(FlagValue).join(FlagType).filter(FlagType.label == 'PHOTO_FLAGS2')\
																	   .filter(FlagValue.bit == bit).one()
								photo_flags2[bit] = photo_flag2_value
							except sqlalchemy.orm.exc.NoResultFound:
								print("The FlagType or FlagValues tables either haven't been loaded or the bit value '{0}' wasn't found for type '{1}'.".format(bit, 'PHOTO_FLAGS2'))
								sys.exit(1)
						new_photo_flag2 = PhotoObjToFlag()
						session.add(new_photo_flag2)
						new_photo_flag2.filter = idxToFilter[filter_idx]
						new_photo_flag2.photoObj = new_obj
						new_photo_flag2.flagValue = photo_flag2_value
				new_obj.photo_flags = row["flags2"]
				del row['flags2']
			
				# --------------
				# resolve_status
				#
				# only bits 1-11 defined
				for bit in int2bits(int(row["resolve_status"]), bits=16):
					try:
						resolve_status_flag = resolve_status_flags[bit]
					except KeyError:
						try:
							resolve_status_flag = session.query(FlagValue).join(FlagType).filter(FlagType.label == 'RESOLVE_STATUS')\
																   .filter(FlagValue.bit == bit).one()
							#resolve_status_flag = session.query(ResolveStatusFlag).filter(ResolveStatusFlag.bit == bit).one()
							resolve_status_flags[bit] = resolve_status_flag
						except sqlalchemy.orm.exc.NoResultFound:
							print("The table 'resolve_status_flag' either hasn't been loaded or the bit value '{0}' wasn't found.".format(row["resolve_status"]))
							sys.exit(1)
					#new_obj.object2Flags.append(resolve_status_flag)
					new_obj.flags.append(resolve_status_flag)
				del row["resolve_status"]
			
				# ----------
				# Columns to skip as they are already in the "field" table or redundant
				for col in ["fieldid", "skyversion", "run", "rerun", "camcol", "nchild", "mjd", "ifield", "score"]:
					del row[col]
			
				# other clean up
				if row["balkan_id"] == -1:
					row["balkan_id"] = None
				for col in ["objc_prob_psf", "rowvdeg", "rowvdegerr", "colvdeg", "colvdegerr"]:
					if int(row[col]) == -9999:
						row[col] = None
					
				# handle exceptions - names that are different between the FITS file and database
					# none
		
				for column in row.keys():
					if debug:
						if not hasattr(new_obj, column):
							print("mismatched column name: {0}".format(column))
	# 				if column == "petrothetaerr":
	# 					print (type(row[column]), row[column])
	# 					values = list(row[column])
	# 					print(values[0] == -9999)
	# 					print(values[0] == -9999.0)
	# 					print ([None if x == -9999.0 else x for x in values])
	#					sys.exit(1)
	#				if isinstance(row[column], numpy.ndarray):
	#					values = row[column].tolist()
	#					values = [None if x == -9999.0 else x for x in values]
	#					setattr(new_obj, column, values)
	#				else:

					setattr(new_obj, column, row[column])
		
				## end loop over rows in one file

			## end with-file block
		
		elapsed = time.time() - start
		print("Time elapsed (no commit): {0}".format(elapsed))
		
		start = time.time()
		#print("committing")
		session.commit()
		
		print("time to commit: {0}".format(time.time() - start))
		print("")
	
		# just read one file for now
		#print("Exiting reading just one file.")
		#sys.exit(1)

if False:
	cProfile.run('main()', 'prof_stats')
	p = pstats.Stats('prof_stats')

	print("Cumulative time by function")
	p.sort_stats('cumulative').print_stats(20)

	print("Time spent within each function")
	p.sort_stats('time').print_stats(20)
