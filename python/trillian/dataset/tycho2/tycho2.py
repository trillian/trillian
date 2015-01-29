#!/usr/bin/env python

import os

from .. import Dataset

class Tycho2(Dataset):

	def __init__(self):
		self.data_is_local = True
		self.datapath = os.path.join("/", "trillian", "datasets", "tycho2")
		

