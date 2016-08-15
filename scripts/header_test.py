#!/usr/bin/env python

'''
This script reads headers from FITS image files from the Trillian database and calcualtes the polygon they cover on the sky.
'''

import sqlalchemy

from trillian.database.connections import LocalhostConnection as db
from trillian.database.trilliandb.FileModelClasses import *

parser = argparse.ArgumentParser(description="program description")

# Set up session
session = db.Session()




#session.commit()
db.engine.dispose()
sys.exit(0)