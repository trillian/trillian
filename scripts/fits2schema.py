#!/usr/bin/env python

'''
This script takes every table header in a FITS file and generates a PostgreSQL schema.
(Or at least a starting point for one.)
'''

from trillian.utilities.files.fits import fits2schema

import argparse

parser = argparse.ArgumentParser(description="Generate a template for a database table from FITS table(s).")

# TODO: update to not require the "-f" flag
parser.add_argument("-f", "--file",
					help="FITS file",
					required=True,
					default=None)

args = parser.parse_args()

schema = fits2schema(fits_filepath=args.file)

for hdu_num in sorted(schema.keys()):
	print(schema[hdu_num])