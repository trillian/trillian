#!/usr/bin/env python

from abc import ABCMeta

class Dataset(metaclass=ABCMeta):
	
	#@abstractmethod
	
	#@property
	#@abstractmethod <- always the innermost

	@abstractmethod
	def populate(self, trixel=None):
		pass


