#!/usr/bin/env python

__author__ = "Demitri Muna"

'''
Classes to add support for PostrgeSQL geometric data tpyes that SQLAlchemy doesn't natively support.

Example usage, e.g. at the top of a ModelClasses file:

from sqlalchemy.dialects.postgresql import base as pg
from .PGGeometry import PGPoint
pg.ischema_names['point'] = PGPoint

This will assign the PGPoint object type for all fields of type 'point'.

For illustrative purposes in the comments below, assume a column defined as:
CREATE TABLE some_table (
	pt point,
	pg polygon
);
'''
import ast
import numpy as np
import sqlalchemy.types as types

class PGPoint(types.UserDefinedType):
	'''
	Class to represent the PostgreSQL "point" datatype.
	
	Ref: https://www.postgresql.org/docs/9.5/static/datatype-geometric.html
	
	Using this datatype definition, tuples of float values can be provided
	to point columns, and tuples of float values will be returned.
	'''
	def bind_processor(self, dialect):
		'''
		Return a function that performs the conversion from the
		provided object to a form that PostgreSQL can understand.
		
		To insert a value into a 'point' field:
			INSERT INTO some_table (pt) VALUES ('1,2');
		'''
		def process(value):
			if value is None:
				return value
			items = value.split(",")
			return "{0[0]},{0[1]}".format(value.split(","))
		return process
	
	def result_processor(self, dialect, coltype):
		'''
		Return a function that converts the value that comes from the
		database to a Python object.
		'''
		def process(value):
			if value is None:
				return None
			# value from db will be a string of the form (without the quotes): '1,2'
			#point_values = value.split(",") # not sure if there will be surrounding quotes
			#return (float(point_values[0]), float(point_values[1]))
			return np.array(ast.literal_eval(value))
		return process

class PGPolygon(types.UserDefinedType):
	'''
	Class to represent PostgreSQL "polygon" datatype.
	
	Ref: https://www.postgresql.org/docs/9.5/static/datatype-geometric.html
	
	Using this datatype definition, tuples of float values can be provided
	to point columns, and tuples of float values will be returned.
	'''
	def bind_processor(self, dialect):
		'''
		Return a function that performs the conversion from the
		provided object to a form that PostgreSQL can understand.
		
		To insert a value into a 'polygon' field:
			INSERT INTO some_table (pg) VALUES ('((1,2),(3,4),(4,5))');
		'''
		def process(value):
			''' Return a string. '''
			if value is None:
				return None
			if isinstance(value, np.ndarray):
				return "%s" % str(value.tolist()).replace("[","(").replace("]",")")
			else:
				# assuming some combination of tuples/lists
				return str(value).replace("[","(").replace("]",")")
		return process
	
	def result_processor(self, dialect, coltype):
		'''
		Return a function that converts the value that comes from the
		database to a Python object.
		'''
		def process(value):
			''' Return a Python object. '''
			if value is None:
				return None
			# value from db will be a string of the form (without quotes): '((1,2),(3,4),(4,5))'
			#
			return np.array(ast.literal_eval(value))
		return process
			




