
import os.path

#import fitsio
from astropy.io import fits

class SPAll(object):

	def __init__(self, filepath=None):

		if not os.path.isfile(filepath):
			raise Exception("Could not create SPPlate object; file not found ('{0}').".format(filepath))

	def reduction_2d_version(self):
		pass
		
	def fibers(self, fibers=None, columns=None):
		'''
		Returns an array of dictionaries for the specified objects.
		
		@type: fibers: list
		@param: fibers: a list of fibers
		@type: columns: list
		@param: columns: a list of column names to be read (excluding all others)
		@rtype: list
		@returns: A list of dictionaries for the specified fibers.
		'''
		if columns is None:
			rows = fitsio.read(self.filepath, rows=fibers, ext=1)
		else:
			rows = fitsio.read(self.filepath, rows=fibers, columns=columns, ext=1)

	def all_plate_ids(self):
		'''
		Returns a list of all plate IDs.
		
		@rtype: list
		@returns: A list containing all plate IDs in this file.
		'''
		return fitsio.read(self.filepath, columns=['PLATE'], ext=1)

	