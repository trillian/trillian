#!/usr/bin/env python

import sys
import csv
import argparse
import numpy as np

import fitsio

parser = argparse.ArgumentParser(description="Generate a template for a database table from FITS table(s).")

# TODO: update to not require the "-f" flag
parser.add_argument("-f", "--file",
					help="FITS file (accepts .gz, .Z, .zip, .bz2 compressed files)",
					required=True)
parser.add_argument("-n", "--hdu-num",
					help="HDU number (1-based), first table found if not specified",
					type=int)
parser.add_argument("-t", "--trim-strings",
					help="trim leading and trailing whitespace from strings",
					action="store_true")
#parser.add_argument("-p", "--pgtable",
#					help="format output for a PostgreSQL 'COPY' command with this table name")
parser.add_argument("-d", "--delimiter",
					help="column delimiter to use for output",
					choices=['tab', 'space', 'pipe', 'comma'],
					default='comma')
parser.add_argument("--header",
					help="print header of column names",
					action="store_true")

# print help if no args specified
if len(sys.argv) == 1:
	print("\n")
	parser.print_help()
	print("\n")
	sys.exit(1)	

args = parser.parse_args()

# if HDU number not specified, find the first table HDU
if args.hdu_num is None:
	with fitsio.FITS(args.file) as fits_file:
		for hdu in fits_file:
			if hdu.get_exttype() in ('BINARY_TBL', 'ASCII_TBL'):
				hdu_num = hdu.get_info()["hdunum"]
				break
	if hdu_num is None:
		raise Exception("No table HDU found in file '{0}'".format(fits_file))
else:
	hdu_num = args.hdu_num

delimiter = {"tab":"\t", "comma":",", "space":" ", "pipe":"|"}[args.delimiter]
	
with fitsio.FITS(args.file, iter_row_buffer=2000) as fits_file:

	# read specified HDU
	hdu = fits_file[hdu_num-1] # HDU numbers are 1-based

#	if args.pgtable:
#		if args.header:
#			header = ", HEADER"
#		else:
#			header = ""
#		print("COPY {0} FROM stdin WITH (FORMAT 'csv'{1}".format(args.pgtable, header))
	
	#writer = csv.writer(sys.stdout)

	if args.header:
		# get column names
		print(delimiter.join(hdu.get_colnames()))
	
	for row in hdu:
		# "row" is an numpy.ndarray
		#writer.writerows(
		values = [x.decode('utf-8').strip() if type(x)==np.bytes_ else str(x) for x in row]
		
		print(delimiter.join(values))


