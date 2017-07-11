#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from ..DatabaseConnection import DatabaseConnection
from ..pgutils import read_password_from_pgpass

# ---------------------------------------------------------------------
# Fill in database connection information here.
# Note!! The password is parsed from the user’s .pgpass file
# 		 so the source file can be checked into public version control.
# ---------------------------------------------------------------------
db_config = {
	'user'     : 'trillian_admin',  # specify the database username
	'password' : None,     			# the database password for that user -> '' is no password, None is not specified
	'database' : 'trilliandb',		# the name of the database
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
#
if db_config["password"] is None:
	db_config["password"] = read_password_from_pgpass(host=db_config["host"], port=db_config["port"], user=db_config["user"], database=db_config["database"])

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



