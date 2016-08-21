#!/usr/bin/env python

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship, exc, column_property, validates
from sqlalchemy import Column, orm
#from sqlalchemy import func # for aggregate, other functions
from sqlalchemy.orm.session import Session

from ..DatabaseConnection import DatabaseConnection
from ..AstropyQuantitySQLAlchemyTypes import GigabyteType
from ..pggeometry import PGPoint, PGPolygon

dbc = DatabaseConnection()

# -----------------------------------------
# This is to hide the warning:
# /usr/local/anaconda3/lib/python3.4/site-packages/sqlalchemy/dialects/postgresql/base.py:2505: SAWarning: Did not recognize type 'point' of column 'map'
# This defines the class PGPoint for any column of type 'point'.
# -----------------------------------------
from sqlalchemy.dialects.postgresql import base as pg
pg.ischema_names['point'] = PGPoint
pg.ischema_names['polygon'] = PGPolygon
# -----------------------------------------

# ========================
# Define database classes
# ========================
#
Base = dbc.Base

class Server(Base):
	__tablename__ = 'trillian_server'
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

class Node(Base):
	__tablename__ = 'node'
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}
	
	# custom types
	available_space = Column(name='available_space', type_=GigabyteType)
	
class NodeType(Base):
	__tablename__ = 'node_type'
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

class NodeCapability(Base):
	__tablename__ = 'node_capability'
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

class NodeToCapability(Base):
	__tablename__ = 'node_to_capability'
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

class Dataset(Base):
	__tablename__ = 'dataset'
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

class DatasetRelease(Base):
	__tablename__ = 'dataset_release'
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}
	
	@staticmethod
	def objectFromString(session=None, short_name=None, add=False):
		'''
		Get the DatasetRealease object that matches the provided string.

		@param session An SQLAlchemy Session instance.
		@param short_name The short_name value of the DatasetRelease.
		@param add Boolean to indicate if a new entry should be added to the database if not found.
		@returns A DatasetRelease object that matches `commentString`, None otherwise.
		'''
		theDatasetRelease = None
		
		if short_name is None:
			raise Exception("{0}.{1} 'short_name' was not provided.".format(self.__module__, type(self).__name__))
		if session is None:
			raise Exception("{0}.{1} A session must be provided.".format(self.__module__, type(self).__name__))
		
		try:
			theDatasetRelease = session.query(DatasetRelease)\
									   .filter(DatasetRelease.short_name==short_name)\
									   .one()
		except sqlalchemy.orm.exc.NoResultFound:
			if add:
				# create it here
				# use a new session in case another running process might be doing the same
				TempSession = scoped_session(sessionmaker(bind=dbc.engine, autocommit=True))
				tempSession = TempSession()
				
				tempSession.begin()
				theDatasetRelease = DatasetRelease()
				theDatasetRelease.short_name = short_name
				tempSession.add(theDatasetRelease)
				
				try:
					tempSession.commit()
				except sqlalchemy.exc.IntegrityError:
					# since this session is in a "bubble", another process elsewhere
					# (e.g. in a multiprocessing environment) could have beat us to it.
					#
					# Likely error:
					# sqlalchemy.exc.IntegrityError: (psycopg2.IntegrityError) duplicate key value violates unique constraint "fits_header_comment_uniq"
					#
					pass # since we know the value is there, the next query should succeed.

				# now pull it out into the given session
				theDatasetRelease = session.query(DatasetRelease)\
									.filter(DatasetRelease.short_name==short_name)\
									.one()
			else:
				theDatasetRelease = None
		except sqlalchemy.orm.exc.MultipleResultsFound:
			raise Exception("Database integrity error: multiple keyword records with label '{0}' found.".format(keyword))

		return theDatasetRelease

class NodeToDatasetRelease(Base):
	__tablename__ = 'node_to_dataset_release'
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

class Trixel(Base):
	__tablename__ = 'trixel'
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

class Footprint(Base):
	__tablename__ = 'footprint'
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

#class TrillianUser(Base):
#	__tablename__ = 'trillian_user'
#	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

# =========================
# Define relationships here
# =========================
#
Server.nodes = relationship(Node, backref="server")

Node.nodeType = relationship(NodeType, backref="nodes")
Node.datasetReleases = relationship(DatasetRelease,
						 		secondary=NodeToDatasetRelease.__table__,
						 		backref="nodes")
Node.capabilities = relationship(NodeCapability,
							 secondary=NodeToCapability.__table__,
							 backref="nodes")
Node.trixels = relationship(Trixel, backref="node")

Trixel.children = relationship(Trixel)
Trixel.parent = relationship(Trixel)

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


