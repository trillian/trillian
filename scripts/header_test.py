#!/usr/bin/env python

'''
This script reads headers from FITS image files from the Trillian database and calcualtes the polygon they cover on the sky.
'''

import sys
import sqlalchemy

from trillian.database.connections import LocalhostConnection as db
from trillian.database.trilliandb.FileModelClasses import *

#parser = argparse.ArgumentParser(description="program description")

# Set up session
session = db.Session()

key = "SIMPLE"
print(FitsHeaderKeyword.objectFromString(session=session, keywordString=key))
print(FitsHeaderKeyword.objectFromString(session=session, keywordString=key))

theKeyword = session.query(FitsHeaderKeyword)\
								.filter(FitsHeaderKeyword.label==key)\
								.one()
print(theKeyword)
								
test_file = session.query(FitsFile).filter(FitsFile.filename=='frame-g-003959-1-0011.fits.bz2').one()

for hdu in test_file.hdus:
	for value in hdu.headerValues:
		print(value)
	print("")



#session.commit()
db.engine.dispose()
sys.exit(0)