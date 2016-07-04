##Directions to Populate Tycho-2 Data Set

##### Prepare Schema

 * Create table "tycho2" under the `dataset_other` schema. (This schema is used for smaller datasets with single tables.) Simply paste the `CREATE TABLE` command from the file `tycho2.sql` into the database.
 * Paste the `COMMENT` commands into the database.
 
##### Download the Data
 
Download all of the data files located here:  
<http://cdsarc.u-strasbg.fr/cgi-bin/Cat?cat=I%2F259&target=http&>

##### Import the Data

Do not decompress the data files, but pipe the files into `psql`. Note this uses tcsh.

    % foreach i (tyc2.dat.*gz)
    foreach? echo Importing $i...
    foreach? gzip -dc $i | sed -e 's/./&|/148' -e 's/ \+|/|/g' -e 's/| \+/|/g' | psql --command "COPY dataset_other.tycho2 FROM stdin WITH (FORMAT 'csv', DELIMITER '|', NULL '')" --username=trillian_admin --dbname=trilliandb
    foreach? end
    
##### Add Primary Key and Indicies

	CREATE SEQUENCE datasets.tycho2_pk_seq;
	ALTER TABLE datasets.tycho2
	  ADD COLUMN pk integer NOT NULL DEFAULT nextval('datasets.tycho2_pk_seq');
	COMMENT ON COLUMN datasets.pk IS 'primary key';

It’s also just as easy to add a new column `pk` of type `serial` instead of manually creating the sequence.

Add the indices:

	CREATE INDEX tycho2_btmag_idx ON dataset_other.tycho2 USING btree (bt_mag);
	CREATE INDEX tycho2_mdec_idx ON dataset_other.tycho2 USING btree (m_dec);
	CREATE INDEX tycho2_mra_idx ON dataset_other.tycho2 USING btree (m_ra);
	CREATE INDEX tycho2_vtmag_idx ON dataset_other.tycho2 USING btree (vt_mag);

