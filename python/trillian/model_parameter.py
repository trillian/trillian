

class ModelParameter(object):
	
	def __init__(self, name=None):
		
		self.name = name
		self.isContinuous = True
		self.isCyclic = False
		self.min = -float("inf")
		self.max = float("inf")
		self.prior = None
		self.unit = None
		self.initialValue = None