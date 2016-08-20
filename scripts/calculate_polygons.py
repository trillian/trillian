#!/usr/bin/env python

'''
This script finds FITS files in the database and calculates their polygon on the sky,
saving the result back to the database.
'''

import sys
import argparse

import sqlalchemy
from sqlalchemy import func
import starlink.Ast as Ast
import numpy as np
from cornish.region import ASTBox, ASTPolygon
from cornish.channel import ASTFITSChannel
from cornish.mapping import ASTFrame

from trillian.database.connections import LocalhostConnection as db
from trillian.database.connections import RemoteTunnelConnection as db
from trillian.database.trilliandb.FileModelClasses import FitsHDU, FitsFile
from trillian.database.trilliandb.TrillianModelClasses import Footprint

def processFilesWithoutPolygons(count=400):
	'''
	This function goes to the database, get 'count' images that don't have polygons, and calculates them.
	'''
	db.engine.dispose() # close all connections for a multiprocessing environment
	session = db.Session()
	
	image_hdus = session.query(FitsHDU)\
						.outerjoin(Footprint)\
						.join(FitsFile)\
						.filter(Footprint.sky_polygon==None)\
						.filter(FitsFile.filename.like('frame-g-006073-4-0063.fits%'))\
						.filter(FitsHDU.number==1)\
						.limit(count)\
						.all()

	keys = ["NAXIS", "NAXIS1", "NAXIS2", "CTYPE1", "CTYPE2", "CRPIX1", "CRPIX2", "CRVAL1", "CRVAL2", "CD1_1", "CD1_2", "CD2_1", "CD2_2"]

	for hdu in image_hdus:

# 		trimmed_header = []
# 		for card in hdu.pseudoHeader():
# 			for key in keys:
# 				if card.startswith(key):
# 					trimmed_header.append(card)
#		print(trimmed_header)

		#hd = hdu.headerDict()
		#trim_hd = dict()
		#for key in keys:
		#	if key in keys:
		#		trim_hd[key] = hd[key]
		#print(trim_hd)
		print(hdu.pseudoHeader())
		fitsChannel = ASTFITSChannel(header=hdu.pseudoHeader())

		print(fitsChannel.boundingPolygon().points)
		
#		print(np.rad2deg(fitsChannel.boundingPolygon().points))
		#raise Exception("")
		sys.exit(1)
	

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(description="A script to extract headers from FITS files.")
	parser.add_argument("-s", "--source",
					dest="source",
					help="Trillian short name identifier for this data source",
					default=None,
					required=True)

	# Print help if no arguments are provided
	#if len(sys.argv) < 2:
	#	parser.print_help()
	#	parser.exit(1)

	args = parser.parse_args()

	processFilesWithoutPolygons(count=10)
	


# Set up session
session = db.Session()



#session.commit()
db.engine.dispose()
sys.exit(0)
