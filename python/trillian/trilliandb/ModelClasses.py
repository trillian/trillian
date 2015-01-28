#!/usr/bin/env python

from DatabaseConnection import DatabaseConnection
from AstropyQuantitySQLAlchemyTypes import GigabyteType

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relation, exc, column_property, validates
from sqlalchemy import orm
from sqlalchemy.orm.session import Session

dbc = DatabaseConnection()

# ========================
# Define database classes
# ========================
Base = declarative_base(bind=dbc.engine)

class Server(Base):	
	__tablename__ = 'server'
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
	__tablename__ = 'node_capability
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

class NodeToCapability(Base):
	__tablename__ = 'node_to_capability
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

class Dataset(Base):	
	__tablename__ = 'dataset'
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

class NodeToDataset(Base):	
	__tablename__ = 'node_to_dataset'
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

class Trixel(Base):	
	__tablename__ = 'trixel'
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

class User(Base):	
	__tablename__ = 'user'
	__table_args__ = {'autoload' : True, 'schema' : 'trillian'}

# =========================
# Define relations here
# =========================

Server.nodes = relation(Node, backref="server")

Node.type = relation(NodeType, backref="nodes")
Node.datasets = relation(Dataset,
						 secondary=NodeToDataset.__table__,
						 backref="nodes")
Node.capabilities = relation(NodeCapability,
							 secondary=NodeToCapability.__table__,
							 backref="nodes")
Node.trixels = relation(Trixel, backref="node")

Trixel.children = relation(Trixel, backref="parent")

# ---------------------------------------------------------
# Test that all relations/mappings are self-consistent.
# ---------------------------------------------------------

from sqlalchemy.orm import configure_mappers
try:
	configure_mappers()
except RuntimeError, error:
	print """
An error occurred when verifying the relations between the database tables.
Most likely this is an error in the definition of the SQLAlchemy relations - 
see the error message below for details.
"""
	print "Error type: %s" % sys.exc_info()[0]
	print "Error value: %s" % sys.exc_info()[1]
	print "Error trace: %s" % sys.exc_info()[2]
	sys.exit(1)
	
	



