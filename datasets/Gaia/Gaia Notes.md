# Gaia

## Gaia DR1 Release

Release date: 14 September 2016

Gaia data release documentation: <http://gaia.esac.esa.int/documentation/GDR1/index.html>

Direct link to data: <http://cdn.gea.esac.esa.int/Gaia/>

##### Release is in three parts:

* Main catalog: Astrometric data set of positions, parallaxes, and mean proper motions for 1.1 billion sources.
* TGAS: Subset of 2 million of the brightest stars contained in the Hipparcos and Tycho-2 catalogues. This is a pure subset – no new data from the main catalog, just matches from the two earlier catalogs. This is called the Tycho-Gaia Astrometric Solution (TGAS).


* G-band light curves and the characteristics of ~3000 Cepheid and RR-Lyrae stars observed at high cadence around the south ecliptic pole.

------

### Main Catalog

Short description of data fields: <http://gaia.esac.esa.int/documentation/GDR1/Catalogue_consolidation/sec_cu1cva/sec_cu9gat.html#Ch7.T8>

Detailed descriptions of catalog fields: <https://gaia.esac.esa.int/documentation/GDR1/datamodel/Ch1/gaia_source.html>

Direct link to data: <http://cdn.gea.esac.esa.int/Gaia/gaia_source/>

Number of rows: 1,142,679,769 

Size imported into database: ~400GB

##### Data Model

Documentation: <https://gaia.esac.esa.int/documentation/GDR1/datamodel/>

`solution_id` : Unique identifier that identifies versions of all subsystems that generated the data & input data used.

`source_id` : Unique source identifier (primary key), 64 bit integer, contains HEALPix id & more.

`epoch` : All values "2015.0" - candidate for dropping from database.

`random_index` : random permutation of 0 to N-1 where N = number of rows. Used for statistical sampling.

`phot_variable_flag` : photometric variability flag indicating if variability was identified in the photometric G band. Only a small subset of variable sources were processed and/or exported. Possible values:

*  `NOT_AVAILABLE`  : source not processed, replaced with `NULL` in database (1,142,676,575 entries)
*  `CONSTANT` : source not identified as variable (not exported into data release – 0 entries)
*  `VARIABLE` : source identified and processed as variable – 3,194 entries.

`ecl_lon`, `ecl_lat` : ecliptic latitude, longitude

###### Errors

* Documentation says that there are no values of `ra_pmra_corr` that are NULL, see `solution_id` = 65408 (others not checked)
* ​

### TGAS Subset

The data fields are the same as above with the addition of:

* `hip` : the Hipparcos identifier (smallint, max value: 118322)
* `tycho2_id` : the Tycho-2 identifier (string)

Since this is a subset of the main catalog, Trillian stores this data as a table with the two fields above along with the `solution_id` from the main table which can be used to for joins.

Direct link to data: <http://cdn.gea.esac.esa.int/Gaia/tgas_source/>

### Importing into the database

```bash
% cd datasets/gaia/dr1/main 
% for f in `ls -d *`; do
> echo "Processing: $f"
> gzip -dc $f | sed -e 's/false/f/' -e 's/true/t/' -e 's/NOT_AVAILABLE//' | psql --command "COPY dataset_gaia.dr1 FROM stdin NULL as '' CSV HEADER "
> done
```
##### Indices

```sql
CREATE INDEX q3c_gaia_dr1_main_idx ON dataset_gaia.dr1 (q3c_ang2ipix(ra, dec));
```
Note: Altering the table (e.g. marking a field as `NOT NULL`, takes about 10 minutes.)