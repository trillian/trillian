#!/usr/bin/env python

'''
ModelClasses file for schema "mast".
'''
import sqlalchemy
from sqlalchemy.orm import relationship

from ..DatabaseConnection import DatabaseConnection

dbc = DatabaseConnection()

# ========================
# Define database classes
# ========================
#
Base = dbc.Base

class CaomArtifact(Base):
	''' Table of data files. '''
	__tablename__ = 'caom_artifact'
	__table_args__ = {'autoload' : True, 'schema' : 'mast'}

class CaomChunk(Base):
	__tablename__ = 'caom_chunk'
	__table_args__ = {'autoload' : True, 'schema' : 'mast'}

class CaomMembers(Base):
	__tablename__ = 'caom_members'
	__table_args__ = {'autoload' : True, 'schema' : 'mast'}

class CaomObservation(Base):
	__tablename__ = 'caom_observation'
	__table_args__ = {'autoload' : True, 'schema' : 'mast'}

class CaomPart(Base):
	__tablename__ = 'caom_part'
	__table_args__ = {'autoload' : True, 'schema' : 'mast'}

class CaomPlane(Base):
	__tablename__ = 'caom_plane'
	__table_args__ = {'autoload' : True, 'schema' : 'mast'}

class CaomProductDescription(Base):
	__tablename__ = 'caom_product_description'
	__table_args__ = {'autoload' : True, 'schema' : 'mast'}

class MetaApertures(Base):
	__tablename__ = 'meta_apertures'
	__table_args__ = {'autoload' : True, 'schema' : 'mast'}

class MetaFilters(Base):
	__tablename__ = 'meta_filters'
	__table_args__ = {'autoload' : True, 'schema' : 'mast'}

class MetaInstruments(Base):
	__tablename__ = 'meta_instruments'
	__table_args__ = {'autoload' : True, 'schema' : 'mast'}

class MASTUCD(Base):
	__tablename__ = 'ucd'
	__table_args__ = {'autoload' : True, 'schema' : 'mast'}

# =========================
# Define relationships here
# =========================
#
CaomArtifact.plane = relationship(CaomPlane, backref="artifact")

# ---------------------------------------------------------
# Test that all relations/mappings are self-consistent.
# ---------------------------------------------------------
#
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
	
