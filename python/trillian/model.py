
import ModelParameter

class Model(TrillianModel):
	
	def __init__(self):
		self.parameters = list() # list of ModelParameter objects
	
	def specific_intensity(x=None, y=None, wavelength=None):
		
		# x - astropy.Quantity array of x positions
		# y - astropy.Quantity array of y positions
		
		
		# returns either
		# 	* one image for all wavelengths
		#	* one image for each wavelength
		
	def isMultiwavelength(self):
		
		# True if the specific_intensity method
		# returns one image for each wavelength,
		# False if one image is returned for any given wavelength

		return True
		