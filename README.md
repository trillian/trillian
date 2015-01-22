Trillian
========

Trillian is a project whose aim is to bridge the gap between astrophysical models and the vast amount of publicly available astronomical data. 

Its principle features include:

 * a distributed data scheme
 * distributed computation
 * integrated API access to disparate data

Dependencies
------------

###### Python packages

 * healpy
 * SQLAlchemy
 * psycopg2

## Division of Sky with HEALPix

Trillian divides the sky using the HEALPix pixel scheme, which divides the sky into equal area regions.

##Mozilla Science Sprint
Much of the open data conversation focuses on distributing data - how to make data easily available for local replication.  But, some fields have datasets that are so enormous, transferring and storing additional copies for every user is prohibitively expensive and slow.  Instead, we'd like to explore distributed *analysis* - pushing analysis scripts to the data, rather than pulling the data to us.  The experiments on CERN's LHC set a very successful precedent for this model at the largest scale; one of Trillian's early goals is to achieve this functionality with much lower infrastructural overhead.

For the sprint, we'd like to start exploring a basic Python implementation of a distributed analysis framework.  Our core goals are:

 - Resolve which of a list of hosts are eligible to run a job, based on data availability
 - send a Python script to an eligible host for execution
 - return the analysis result to the initiating user.

Stretch goals include:

 - An exploration of security implications and procedures; how do we mitigate the risk of malicious code being executed on the analysis hosts?
 - Smart job queueing: beyond simple data availability, provide job allocation based on available processing power, connection speed, other variables.

At this stage, strategic advice from a python expert is as valuable as lines of code, so if you have ideas in this space, please start a conversation in the issue tracker! 
