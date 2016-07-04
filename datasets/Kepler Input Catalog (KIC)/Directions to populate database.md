## Kepler Input Catalog (KIC)

##### Data Source

URLs:  
[https://www.cfa.harvard.edu/kepler/kic/kicindex.html](https://www.cfa.harvard.edu/kepler/kic/kicindex.html)  
[http://tdc-www.harvard.edu/software/catalogs/kic.html](http://tdc-www.harvard.edu/software/catalogs/kic.html)  
[https://archive.stsci.edu/kepler/kic.html](https://archive.stsci.edu/kepler/kic.html)  

Number of rows: ~13M (13,161,029)  
Size of disk (compressed): 761M  

Field definitions:  
[http://archive.stsci.edu/kepler/kic10/help/quickcol.html
](http://archive.stsci.edu/kepler/kic10/help/quickcol.html
)  
[http://archive.stsci.edu/search_fields.php?mission=kepler](http://archive.stsci.edu/search_fields.php?mission=kepler)  

##### Importing the Data

Define the table from the SQL description in this directory.

    gzip -dc kic.txt.gz | psql --command "COPY dataset_kepler.kic FROM stdin WITH (FORMAT 'csv', HEADER,  DELIMITER '|', NULL '') " --username=trillian_admin --dbname=trilliandb
    
Add a primary key:

    ALTER TABLE ONLY dataset_kepler.kic
    ADD CONSTRAINT kic_pk PRIMARY KEY (kepler_id);

Add indices:

    CREATE INDEX d51mag_idx ON dataset_kepler.kic USING btree (d51mag);
    CREATE INDEX feh_idx ON dataset_kepler.kic USING btree (feh);
	CREATE INDEX galaxy_idx ON dataset_kepler.kic USING btree (galaxy);
	CREATE INDEX gmag_idx ON dataset_kepler.kic USING btree (gmag);
	CREATE INDEX gredmag_idx ON dataset_kepler.kic USING btree (gredmag);
	CREATE INDEX hmag_idx ON dataset_kepler.kic USING btree (hmag);
	CREATE INDEX imag_idx ON dataset_kepler.kic USING btree (imag);
	CREATE INDEX jmag_idx ON dataset_kepler.kic USING btree (jmag);
	CREATE INDEX kepmag_idx ON dataset_kepler.kic USING btree (kepmag);
	CREATE INDEX kmag_idx ON dataset_kepler.kic USING btree (kmag);
	CREATE INDEX logg_idx ON dataset_kepler.kic USING btree (logg);
	CREATE INDEX pmdec_idx ON dataset_kepler.kic USING btree (pmdec);
	CREATE INDEX pmra_idx ON dataset_kepler.kic USING btree (pmra);
	CREATE INDEX rmag_idx ON dataset_kepler.kic USING btree (rmag);
	CREATE INDEX teff_idx ON dataset_kepler.kic USING btree (teff);
	CREATE INDEX tm_designation_idx ON dataset_kepler.kic USING btree (tm_designation);
	CREATE INDEX tmid_idx ON dataset_kepler.kic USING btree (tmid);
	CREATE INDEX variable_idx ON dataset_kepler.kic USING btree (variable);
	CREATE INDEX zmag_idx ON dataset_kepler.kic USING btree (zmag);

    
