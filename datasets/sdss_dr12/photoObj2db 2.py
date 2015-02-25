#!/usr/bin/env python

from __future__ import print_function

'''
This script loads photoObj-*.fits files into the SDSS photodb database.
Is is expected that the field table is populated before running this (see: photoField2db.py).

If the base directory is not provided, the script will look in the current directory for the data.

Sample database connection strings:
postgresql://sdssdb_admin:xxxx@localhost:5500/utahdb

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

from sdss.database.connections.UtahTunnelConnection import db
from sdss.database.photodb.ModelClasses import PhotoObj, Field, Thing, Object1Flag, Object2Flag, ResolveStatusFlag
import sdss.database.NumpyAdaptors

debug = True # turn this on while debugging or in development

parser = argparse.ArgumentParser(description="Script to load photoField FITS files into a database.",
								 usage="% photoField2db.py ...")

# plateruns
parser.add_argument("-d", "--base-directory",  default=None, help="directory containing reduction", required=False)
parser.add_argument("-c", "--database-connection-string",  default=None, help="database connection string", required=True)

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
	''' For a given integer, returns an array of the bit positions that are "on". '''
	return [x for x in range(0,bits) if (value & (1 << x)) != 0]

class PhotoObjFile(object):
	
	def __init__(self, filepath=None):
		self.filepath = filepath
		self._column_names = None
		self.hdu_list = fitsio.FITS(filepath) # note - not ever closed
		self.hdu_list[1].lower = True # returns lowercase column names - doesn't seem to work
		self._column_names = None
		
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
			
#column_names = None

# save previous photoObj records to tie child entries back to parents.
photoObjDict = dict()
object_types = dict()
object1_flags = dict()
object2_flags = dict()
resolve_status_flags = dict()

field = None

for photoObj_filepath in glob.glob(os.path.join(base_directory, "[1-6]", "photoObj-*.fits")):
	
	with PhotoObjFile(photoObj_filepath) as photoObjFile: # will close file when done

		# I expect "objid" values are unique across all files. Look for the first one to
		# see if this file has been loaded before. (This script won't import partial files.)
		try:
			session.query(PhotoObj).filter(PhotoObj.objid == photoObjFile.first_objid()).one()
			continue # already in database, go to next file
		except sqlalchemy.orm.exc.NoResultFound:
			pass

		col2idx = dict(zip(range(len(photoObjFile.column_names)), photoObjFile.column_names))

		session.begin()

		# iterate over each row in the FITS file.
		for row in photoObjFile.dataHDU[0:1]:

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
			#print(row.keys())
			parent_id = str(row["parentid"]).strip() # is a numpy string
			if len(parent_id) == 0:
				# this is a parent object
				new_obj.parent = parent_id
				photoObjDict.clear()
				photoObjDict[parent_id] = new_obj
			else:
				new_obj.parent = photoObjDict[parent_id]
			del row["parentid"] # handled

			# -----
			# field
			#
			# photoObj.field == photoField.field
			# all entries in this file are in the same field, so only look it up once
			if field == None:
				try:
					field = session.query(Field).filter(Field.field == row["field"]).one()
				except sqlalchemy.orm.exc.NoResultFound:
					print("\nA photoObj field with an id of '{0}' could not be found!\n\n".format(row["field"]))
					session.rollback()
					sys.exit(1)
			new_obj.fields.append(field)
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
				object_type = object_types[row["object_type"]]
			except KeyError:
				try:
					object_type = session.query(ObjectType).filter(ObjectType.value == row["object_type"]).one()
					object_types[row["object_type"]] = object_type
				except sqlalchemy.orm.exc.NoResultFound:
					print("The table 'object_type' either hasn't been loaded or the value '{0}' wasn't found.".format(row["object_type"]))
					sys.exit(1)
			new_obj.objectType = object_type
			del row["object_type"]
			
			# ------------
			# object1 flag
			#
			if row["object1_flag"] < 0:
				# correct for negative values, see: http://www.phy.ornl.gov/csep/CSEP/RN/NODE15.html
				row["object1_flag"] = row["object1_flag"] & 0x7fffffff # 32 bit value
			for bit in int2bits(row["object1_flag"]):
				try:
					object1_flag = object1_flags[bit]
				except KeyError:
					try:
						object1_flag = session.query(Object1Flag).filter(Object1Flag.bit == bit).one()
						object1_flags[bit] = object1_flag
					except sqlalchemy.orm.exc.NoResultFound:
						print("The table 'object1_flag' either hasn't been loaded or the bit value '{0}' wasn't found.".format(row["object_type"]))
						sys.exit(1)
				new_obj.object1Flags.append(object1_flag)
			del row["object1_flag"]

			# ------------
			# object2 flag
			#
			if row["object2_flag"] < 0:
				# correct for negative values, see: http://www.phy.ornl.gov/csep/CSEP/RN/NODE15.html
				row["object2_flag"] = row["object2_flag"] & 0x7fffffff # 32 bit value
			for bit in int2bits(row["object2_flag"]):
				try:
					object2_flag = object2_flags[bit]
				except KeyError:
					try:
						object2_flag = session.query(Object2Flag).filter(Object2Flag.bit == bit).one()
						object2_flags[bit] = object2_flag
					except sqlalchemy.orm.exc.NoResultFound:
						print("The table 'object2_flag' either hasn't been loaded or the bit value '{0}' wasn't found.".format(row["object_type"]))
						sys.exit(1)
				new_obj.object2Flags.append(object2_flag)
			del row["object2_flag"]
			
			# --------------
			# resolve_status
			#
			# only bits 1-11 defined
			for bit in int2bits(row["resolve_status"], bit=16):
				try:
					resolve_status_flag = resolve_status_flags[bit]
				except KeyError:
					try:
						resolve_status_flag = session.query(ResolveStatusFlag).filter(ResolveStatusFlag.bit == bit).one()
						resolve_status_flags[bit] = resolve_status_flag
					except sqlalchemy.orm.exc.NoResultFound:
						print("The table 'resolve_status_flag' either hasn't been loaded or the bit value '{0}' wasn't found.".format(row["object_type"]))
						sys.exit(1)
				new_obj.object2Flags.append(resolve_status_flag)
			del row["resolve_status"]
			
			# ----------
			# Columns to skip as they are already in the "field" table or redundant
			#
			for col in ["skyversion", "run", "rerun", "camcol", "nchild", "mdj", "ifield", "score"]:
				del row[col]
			
			# other clean up
			if row["balkan_id"] == -1:
				row["balkan_id"] = None
			for col in ["objc_prob_psf", "rowvdeg", "rowvdegerr", "colvdeg", "colvdegerr"]:
				if int(row[col]) == -9999:
					row[col] = None
					
			# handle exceptions - names that are different between the FITS file and database
				# none
		
			for column in photoObjFile.column_names: #row.keys():
				if debug:
					if not hasattr(new_obj, column):
						print("mismatched column name: {0}".format(column))
			
				#print("{2} {0} : {1}".format(row[column], type(row[column]), column))
			
				setattr(new_obj, column, row[column])
	
	#session.commit()
	
	# just read one file for now
	print("Exiting reading just one file.")
	sys.exit(1)






















