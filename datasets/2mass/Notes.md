## 2MASS Data Set

#### Data Access

IPAC: <http://irsa.ipac.caltech.edu/ibe/data/twomass/>  

Column descriptions: <http://cfa165.harvard.edu/software/catalogs/tmc.format.html>

#### Importing into the Database

Create the table from the file `twomass_psc_schema.sql` in this directory.

Command used from raw files:  

    zcat psc_* | psql -c "COPY dataset_twomass.psc FROM stdin WITH DELIMITER '|' "

Use the field `pts_key` as the primary key:

    ALTER TABLE dataset_twomass.psc ADD CONSTRAINT twomass_psc_pk PRIMARY KEY (pts_key);   

Index creation:  

	CREATE INDEX designation_idx ON dataset_twomass.psc (designation ASC NULLS LAST);
	CREATE INDEX j_m_idx ON dataset_twomass.psc (j_m ASC NULLS LAST);
	CREATE INDEX h_m_idx ON dataset_twomass.psc (h_m ASC NULLS LAST);
	CREATE INDEX k_m_idx ON dataset_twomass.psc (k_m ASC NULLS LAST);
	
Index ra, dec coordinates:

    CREATE INDEX q3c_2mass_idx ON dataset_twomass.psc (q3c_ang2ipix(ra, dec));

