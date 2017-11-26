#!/usr/bin/env python

'''
This script scrapes the MAST database to populate the files from GALEX into the Trillian database.
It only selects FITS files (caom_artifact.contenttype="FITS").
'''

import sys
import os.path
import sqlalchemy

from trillian.database.connections import LocalhostConnection as db
#from trillian.database.connections import RemoteTunnelConnection as db
from trillian.database.trilliandb.FileModelClasses import FitsFile, DirectoryPath, DirectoryPathType
from trillian.database.trilliandb.MASTModelClasses import CaomArtifact
from trillian.database.trilliandb.TrillianModelClasses import DatasetRelease

# Set up session
session = db.Session(autoflush=False)

# get the dataset releases
gr6 = session.query(DatasetRelease).filter(DatasetRelease.display_name=="GR6").one()
gr7 = session.query(DatasetRelease).filter(DatasetRelease.display_name=="GR7").one()

# get directory path types
relative_path_type = session.query(DirectoryPathType).filter(DirectoryPathType.label=='relative path').one()
base_path_type = session.query(DirectoryPathType).filter(DirectoryPathType.label=='base path').one()

def process_gr6():
	session.begin()

	directory_paths = dict()

	gr6_files = session.query(CaomArtifact).filter(CaomArtifact.datauri.like('%/GR6/%'))\
										   .filter(CaomArtifact.contenttype=="FITS")\
										   .all()

	for gr6_file in gr6_files:
		new_file = FitsFile()
		new_file.datasetRelease = gr6
		new_file.filename = gr6_file.productfilename
		new_file.uncompressed_size = gr6_file.contentlength

		session.add(new_file)
	
		# Extract relative path - example file.datauri:
		#   http://galex.stsci.edu/data/GR6/pipe/02-vsn/50089-AIS_89/d/00-visits/0002-img/07-try/AIS_89_0002_sg18-nd-int.fits.gz
		#
		path = os.path.dirname(gr6_file.datauri.split("/pipe")[1]) # all files have prefix 'GR6/pipe'

		if path in directory_paths:
			dir_path = directory_paths[path]
		else:
			try:
				session.query(DirectoryPath).filter(DirectoryPath.path==path).one()
			except sqlalchemy.orm.exc.NoResultFound:
				dir_path = DirectoryPath()
				dir_path.path = path
				dir_path.pathType = relative_path_type
				session.add(dir_path)
				session.flush()
				
				directory_paths[path] = dir_path
	
		new_file.directoryPaths.append(dir_path)

	session.commit()

# ===================================================================

def process_gr7():

	session.begin()
	directory_paths = dict()

	gr7_files = session.query(CaomArtifact).filter(CaomArtifact.datauri.like('%/GR7/%'))\
										   .filter(CaomArtifact.contenttype=="FITS")\
										   .all()

	for gr7_file in gr7_files:
		new_file = FitsFile()
		new_file.datasetRelease = gr7
		new_file.filename = gr7_file.productfilename
		new_file.uncompressed_size = gr7_file.contentlength

		session.add(new_file)
	
		# Extract relative path - example file.datauri:
		#   http://galex.stsci.edu/data/GR7/pipe/02-vsn/50089-AIS_89/d/00-visits/0002-img/07-try/AIS_89_0002_sg18-nd-int.fits.gz
		#
		path = os.path.dirname(gr7_file.datauri.split("/pipe")[1]) # all files have prefix 'GR7/pipe'

		if path in directory_paths:
			dir_path = directory_paths[path]
		else:
			try:
				session.query(DirectoryPath).filter(DirectoryPath.path==path).one()
			except sqlalchemy.orm.exc.NoResultFound:
				dir_path = DirectoryPath()
				dir_path.path = path
				dir_path.pathType = relative_path_type
				session.add(dir_path)
				session.flush()

				directory_paths[path] = dir_path
	
		new_file.directoryPaths.append(dir_path)
	
	session.commit()

process_gr7()
#process_gr6()

#session.commit()
db.engine.dispose()
sys.exit(0)
