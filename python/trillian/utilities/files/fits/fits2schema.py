#!/usr/bin/python

import fitsio

def fits2schema(fits_filepath=None, hdu=None, table_name=None, database="postgresql"):
	'''
	This script takes a FITS file and returns an SQL schema.
	
	A value of 'None' is returned if no table HDUs are found.
	Currently only PostgreSQL table definitions are supported.
	
	Parameters
	----------
	fits_filepath : str
		The full path anf filename to the FITS file.
	hdu : int
		The HDU number requested (1-based), 'None' for all table HDUs.
	table_name : str
		The name of the SQL table. Pass 'None' to attempt to read the HDU table name.
	database : str
		Database flavor; currently only accepts PostgreSQL.
		
	Returns
	-------
	str
		If one HDU is requested, the schema; if multiple, a dictionary of schema (key=HDU num).
	'''
	#if hdu == None:
	#	raise Exception("An HDU must be specified ('hdu=hdu').")
	
	table_hdus = list() # list of HDU objects
	
	if hdu == None:
		# read all table HDUs
		for hdu in fitsio.FITS(fits_filepath):
			if hdu.get_exttype() in ('BINARY_TBL', 'ASCII_TBL'):
				table_hdus.append(hdu)

	if len(table_hdus) == 0:
		# no table HDUs found
		return None
		
	if database.lower() not in ['postgresql']:
		print("Database type '{0}' not currently supported.".format(database))
		return

	datatypes = dict()
	datatypes["postgresql"] = {"A":"TEXT", "B":"SMALLINT", "J":"BIGINT",
							   "I":"INTEGER", "E":"NUMERIC", "D":"numeric",
							   "C":"NUMERIC[2]", "M":"NUMERIC[2]", "K":"BIGINT", "X":"BIT"}
	
	schemas = dict()
	
	for hdu in table_hdus:
		table_name = hdu.get_extname()
		hdu_num = hdu.get_info()['hdunum'] + 1
		if table_name == '':
			table_name = "HDU_{0}".format(str(hdu_num))
		
		#column_names = hdu.get_colnames()
		#column_types = hdu.get_rec_dtype()
		#column_descr = hdu.get_rec_column_descr()
		
		fields = list()
		
		hdu_info = hdu.get_info()
		column_info = hdu_info["colinfo"]
		
		for column_dict in column_info:
			tform = column_dict["tform"]
			type_letter = tform[-1] # letter
			length = tform[:-1]
			isArray = len(length) > 0
			name = column_dict["name"].lower()
			
			if database == 'postgresql':
			
				schema = "CREATE TABLE {0} (\n".format(table_name)

				if type_letter == "A":
					if len(length) == 0:
						fields.append("    {0} TEXT".format(name))
					else:
						#fields.append("    {0} varchar({1})".format(name, length))
						# TEXT = VARCHAR = VARCHAR(n) > CHAR(n),
						# see: https://stackoverflow.com/questions/4848964/postgresql-difference-between-text-and-varchar-character-varying
						fields.append("    {0} TEXT".format(name))
				elif type_letter in "IEDBJK":
					if len(length) > 0:
						if column.dim:
							dims = [int(x) for x in column.dim.lstrip("(").rstrip(")").split(",")]
							fields.append("    {0} {1}{2}".format(name, datatypes["postgresql"][type_letter], ''.join(["[{0}]".format(x) for x in dims]), column.unit))
						else:
							fields.append("    {0} {1}[{2}]".format(name, datatypes["postgresql"][type_letter], length, column.unit))
					else:
						fields.append("    {0} {1}".format(name, datatypes["postgresql"][type_letter]))
				else:
					raise Exception("Unknown type letter found: {0}".format(type_letter))
			
			schema = schema + ",\n".join(fields) + "\n)" + "\nWITH (OIDS=FALSE);"
			
			if len(table_hdus) == 0:
				return schema
			else:
				schemas[int(hdu_num)] = schema

	return schemas
