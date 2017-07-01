#!/usr/bin/env python

'''
This script loads the specified photoRunAll-*.fits file into the SDSS dataset schema.
This is effectively a stand-alone table and should be run before loading photoField-*.fits files.
'''

import sys
import fitsio
import socket
import argparse
from subprocess import Popen, PIPE, STDOUT

import sqlalchemy
import numpy as np

# Get the database connection based on where we're running this script.
hostname = socket.gethostname()
if socket == "ast-trillian":
	from trillian.database.connections.LocalhostConnection import db, db_config
else:
	from trillian.database.connections.RemoteTunnelConnection import db, db_config
	
from trillian.database.datasets.sdss_dr14.ModelClasses import Run
from trillian.dataset.sdss.files import PhotoRunAll

debug = True # turn this on while debugging or in development

parser = argparse.ArgumentParser(description="Script to load photoRun FITS files into a database.",
								 usage="photoRun2db.py -d data_directory_path")

# plateruns
parser.add_argument("-f", "--file", default=None, help="path to the photoRunAll file", required=True)
#parser.add_argument("-c", "--database-connection-string", default=None, help="database connection string", required=True)
#parser.add_argument("-v", "--verbose", action="store_true", help="display progress messages", required=False)

args = parser.parse_args()

# database connection
session = db.Session()

photoRunAll = PhotoRunAll(filepath=args.file)
tablename = "{0}.{1}".format(Run.__table__.schema, Run.__table__.name)
delimiter = "|"


use_cursor_method = False
use_pipe_method = True

if False:
	pass
	#import psycopg2
# 	import os
# 	import threading
# 	
# 	write_fd = os.pipe()
# 	
# 	connection = db.engine.raw_connection() # psycopg2 connection
# 	
# 	def copy_from():
# 		
# 	
# 	to_thread = threading.Thread(target=copy_from)
# 	to_thread.start()
# 	
# 	
# 	to_thread.join()
# 
elif use_cursor_method:

	columns = ['skyversion', 'run', 'rerun', 'mjd', 'datestring', 'stripe',
			   'strip', 'xbore', 'field_ref', 'lastfield', 'flavor', 'xbin',
			   'ybin', 'nrow', 'mjd_ref', 'mu_ref', 'linestart', 'tracking',
			   'node', 'incl', 'comments', 'qterm', 'maxmuresid', 'maxnuresid',
			   'startfield', 'endfield', 'photo_version', 'dervish_version',
			   'astrom_version', 'sas_version']
	columns = [x.upper() for x in columns]
	
	from io import StringIO
	
	session.begin()
	
	connection = session.connection().connection
	cursor = connection.cursor() # -> psycopg2 cursor, created in the context of the open session
	print(cursor)
	copy_command = "COPY {0} FROM STDIN WITH (FORMAT 'csv', HEADER, DELIMITER '{1}', NULL '')".format(tablename, delimiter)

	data_stream = StringIO()

	# print header line
	#data_stream.write(delimiter.join(columns))
	
	for row in photoRunAll.dataHDU:
		values = list()
		for column in columns:
			try:
				# note that string values are returned as bytes
				value = row[column]
				if type(value) == np.bytes_:
					values.append("'{0}'".format(value.strip().decode("utf-8")))
				else:
					values.append(value)
			except ValueError as e:
				print (e)
				print(photoRunAll.dataHDU.get_colnames())
				raise Exception("Column name not found.")

		data = delimiter.join([str(x) for x in values])
		#print(data)
		data_stream.write(data)

	#cursor.copy_expert(sql=copy_command, file=data_stream)
	cursor.copy_from(file=data_stream, table=tablename, sep=delimiter, null='', columns=columns)
	connection.commit()
	session.commit()

elif use_pipe_method:
	
	columns = ['skyversion', 'run', 'rerun', 'mjd', 'datestring', 'stripe',
			   'strip', 'xbore', 'field_ref', 'lastfield', 'flavor', 'xbin',
			   'ybin', 'nrow', 'mjd_ref', 'mu_ref', 'linestart', 'tracking',
			   'node', 'incl', 'comments', 'qterm', 'maxmuresid', 'maxnuresid',
			   'startfield', 'endfield', 'photo_version', 'dervish_version',
			   'astrom_version', 'sas_version']
	columns = [x.upper() for x in columns]
	
	
	# open a pipe to psql
	#
	psql_args = ['psql']
	psql_args.extend(['-h', '{0}'.format(db_config["host"])])
	psql_args.extend(['-U', '{0}'.format(db_config["user"])])
	psql_args.extend(['-p', '{0}'.format(db_config["port"])])
	psql_args.extend([db_config["database"]])
	#psql_args.append('--set=ON_ERROR_STOP=true')
	#psql_args.append('--quiet')
	#psql_args.extend(['-c', '''"COPY {0} FROM STDIN WITH (FORMAT 'csv', HEADER, DELIMITER '{2}', NULL '')" '''.format(tablename, ",".join(columns), delimiter)])
	
	#print("Command: ", " ".join(psql_args))
	
	with Popen(args=psql_args, stdout=PIPE, stdin=PIPE, stderr=PIPE) as psql:
		
		# send COPY command
		copy_command = "COPY {0} ".format(tablename) # FROM STDIN WITH (FORMAT 'csv', HEADER, DELIMITER '{2}', NULL '');\n'''.format(tablename, ",".join(columns), delimiter)
		copy_command = copy_command + "({0})".format(",".join(columns))
		copy_command = copy_command + " FROM STDIN WITH (FORMAT 'csv', DELIMITER '{0}', NULL '');\n".format(delimiter)
		print(copy_command)
		psql.stdin.write(copy_command.encode())
		
		# print header line
		#header_line = delimiter.join(columns)
		#print(header_line)
		#psql.stdin.write(header_line.encode())
	
		for row in photoRunAll.dataHDU[0:3]:
			values = list()
			for column in columns:
				try:
					# note that string values are returned as bytes
					value = row[column]
					if column == 'RERUN':
						value = int(value)
					if type(value) == np.bytes_:
						values.append("'{0}'".format(value.strip().decode("utf-8")))
					else:
						values.append(value)
				except ValueError as e:
					print (e)
					print(photoRunAll.dataHDU.get_colnames())
					raise Exception("Column name not found.")

			data = delimiter.join([str(x) for x in values]) + "\n"
			print(data)
			psql.stdin.write(data.encode()) # expecting bytes

		print(psql.stdin)

		# read output
		#print (psql.stdout.read().decode("utf-8"))
		#print (psql.stderr.read().decode("utf-8"))
		out, err = psql.communicate() # no further writes to stdin allowed after this
		print("Out: ", out.decode('utf-8'))
		print("Err: ", err.decode('utf-8'))

else:
	for row in photoRunAll.dataHDU:
		print(row)
		raise Exception("Not implemented.")

