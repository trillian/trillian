#!/usr/bin/env python

'''
This script creates the first trixels into the database.

This corresponds to n_side = 1 (12 pixels, lowest resolution).
Trillian uses the nested HEALPix scheme.

This script assumes there are no rows in the "trixel" table and no nodes.
The node information is hard coded here, but this script should really
only be run once.

'''

import sqlalchemy
import healpy as hp

from trillian.database.connections.LocalhostConnection import db
from trillian.trilliandb.ModelClasses import Server, Trixel, Node, NodeCapability

session = db.Session()

# there is only one server - effectively a singleton
try:
	trillianServer = session.query(Server).filter(Server.name=="Trillian Server").one()
except sqlalchemy.orm.exc.NoResultFound:
	# create initial server
	trillianServer = Server()
	trillian.name = "Trillian Server"
	session.add(trillianServer)
	
# ----------------------
# First node information
# ----------------------

# fetch/populate node capabilities
try:
	node_compute_capability = session.query(NodeCapability)\.
									 .filter(NodeCapability.label=="Compute").one()
except sqlalchemy.orm.exc.NoResultFound:
	node_compute_capability = NodeCapability()
	node_compute_capability.label = "Compute"
	session.add(node_compute_capability)

try:
	node_storage_capability = session.query(NodeCapability)\.
									 .filter(NodeCapability.label=="Storage").one()
except sqlalchemy.orm.exc.NoResultFound:
	node_storage_capability = NodeCapability()
	node_storage_capability.label = "Storage"
	session.add(node_storage_capability)

# Create first node
# -----------------
node1 = Node()
node1.host_address = "128.0.0.1" # first node is localhost
node1.server = trillianServer
node1.available_space = 10 * u.TB
# additional details should be filled in manually (i.e. not included
# in publicly available scripts) for security.
#node1.username
#node1.server_path

node.capabilities.append(node_compute_capability)
node.capabilities.append(node_storage_capability)

session.append(node1)
trillianServer.nodes.append(node1)

# -----------------------
# Create first 12 Trixels
# -----------------------
# Pixels are numbered starting from 0
# A map is available here: http://healpix.jpl.nasa.gov/html/intronode4.htm

for pix_id in range(hp.nside2npix(nside=1)):
	trixel = Trixel()
	trixel.healpix_n_side = 1
	trixel.healpix_pixel_id = pix_id
	# parent_trixel_id defaults to NULL, i.e., top level object
	
	session.add(trixel)
	node1.trixels.append(trixel)
		
session.commit()





