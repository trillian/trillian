#!/usr/bin/python

import os
import pickle
import sqlalchemy
from sqlalchemy.schema import Table
from sqlalchemy.orm import relationship, backref
from trillian.database.DatabaseConnection import DatabaseConnection
#from sdss.internal.database.DatabaseConnection import DatabaseConnection

#import sqlalchemy.engine.reflection.Inspector as Inspector

db = DatabaseConnection()
Base = db.Base

from sqlalchemy import inspect
inspector = inspect(db.engine)

metadata_pickle_filename = "ModelClasses_sdss_dr14.pickle"

# ------------------------------------------
# Load the cached metadata if it's available
# ------------------------------------------
cache_path = os.path.join(os.path.expanduser("~"), ".sqlalchemy_cache")
cached_metadata = None
if os.path.exists(cache_path):
	try:
		with open(os.path.join(cache_path, metadata_pickle_filename), 'rb') as cache_file:
			cached_metadata = pickle.load(file=cache_file)
	except IOError:
		# cache file not found - no problem
		pass
# ------------------------------------------

# TABLE DEFINITIONS
# -----------------
class Run(Base):

	if cached_metadata:
		__table__ = cached_metadata.tables['dataset_sdss_dr14.run']
	else:
		__tablename__ = 'run'
		__table_args__ = {'autoload':True, 'schema':'dataset_sdss_dr14'}

	def __repr__(self):
		return '<Run (pk={0}, run={1})>'.format(self.pk, self.run)

class Field(Base):
	
	if cached_metadata:
		__table__ = cached_metadata.tables['dataset_sdss_dr14.field']
	else:
		__tablename__ = 'field'
		__table_args__ = {'autoload':True, 'schema':'dataset_sdss_dr14'}

	def __repr__(self):
		return '<Field (pk={0})>'.format(self.pk)
		
	run = relationship(Run, backref="fields")

class FlagType(Base):
	
	if cached_metadata:
		__table__ = cached_metadata.tables['dataset_sdss_dr14.flag_type']
	else:
		__tablename__ = 'flag_type'
		__table_args__ = {'autoload':True, 'schema':'dataset_sdss_dr14'}

	def __repr__(self):
		return '<FlagType ("{2}": pk={0}, size: int{1})>'.format(self.pk, self.data_type, self.label)

class FlagValue(Base):

	if cached_metadata:
		__table__ = cached_metadata.tables['dataset_sdss_dr14.flag_value']
	else:
		__tablename__ = 'flag_value'
		__table_args__ = {'autoload':True, 'schema':'dataset_sdss_dr14'}

	def __repr__(self):
		return '<FlagValue: type="{0}", value="{1}", bit={2} (pk={3})>'.format(self.flagType.label, self.label, self.bit, self.pk)

	flagType = relationship(FlagType, backref="values")

class FieldToFlag(Base):

	if cached_metadata:
		__table__ = cached_metadata.tables['dataset_sdss_dr14.field_to_flag']
	else:
		__tablename__ = 'field_to_flag'
		__table_args__ = {'autoload':True, 'schema':'dataset_sdss_dr14'}

	def __repr__(self):
		return '<FieldToFlag (pk={0})>'.format(self.pk)

	#flagValue = relationship(FlagValue)
	#field = relationship(Field, backref="flags")

class PhotoObjToFlag(Base):

	if cached_metadata:
		__table__ = cached_metadata.tables['dataset_sdss_dr14.photoobj_to_flag']
	else:
		__tablename__ = 'photoobj_to_flag'
		__table_args__ = {'autoload':True, 'schema':'dataset_sdss_dr14'}

	def __repr__(self):
		return '<PhotoObjToFlag (pk={0})>'.format(self.pk)

	flagValue = relationship('FlagValue', backref='photoObjToFlags')
	photoObj = relationship('PhotoObj')
	
class ObjectType(Base):

	if cached_metadata:
		__table__ = cached_metadata.tables['dataset_sdss_dr14.object_type']
	else:
		__tablename__ = 'object_type'
		__table_args__ = {'autoload':True, 'schema':'dataset_sdss_dr14'}

	def __repr__(self):
		return '<ObjectType (pk={0})>'.format(self.pk)

