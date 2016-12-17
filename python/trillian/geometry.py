#!/usr/bin/env python


def polygonFromFITS(hdu=None, header=None):
	'''
	Calculate the polygon on the sky represented by a given FITS image.
	Takes a FITS HDU or header object, either from fitsio or astropy.io.fits.
	'''
	if all([hdu, header]):
		raise Exception("Only specify an HDU or header to create a FITSChannel object.")
	
	if not any([hdu, header]):
		raise Exception("Either an hdu or header must be provided.")
	
	

	