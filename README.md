Trillian
========
#### An All-Sky, Multi-wavelength Astronomy Computational Engine

Trillian is a project whose aim is to bridge the gap between astrophysical models and the vast amount of publicly available astronomical data. 

Its principle features include:

 * a distributed data scheme
 * distributed computation
 * integrated API access to disparate data

A more detailed descripton of the project can be found here: [http://trillianverse.org](http://trillianverse.org).

An arXiv paper by Demitri Muna and Eric Huff that describes Trillian in more detail can be found here: [arXiv:1402.5932](http://arxiv.org/abs/1402.5932).

Links
-----
Project home page: [http://trillianverse.org](http://trillianverse.org)  
Mozilla ScienceLab Collaborate page: [https://mozillascience.org/projects/trillian](https://mozillascience.org/projects/trillian)  
Mailing list: [https://groups.google.com/forum/#!forum/trillianverse](https://groups.google.com/forum/#!forum/trillianverse)  

Dependencies
------------
###### Server Software
 * [PostgreSQL](http://postgresql.org)
 * [Q3C](https://code.google.com/p/q3c/)

###### Python packages

 * [healpy](https://pypi.python.org/pypi/healpy/1.8.4)
 * [SQLAlchemy](http://sqlalchemy.org)
 * [psycopg2](https://pypi.python.org/pypi/psycopg2/2.5.4)

## Division of Sky with HEALPix

Trillian divides the sky using the HEALPix scheme, which defines equal area regions on a sphere. Each HEALPix region is represented on the server by a one-to-one mapping to a “trixel”: a discrete collection of all data available for that HEALPix region. In other words, data of all wavelengths of a particular part of the sky is located in the same place. Trillian uses the “nested” HEALPix scheme.

## Sky Coverage

The Trillian server has ~30TB of disk space, which is certainly not enough for all-sky coverage while trying to include even the most popular data sets. However, full-sky coverage is not necessary as a proof of concept. Two regions on the sky have been chosen initially: SDSS’s Stripe 82 and the Kepler field, selected as they have been heavily studied and are good representative regions for both extragalactic and Galactic science. Data covering as many wavelengths as possible will be collected for these areas.

## Current Development Goals

The first milestone is to provide an arbitrarily simple model to Trillian, have the framework apply that model to all objects available, and return a likelihood value for each one. Current tasks include:

 - Initialize the server with the coarsest resolution of HEALPix regions/trixels.
 - Define the structure of each trixel (the storage on disk representation of each HEALPix region). This will include a schema for each data set (e.g. SDSS, WISE, etc.) in a shared database on each node, indexing of image data, etc.
 - Define an API for accessing data between nodes.
 - Implement a Docker VM that can accept a user-supplied Python program to be run on nodes.
 - Define the API for the user-supplied Python code. This code will accept data in a defined format (limited on the first pass to magnitudes, spectra, and raw pixel data), and return a likelihood value that the provided data fits the model represented by the code.
 - Define a job queue system (built on Redis?) for communication between the central server and the nodes.

## Support

 * Trillian is gratefully supported by the [Center for Cosmology and Astroparticle Physics (CCAPP)](http://ccapp.osu.edu) at Ohio State University.
 * The Trillian project was selected for Mozilla Science Lab’s [Collaborate on Software for Science](http://collaborate.mozillascience.org).
 * Trillian has been used as a use case example for development of the [DAT](Collaborate on Software for Science) project.

## Contact

The Trillian project is currently seeking collborators. If you are interested in contributing to this project, please contact [Demitri Muna](http://github.com/demitri).

---

Historical Notes

## Mozilla Science Sprint (22 July 2014)
Much of the open data conversation focuses on distributing data - how to make data easily available for local replication.  But, some fields have datasets that are so enormous, transferring and storing additional copies for every user is prohibitively expensive and slow.  Instead, we'd like to explore distributed *analysis* - pushing analysis scripts to the data, rather than pulling the data to us.  The experiments on CERN's LHC set a very successful precedent for this model at the largest scale; one of Trillian's early goals is to achieve this functionality with much lower infrastructural overhead.

For the sprint, we'd like to start exploring a basic Python implementation of a distributed analysis framework.  Our core goals are:

 - resolve which of a list of hosts are eligible to run a job, based on data availability
 - send a Python script to an eligible host for execution
 - return the analysis result to the initiating user.

Stretch goals include:

 - An exploration of security implications and procedures; how do we mitigate the risk of malicious code being executed on the analysis hosts?
 - Smart job queueing: beyond simple data availability, provide job allocation based on available processing power, connection speed, other variables.
