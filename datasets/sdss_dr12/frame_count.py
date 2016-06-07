#!/usr/bin/env python

'''
Script to count the number of frame-*fits* files in each run directory.

Lowest count: frame 3959: 420.
'''

from glob import glob
import os.path
from os.path import basename

runs_dir = "/uufs/chpc.utah.edu/common/home/sdss01/dr12/boss/photoObj/frames/301"

runs = [basename(x) for x in glob(os.path.join(frame_dir, "*"))]

for run in runs:
	print("{0}\t{1}".format(run, len(glob( os.path.join(runs_dir, run, "[1-6]", "*fits*") ))))


