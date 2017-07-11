#!/usr/bin/python

import sys
from decimal import *

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship, backref, exc, column_property
from sqlalchemy import orm
from sqlalchemy.orm.session import Session
from sqlalchemy import String
from sqlalchemy import func

Base = db.Base

class Object(Base):
    __tablename__ = 'object'
    __table_args__ = {'autoload': True, 'schema': 'dataset_sdss_dr12'}

	objectTypes = relationship('ObjectType', backref="objects")
	things = relationship('Thing', backref="objects")
	object1Flags = relationship('Object1Flag', backref="objects")
	object2Flags = relationship('Object2Flag', backref="objects")
	fields = relationship("Field", backref="objects")
	resolveStatus = relationship("ResolveStatus", backref="objects")

	#def __repr__(self):
	#    return '<Exposure_Status (pk={0}, label={1})>'.format(
	#        self.pk, self.label)

class Field(Base):
    __tablename__ = 'field'
    __table_args__ = {'autoload': True, 'schema': 'dataset_sdss_dr12'}

class ObjectTypeFlag(Base):
    __tablename__ = 'object_type_flag'
    __table_args__ = {'autoload': True, 'schema': 'dataset_sdss_dr12'}

class ObjectToObjectTypeFlag(Base):
    __tablename__ = 'object_to_type_flag'
    __table_args__ = {'autoload': True, 'schema': 'dataset_sdss_dr12'}

class Thing(Base):
    __tablename__ = 'thing'
    __table_args__ = {'autoload': True, 'schema': 'dataset_sdss_dr12'}

class ThingToObject(Base):
    __tablename__ = 'object_type_flag'
    __table_args__ = {'autoload': True, 'schema': 'dataset_sdss_dr12'}

class Object1Flag(Base):
    __tablename__ = 'object1_flag'
    __table_args__ = {'autoload': True, 'schema': 'dataset_sdss_dr12'}

class Object1Flag(Base):
    __tablename__ = 'object_to_object1_flag'
    __table_args__ = {'autoload': True, 'schema': 'dataset_sdss_dr12'}

class Object2Flag(Base):
    __tablename__ = 'object2_flag'
    __table_args__ = {'autoload': True, 'schema': 'dataset_sdss_dr12'}

class ObjectToObject2Flag(Base):
    __tablename__ = 'object_to_object2_flag'
    __table_args__ = {'autoload': True, 'schema': 'dataset_sdss_dr12'}

class ResolveStatus(Base):
    __tablename__ = 'resolve_status'
    __table_args__ = {'autoload': True, 'schema': 'dataset_sdss_dr12'}

class ObjectToResolveStatus(Base):
    __tablename__ = 'object_to_resolve_status'
    __table_args__ = {'autoload': True, 'schema': 'dataset_sdss_dr12'}

#---------
# Test that all relationships/mappings are self-consistent.
#---------
from sqlalchemy.orm import configure_mappers
try:
	configure_mappers()
except RuntimeError, error:
	print('''
	dataset_sdss_dr12.ModelClasses:
	An error occurred when verifying the relationships between the database tables.  
	Most likely this is an error in the definition of the SQLALchemy relationships-
	see the error message below for details.
	''')
	print('Error type: {0}'.format(sys.exc_info()[0]))
	print('Error value: {0}'.format(sys.exc_info()[1]))
	print('Error trace: {0}'.format(sys.exc_info()[2]))
	sys.exit(1)
		
