#!/usr/bin/env python

'''
Script to count the number of frame-*fits* files in each frame directory.
'''

from glob import glob
import os.path
from os.path import basename

frame_dir = "/uufs/chpc.utah.edu/common/home/sdss01/dr12/boss/photoObj/frames/301"

frames = [basename(x) for x in glob(os.path.join(frame_dir, "*"))]

for frame in frames:
	print("{0}\t{1}".format(frame, len(glob( os.path.join(frame_dir, frame, "[1-6]", "*fits*" )))


