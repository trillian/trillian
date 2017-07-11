
import os.path

import fitsio
#from astropy.io import fits

class PhotoRunAll(object):

	def __init__(self, filepath=None):

		if not os.path.isfile(filepath):
			raise Exception("Could not create PhotoRunAll object; file not found ('{0}').".format(filepath))
		
		self._columnNames = None
		self.hdu_list = fitsio.FITS(filepath, iter_row_buffer=1000)
		self.dataHDU = self.hdu_list[1]
		self.nrows = self.dataHDU.get_nrows()
	
	@property
	def columnNames(self):
		if self._column_names == None:
			row1 = self.dataHDU.read(rows=[0,0])
			self._column_names = [x.name.lower() for x in self.dataHDU.columns]
		return self._column_names