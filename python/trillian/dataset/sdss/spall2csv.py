#!/usr/bin/env python

import numpy as np
from astropy.io import fits

def spall2csv(filepath=None, delimiter="|", hdunum=None):
	
	hduList = fits.open(name=filepath, memmap=True)
	hdu = hduList[hdunum-1]
	spall_table = hdu.data.view(np.recarray) # use when reading row by row
	
	# get column names as a list
	column_names = hdu.columns.names

	# open output file
	output_filename = filepath+".out"
	output_file = open(output_filename, 'w')
	
	# print header
	print(delimiter.join(column_names), file=output_file)

	nrows = len(spall_table)
	for i in range(nrows):
		row = spall_table[i] # -> astropy.io.fits.fitsrec.FITS_record
		
		values = list()
		
		# read each column value in this row, add to a list
		for col in column_names:
			value = row[col]
			if isinstance(value, np.ndarray):
				# convert arrays to PostgreSQL array format
				# only up to 2D shapes supported here
				if len(value.shape) == 1:
					value = "{{{0}}}".format(",".join([str(x) for x in value.tolist()]))
				else:
					rows = list()
					for i in range(value.shape[0]):
						rows.append("{{{0}}}".format(",".join([str(x) for x in value[i].tolist()])))
					value = "{{{0}}}".format(",".join(rows))
					
			elif isinstance(value, str):
				# string values must be quoted for database import
				if len(value) > 0:
					value = "'{0}'".format(value.strip()) #"'{0}'".format(value.decode("utf-8").strip())
			elif isinstance(value, bytes):
				if len(value) > 0:
					value = "'{0}'".format(value.decode('utf-8').strip())
			else:
				# rest are numeric, convert to string
				#print(type(value))
				value = str(value)
			values.append(value)

		# print row
		print(delimiter.join(values), file=output_file)
		
	output_file.close()	

def columns2sql_table(columns=None, table_name='tablename'):
	'''
	Convert a list of astropy.io.fits.column.ColDefs into a PostgreSQL table definition.
	'''
	fields = list()
	
	for column in columns:
		type_name = column.dtype.name
		if type_name.startswith('bytes'):
			table_def.append('{0} {1}'.format(column.name, 'text'))
		elif type_name.dtype.name.startswith('float'):
			table_def.append('{0} {1}'.format(column.name, 'numeric'))
		elif type_name.dtype == 'int32':
			table_def.append('{0} {1}'.format(column.name, 'integer'))
		elif type_name.dtype == 'int64':
			table_def.append('{0} {1}'.format(column.name, 'bigint'))
		elif type_name.dtype == 'uint8':
			table_def.append('{0} {1}'.format(column.name, 'smallint'))

	table_def = "CREATE TABLE {0} (".format(table_name) + \
				",\r    ".join(fields) + \
				");"
				
	return table_def

spall2csv(filepath="spAll-v5_10_0.fits", hdunum=2)
