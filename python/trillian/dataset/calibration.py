#!/usr/bin/env python

from abc import ABCMeta, abstractproperty

import numpy as np
from scipy.integrate import simps
from astropy import constants

class Calibration(object):

    __metaclass__ = ABCMeta

#	def __init__(self):
#		self.dataset = dataset
#		self.release = release
				
	@abstractproperty
	def psf(self):
		pass
		
	@abstractproperty
	def zero_point(self):
		pass

	@abstractproperty
	def bandpass(self):
		pass
		
class Bandpass(metaclass=ABCMeta):
    
	def __init__(self):
		'''
		
		:param wavelengths - Numpy array
		:param transmission - Numpy array
		'''
		self.name = None
		self.zero_point = None
		self.wavelengths = None  # Numpy array
		self.transmission = None # Numpy array

	def magnitude(self, spectrum=None):
		'''
		
		'''
		c = constants.c
		c = c.to(u.Angstrom/u.second)
		#c_AAs     = 2.99792458e18                          # Speed of light in Angstrom/s
		#lamS,spec = np.loadtxt('spectrum.dat',unpack=True) #Two columns with wavelength (in Angstrom) and flux density (in erg/s/cm2/AA)
		#lamF,filt = np.loadtxt('filter.dat'  ,unpack=True) #Two columns with wavelength and response in the range [0,1]
		#filt_int  = np.interp(lamS,lamF,filt)              #Interpolate to common wavelength axis
		
		# interpolate spectrum wavelength grid onto bandpass grid
		interpolated_spectrum = np.interp(x=self.wavelengths, xp=spectrum.wavelengths, fp=spectrum.flux)

		#fnu = a/b / c

		a = simps(y=interpolated_spectrum * self.wavelenths * self.transmission, x=self.wavelengths)
		b = simps(y=self.transmission / self.wavelengths, x = self.wavelengths) 
						
		#I1        = simps(S*T*lam,lam)                     #Denominator
		#I2        = simps(  T/lam,lam)                     #Numerator

		#fnu       = I1/I2 / c_AAs                          #Average flux density
		f_nu = a/b / c # average flux density

		#mAB       = -2.5*np.log10(fnu) - 48.6              #AB magnitude
		ab_mag = -2.5 * np.log10(f_nu) + self.zero_point # AB magnitude
		
