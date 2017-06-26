
import os.path

import fitsio
import numpy as np

class SPPlate(object):
	
	def __init__(self, filepath=None):
		
		if not os.path.isfile(filepath):
			raise Exception("Could not create SPPlate object; file not found ('{0}').".format(filepath))
	
		self.filepath = filepath
		self._headers = dict()
		self._number_of_headers = None
		self._fiber_count = None
		
		# Image HDUs
		self._flux_image = None
		self._inverse_variance_image = None
		self._and_mask_image = None
		self._or_mask_image = None
		self._wavelength_dispersion_image = None
		self._sky_flux_image = None
		
		# hardcoded for the moment
		self.spAll_filepath = "/Users/demitri/Documents/Data/SDSS/v5_10_0/spAll-v5_10_0.fits"
	
	@property
	self fiber_count(self):
		'''
		Returns the number of fibers in this file.
		
		@rtype: int
		@returns: The number of fibers in this file.
		'''
		if self._fiber_count is None:
			self._fiber_count = self.header(1)["NAXIS2"]
		return self._fiber_count
			
	@property
	def number_of_headers(self):
		if self._number_of_headers is None:
			self._number_of_headers = len(fitsio.FITS(self.filepath))
		return self._number_of_headers

	def header(self, hdu=None):
		''' Returns the header for the given HDU (1-based). '''
		
		assert (hdu is not None), "An hdu value must be specified to select a header."
		
		# check valid range
		if hdu == 0:
			raise Exception("Invalid HDU - HDU numbers start with '1'.")
		elif hdu > self.number_of_headers:
			raise Exception("Tried to access hdu '{0}' when there are only {1} in this file.".format(hdu, self.number_of_headers))
			
		try:
			return self._headers[hdu]
		except KeyError:
			self._headers[hdu] = fitsio.read_header(filename=self.filepath, ext=hdu-1)
		return self._headers[hdu]
	
	def
	
	@property
	def reduction_2d_version(self):
		''' Spectro-2D reduction name. '''
		#header = fitsio.read_header(filename=self.filepath, ext=0)
		#return header["RUN2D"].strip()
		return self.header(hdu=1)["RUN2D"].strip()
	
	@property
	def wavelength_array(self):
		'''
		Returns the wavelength array in Ångstroms.
		
		λi = 10**(c0 + c1 * xi)
		
		where xi is the index i of the data grid.
		
		@rtype: numpy.array
		@returns: A list of wavelength values in Ångstroms for this plate's spectra reduction.
		
		'''
		naxis1 = self.header(hdu=1)["NAXIS1"] # length of spectrum
		coeff0 = self.header(hdu=1)["COEFF0"]
		coeff1 = self.header(hdu=1)["COEFF1"]
		
		wavelengths = np.array([(coeff0 + coeff1 * i) for i in range(naxis1)])
		return 10**wavelengths
	
	def fiber_value_is_valid(self, fiber=None):
		'''
		Checks that a fiber number is valid and in the correct range for this file.

		@type: fiber: int
		@param: fiber: fiber ID
		@rtype: bool
		@returns: True if the fiber ID is valid for this file.
		'''
		return fiber is not None and isinstance(fiber, int) and (1 <= fiber <= self.fiber_count)
	
	def flux(self, fiber=None):
		'''
		Returns the flux for a given fiber ID (1-based).
		
		This code assumes that scripts will iterate over fibers,
		so lazy loads the entire HDU at once.
		
		@type: fiber: int
		@param: fiber: fiber ID
		@rtype: numpy.array
		@returns: A array of flux values for the specified fiber.
		'''
		if self.fiber_value_is_valid(fiber) == False:
			raise Exception("An invalid fiber value was given.")
		
		if self._flux_image is None:
			with FITS(self.filepath) as hduList:
				self._flux_image = hduList[0].read()
		else:
			return self._flux_image[fiber-1]
	
	def inverse_variance(self, fiber=None)
		'''
		Returns the inverse variance for a given fiber ID (1-based).
		
		This code assumes that scripts will iterate over fibers,
		so lazy loads the entire HDU at once.
		
		@type: fiber: int
		@param: fiber: fiber ID
		@rtype: numpy.array
		@returns: A array of inverse variance values for the specified fiber.
		'''
		if self.fiber_value_is_valid(fiber) == False:
			raise Exception("An invalid fiber value was given.")
		
		if self._inverse_variance_image is None:
			with FITS(self.filepath) as hduList:
				self._inverse_variance_image = hduList[1].read()
		else:
			return self._inverse_variance_image[fiber-1]

	def and_mask(self, fiber=None)
		'''
		Returns the AND mask for a given fiber ID (1-based).
		
		This code assumes that scripts will iterate over fibers,
		so lazy loads the entire HDU at once.
		
		@type: fiber: int
		@param: fiber: fiber ID
		@rtype: numpy.array
		@returns: A array of AND mask values for the specified fiber.
		'''
		if self.fiber_value_is_valid(fiber) == False:
			raise Exception("An invalid fiber value was given.")
		
		if self._and_mask_image is None:
			with FITS(self.filepath) as hduList:
				self._and_mask_image = hduList[2].read()
		else:
			return self._and_mask_image[fiber-1]


	def or_mask(self, fiber=None)
		'''
		Returns the OR mask for a given fiber ID (1-based).
		
		This code assumes that scripts will iterate over fibers,
		so lazy loads the entire HDU at once.
		
		@type: fiber: int
		@param: fiber: fiber ID
		@rtype: numpy.array
		@returns: A array of OR mask values for the specified fiber.
		'''
		if self.fiber_value_is_valid(fiber) == False:
			raise Exception("An invalid fiber value was given.")
		
		if self._or_mask_image is None:
			with FITS(self.filepath) as hduList:
				self._or_mask_image = hduList[3].read()
		else:
			return self._or_mask_image[fiber-1]
	
	def wavelength_dispersion(self, fiber=None)
		'''
		Returns the wavelength dispersion for a given fiber ID (1-based).
		
		This code assumes that scripts will iterate over fibers,
		so lazy loads the entire HDU at once.
		
		@type: fiber: int
		@param: fiber: fiber ID
		@rtype: numpy.array
		@returns: A array of wavelength dispersion values for the specified fiber.
		'''
		if self.fiber_value_is_valid(fiber) == False:
			raise Exception("An invalid fiber value was given.")
		
		if self._wavelength_dispersion_image is None:
			with FITS(self.filepath) as hduList:
				self._wavelength_dispersion_image = hduList[4].read()
		else:
			return self._wavelength_dispersion_image[fiber-1]

	def sky_flux_image(self, fiber=None)
		'''
		Returns the sky flux for a given fiber ID (1-based).
		
		This code assumes that scripts will iterate over fibers,
		so lazy loads the entire HDU at once.
		
		@rtype: numpy.array
		@returns: A array of sky flux values for the specified fiber.
		'''
		if self.fiber_value_is_valid(fiber) == False:
			raise Exception("An invalid fiber value was given.")
		
		if self._sky_flux_image is None:
			with FITS(self.filepath) as hduList:
				self._sky_flux_image = hduList[6].read()
		else:
			return self._sky_flux_image[fiber-1]

	def spAll(self, fiber=None):
		'''
		Returns a dictionary containing the spAll values for the given fiber.
		
		@type: fiber: int
		@param: fiber: fiber ID
		@rtype: dictionary
		@returns: Dictionary of spAll values for the specified fiber.
		'''
		if self.fiber_value_is_valid(fiber) == False:
			raise Exception("An invalid fiber value was given.")
		
		# read all values as a block
		if self._spAll is None:
			with FITS(self.filepath) as hduList:
				self._spAll = hduList[











