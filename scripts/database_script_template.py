#!/usr/bin/env python

'''
This is a template for creating new scripts that access the Trillian database.
'''

import sys
import sqlalchemy

from trillian.database.connections import LocalhostConnection as db
from trillian.database.connections import RemoteTunnelConnection as db
from trillian.database.trilliandb.FileModelClasses import *
#from trillian.database.trilliandb.TrillianModelClasses import DatasetRelease

# Set up session
session = db.Session()



#session.commit()
db.engine.dispose()
sys.exit(0)