class Thing(Base):

	if cached_metadata:
		__table__ = cached_metadata.tables['dataset_sdss_dr14.thing']
	else:
		__tablename__ = 'thing'
		__table_args__ = {'autoload':True, 'schema':'dataset_sdss_dr14'}

	def __init__(self, id):
		self.thing_id = id

	def __repr__(self):
		return '<Thing (pk={0})>'.format(self.pk)

class PhotoObjToThing(Base):

	if cached_metadata:
		__table__ = cached_metadata.tables['dataset_sdss_dr14.photoobj_to_thing']
	else:
		__tablename__ = 'photoobj_to_thing'
		__table_args__ = {'autoload':True, 'schema':'dataset_sdss_dr14'}

	def __repr__(self):
		return '<PhotoObjToThing (pk={0})>'.format(self.pk)


class PhotoObj(Base):
	
	if cached_metadata:
		__table__ = cached_metadata.tables['dataset_sdss_dr14.photoobj']
	else:
		__tablename__ = 'photoobj'
		__table_args__ = {'autoload':True, 'schema':'dataset_sdss_dr14'}

	field = relationship('Field', backref='photoObjs')
	objectType = relationship('ObjectType', backref="photoObjs")
	#object1Flags = relationship('Object1Flag', secondary=PhotoobjToObject1Flag.__table__, backref='photoobjs')
	#object2Flags = relationship('Object2Flag', secondary=PhotoobjToObject2Flag.__table__, backref='photoobjs')
	#resolveStatusFlags = relationship('ResolveStatusFlag', secondary=PhotoobjToResolveStatusFlag.__table__, backref='photoobjs')
	things = relationship('Thing', secondary=PhotoObjToThing.__table__, backref='photoObjs')

	# use this for flags where the filter doesn't need to be set (one flag per object)
	flags = relationship('FlagValue', secondary=PhotoObjToFlag.__table__, backref='photoObjs')

	# use this for flags where the filter must be set
	photoObjToFlags = relationship('PhotoObjToFlag')

	#for col in inspector.get_columns('photoobj', schema='dataset_sdss_dr14'):
	#	if col["name"] == "pk":
	#		break

	def __repr__(self):
		return '<PhotoObj (pk={0})>'.format(self.pk)

PhotoObj.children = relationship('PhotoObj',
								 backref=backref('parent', remote_side=[PhotoObj.pk]))
	
# This is a self-join relationship.
# It must be defined outside of PhotoObj to use "PhotoObj.pk" - not sure how to access the Column after autoload
# Ref: http://docs.sqlalchemy.org/en/latest/orm/relationships.html#adjacency-list-relationships
#PhotoObj.parent = relationship('PhotoObj',
#							   remote_side=[PhotoObj.pk],
#							   backref=backref(name='children', remote_side=[PhotoObj.parent_photoobj_pk]))
#PhotoObj.children = relationship('PhotoObj',
#								 backref=backref('parent', remote_side=[PhotoObj.pk]))

#---------
# Test that all relationships/mappings are self-consistent.
#---------
from sqlalchemy.orm import configure_mappers
try:
	configure_mappers()
except RuntimeError as error:
	import inspect, os
	
	print ("{0}:".format(inspect.getfile(inspect.currentframe())) +
	"An error occurred when verifying the relationships between the database tables." +
	"Most likely this is an error in the definition of the SQLALchemy relationships-" +
	"see the error message below for details.")
	
	print('Error type: {0}'.format(sys.exc_info()[0]))
	print('Error value: {0}'.format(sys.exc_info()[1]))
	print('Error trace: {0}'.format(sys.exc_info()[2]))
	sys.exit(1)


# ----------------------------------------
# If no cached metadata was found, save it
# ----------------------------------------
if cached_metadata is None:
	# cache the metadata for future loading
	# - MUST DELETE IF THE DATABASE SCHEMA HAS CHANGED
	try:
		if not os.path.exists(cache_path):
			os.makedirs(cache_path)
		# make sure to open in binary mode - we're writing bytes, not str
		with open(os.path.join(cache_path, metadata_pickle_filename), 'wb') as cache_file:
			pickle.dump(Base.metadata, cache_file)
	except:
		# couldn't write the file for some reason
		pass

