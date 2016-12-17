#!/usr/bin/env python

'''
This script scrapes the MAST database to populate the files from GALEX into the Trillian database.
'''

import sys
import sqlalchemy

from trillian.database.connections import LocalhostConnection as db
from trillian.database.connections import RemoteTunnelConnection as db
from trillian.database.trilliandb.FileModelClasses import *
from trillian.database.trilliandb.TrillianModelClasses import DatasetRelease

# Set up session
session = db.Session()

# get the dataset release
gr6 = session.query(DatasetRelease).filter(DatasetRelease.display_name=="GR6").one()
gr7 = session.query(DatasetRelease).filter(DatasetRelease.display_name=="GR7").one()



#session.commit()
db.engine.dispose()
sys.exit(0)
