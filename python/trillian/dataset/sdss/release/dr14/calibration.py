
from scipy.integrate import simps

from ....calibration import Calibration

class SDSS_DR14_Calibration(Calibration):
	
	def __init__(self):
		pass
	
	def psf(self):
		pass
	
	def bandpass(self):
		'''
		Dictionary of filters, key = filter name.
		'''
		bandpass = dict()
		#bandpass["u"] = ...
		#bandpass["g"] = ...
		#bandpass["r"] = ...
		#bandpass["i"] = ...
		#bandpass["z"] = ...
		
		return bandpass
	
	def zero_point(self):
		'''
		Dictionary of zero point values (float), accessed by filter name.
		'''
		pass
	
	