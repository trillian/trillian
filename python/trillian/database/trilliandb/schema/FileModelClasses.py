#!/usr/bin/env python

'''
ModelClasses file for schema "trilliandb.file".
'''

from ...DatabaseConnection import DatabaseConnection
from ...AstropyQuantitySQLAlchemyTypes import GigabyteType
from .TrillianModelClasses import DatasetRelease

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relation, exc, column_property, validates
from sqlalchemy import Column, orm
from sqlalchemy.orm.session import Session

dbc = DatabaseConnection()

# ========================
# Define database classes
# ========================
Base = declarative_base(bind=dbc.engine)

class FitsHeaderKeyword(Base):
	__tablename__ = 'fits_header_keyword'
	__table_args__ = {'autoload' : True, 'schema' : 'file'}

class FitsHeaderValue(Base):
	__tablename__ = 'fits_header_value'
	__table_args__ = {'autoload' : True, 'schema' : 'file'}

class FitsHeaderComment(Base):
	__tablename__ = 'fits_header_comment'
	__table_args__ = {'autoload' : True, 'schema' : 'file'}

class FitsHDU(Base):
	__tablename__ = 'fits_hdu'
	__table_args__ = {'autoload' : True, 'schema' : 'file'}

class FitsFile(Base):
	__tablename__ = 'fits_file'
	__table_args__ = {'autoload' : True, 'schema' : 'file'}

class BasePath(Base):
	__tablename__ = 'base_path'
	__table_args__ = {'autoload' : True, 'schema' : 'file'}

# =========================
# Define relations here
# =========================

FitsFile.datasetRelease = relation(DatasetRelease, backref="fitsFiles")
FitsFile.hdus = relation(FitsHDU, backref="fitsFile")
FitsFile.basePath = relation(BasePath) # no backref needed here

FitsHDU.headerValues = relation(FitsHeaderValue, backref="fitsFile")

FitsHeaderValue.keyword = relation(FitsHeaderKeyword, backref="headerValues")
FitsHeaderValue.comment = relation(FitsHeaderComment, backref="headerValues")

# ---------------------------------------------------------
# Test that all relations/mappings are self-consistent.
# ---------------------------------------------------------

from sqlalchemy.orm import configure_mappers
try:
	configure_mappers()
except RuntimeError as error:
	print("""
An error occurred when verifying the relations between the database tables.
Most likely this is an error in the definition of the SQLAlchemy relations - 
see the error message below for details.
""")
	print("Error type: %s" % sys.exc_info()[0])
	print("Error value: %s" % sys.exc_info()[1])
	print("Error trace: %s" % sys.exc_info()[2])
	sys.exit(1)
	
	



