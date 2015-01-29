#!/usr/bin/env python

''' THIS CODE IS INCOMPLETE!!! '''

import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session

from DatabaseConnection import DatabaseConnection

class PostgreSQLConnection(object):
	'''
	
	'''
	def __init__(self, db_config=None):
		
		if db_config is None:
			raise Exception("The db_config parameter must be specified.")
		elif not isinstance(db_config, dict):
			raise TypeError("The db_config parameter must a dictionary of "
							"key/value paris describing the database connection.")
		