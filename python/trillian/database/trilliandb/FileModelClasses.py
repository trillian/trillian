#!/usr/bin/env python

'''
ModelClasses file for schema "file".
'''

from ..DatabaseConnection import DatabaseConnection
from ..AstropyQuantitySQLAlchemyTypes import GigabyteType
from .TrillianModelClasses import DatasetRelease

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship, exc, column_property, validates
from sqlalchemy import Column, Integer, ForeignKey, orm
from sqlalchemy.orm.session import Session

dbc = DatabaseConnection()

# ========================
# Define database classes
# ========================
#
Base = dbc.Base

class FitsHeaderKeyword(Base):
	__tablename__ = 'fits_header_keyword'
	__table_args__ = {'autoload' : True, 'schema' : 'files'}
	
	def __repr__(self):
		return "<{0}.{1} object at {2}: '{3}'>".format(self.__module__, type(self).__name__, hex(id(self)), self.label)

class FitsHeaderValue(Base):
	__tablename__ = 'fits_header_value'
	__table_args__ = {'autoload' : True, 'schema' : 'files'}

class FitsHeaderComment(Base):
	__tablename__ = 'fits_header_comment'
	__table_args__ = {'autoload' : True, 'schema' : 'files'}

class FitsHDU(Base):
	__tablename__ = 'fits_hdu'
	__table_args__ = {'autoload' : True, 'schema' : 'files'}

class FitsFile(Base):
	__tablename__ = 'fits_file'
	__table_args__ = {'autoload' : True, 'schema' : 'files'}
#	dataset_release_pk = Column(Integer, ForeignKey('trillian.dataset_release.pk'))

class BasePath(Base):
	__tablename__ = 'base_path'
	__table_args__ = {'autoload' : True, 'schema' : 'files'}

class FileKind(Base):
	__tablename__ = "file_kind"
	__table_args__ = {'autoload' : True, 'schema' : 'files'}

# =========================
# Define relationships here
# =========================
#
FitsFile.datasetRelease = relationship(DatasetRelease, backref="fitsFiles")

FitsFile.hdus = relationship(FitsHDU, backref="fitsFile")
FitsFile.basePath = relationship(BasePath) # no backref needed here
FitsFile.fileKind = relationship(FileKind, backref="fitsFiles")

FitsHDU.headerValues = relationship(FitsHeaderValue, backref="hdu")

FitsHeaderValue.keyword = relationship(FitsHeaderKeyword, backref="headerValues")
FitsHeaderValue.comment = relationship(FitsHeaderComment, backref="headerValues")

# ---------------------------------------------------------
# Test that all relations/mappings are self-consistent.
# ---------------------------------------------------------
#
from sqlalchemy.orm import configure_mappers
try:
	configure_mappers()
#	raise Exception("")
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
	
	



