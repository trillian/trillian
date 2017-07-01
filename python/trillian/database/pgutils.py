#!/usr/bin/env python

__author__ = "Demitri Muna"

'''
Utlitiy functions for working with PostgreSQL databases.
'''

from os.path import expanduser

def read_password_from_pgpass(host=None, port=None, user=None, database=None):
	'''
	Given the host, user, port, and database name, retrieve the database password from ~/.pgpass.
	'''
	port = str(port) # in case the port is provided as a number, will be compared to a string below
	
	if not all([host, port, user, database]):
		raise Exception("A host, user, port, and database name must be specified to retrieve a password from .pgpass.")
	
	line_no = 0
	with open(expanduser("~/.pgpass")) as pgpass:
		line_no = line_no + 1
		for line in pgpass:
			# skip comments	
			if line.startswith("#"):
				continue
			elif not len(line) > 2:
				continue
			else:
				line = line.rstrip("\n")
			
			try:
				(_host, _port, _database, _user, _password) = line.split(":")
				if _host in [host, '*'] and _port in [port, '*'] and _user in [user, '*'] and _database in [database, '*']:
					return _password
			except ValueError:
				raise Exception("An incorrectly formatted line was found in '~/.pgpass (line {0}).".format(line_no))
	return None