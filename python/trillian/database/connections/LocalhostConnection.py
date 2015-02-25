#!/usr/bin/python

import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from ..DatabaseConnection import DatabaseConnection

# ---------------------------------------------------------------------
# Fill in database connection information here.
# Note!! The password is parsed from the user’s .pgpass file
# 		 so the source file can be checked into public version control.
# ---------------------------------------------------------------------
db_config = {
	'user'     : 'trillian_admin',  # specify the database username
	'password' : '',     			# the database password for that user
	'database' : 'trillian',		# the name of the database
	'host'     : 'localhost',		# your hostname, "localhost" if on your own machine
	'port'     : 5432				# default port is 5432
}
# ---------------------------------------------------------------------

# =====================================================================
# No need to modify anything below this line.
# =====================================================================

# Get the password (if unspecified above) from the user's .pgpass file.
# Asterisks in the .pgpass file are supported, but recommend to be more
# specific, not less.

from os.path import expanduser
line_no = 0
with open(expanduser("~/.pgpass")) as pgpass:
	line_no = line_no + 1
	for line in pgpass:
		# skip comments	
		if line.startswith("#"):
			continue
		try:
			(user, password, host, database) = line.split(":")
			if user in [user, '*'] and database in [database, '*'] and host in [host, '*'] and port in [port, '*']:
				db_config["password"] = password
		except ValueError:
			raise Exception("An incorrectly formatted line was found in '~/.pgpass (line {0}).".format(line_no))

# If password is still empty by here, that must be what the user intended.

database_connection_string = 'postgresql://{0[user]}:{0[password]}@{0[host]}:{0[port]}/{0[database]}'.format(db_config)

# This allows the file to be 'import'ed any number of times, but attempts to
# connect to the database only once.
try:
	db = DatabaseConnection() # fails if connection not yet made.
except:
	db = DatabaseConnection(database_connection_string=database_connection_string)

engine = db.engine
metadata = db.metadata
Session = scoped_session(sessionmaker(bind=engine, autocommit=True))



