#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class Dataset(metaclass=ABCMeta):
	
	#@abstractmethod
	
	#@property
	#@abstractmethod <- always the innermost

	@abstractmethod
	def populate(self, trixel=None):
		pass

	@property
	def data_is_local(self):
		return self.data_is_local	

	def filter(self):
		# returns an instance of FilterTransmission
		pass
	
	def psfModel(self, ra, dec, **kwargs):
		# function that draws image in some place in survey
		pass
	
	
	