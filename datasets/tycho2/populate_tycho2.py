#!/usr/bin/env python

import os
import sys

import sqlalchemy

from trillian.dataset import Tycho2
from trillian.database.connections import RemoteTunnelConnection as db
from trillian.trilliandb.ModelClasses import Dataset

session = db.Session()

try:
	root_data_directory = os.environ["TRILLIAN_DATA"]
except KeyError:
	raise Exception("The environment variable 'TRILLIAN_DATA' pointing to the data directory must be set.")
	sys.exit(1);

data_directory = os.path.join("root_data_directory", "datasets", "tycho2")

# Check if the dataset object exists in the database
try:
	tycho2_dataset = session.query(Dataset).filter(Dataset.name=="Tycho-2").one()
except sqlalchemy.orm.exc.NoResultFound:
	tycho2_dataset = Dataset()
	tycho2_dataset.label = "Tycho-2"
	session.add(tycho2_dataset)
	session.commit()

# The dataset is simple enough to populate by hand.