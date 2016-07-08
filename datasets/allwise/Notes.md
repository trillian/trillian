# WISE Notes

### Overview

The Wide-field Infrared Survey Explorer (WISE) is a NASA infrared satellite.

| Band | Wavelength | Angular Resolution |
| ---- | ---------- | ------------------ |
| 1    | 3.4 µm     | 6.1"               |
| 2    | 4.6 µm     | 6.4"               |
| 3    | 12 µm      | 6.5"               |
| 4    | 22 µm      | 12.0"              |

This is an overview of the available WISE data products:

###### [WISE AllSky](http://wise2.ipac.caltech.edu/docs/release/allsky/)

* Release date: 14 March 2012
* All-Sky source catalog, 563M objects.
* All-Sky co-added images, 18,240 FITS files x 4 bands
* All-Sky individual exposures, 
* Source databse from single exposure images, ~9.4B detections
* Reject table, 284M low signal to noise detections or image artifacts
* Data taken from 7 January 2010 to 6 August 2010 (full cryogenic phase)

###### [WISE AllWISE](http://wise2.ipac.caltech.edu/docs/release/allwise/)

* Release date: 13 November 2013
* New co-added images from All-Sky individual exposures, 18,240 FITS files x 4 bands, 1.56°x1.56°
* AllWISE multi-epoch photometry database, 42B objects.
* Reject table, 484M low signal to noise detections or image artifacts
* AllWISE supercedes the AllSky release.

The All-Sky co-added image and detection catalogs will not be used in Trillian.

### Data Availablility

#### NERSC

###### Level 1b Data Products

Link at IPAC: [http://irsa.ipac.caltech.edu/ibe/docs/wise/merge/merge_p1bm_frm/](http://irsa.ipac.caltech.edu/ibe/docs/wise/merge/merge_p1bm_frm/)

These are the single exposure images from the AllSky and NEOWISE-R releases, separated as:

| Data Set                                 | Directory                    |
| ---------------------------------------- | :--------------------------- |
| AllSky Single Exposure Images            | `allsky/4band_p1bm_frm`      |
| 3-Band Cryo Single Exposure Images       | `cryo_3band/3band_p1bm_frm`  |
| Post-Cryo (2 band) Single Exposure Images | `postcryo/2band_p1bm_frm`    |
| NEOWISE-R Single Exposure Images         | `neowiser/neowiser_p1bm_frm` |

Each frame is uniquely identified by the `scan_id`, `frame_num`, and `band`.

These are the (only) single-exposure images:
<http://portal.nersc.gov/project/cosmo/data/wise/allsky/4band_p1bm_frm/>

#### IPAC

IPAC mission keyword: "wise"

Images:
<http://irsa.ipac.caltech.edu/ibe/data/wise/merge/merge_p1bm_frm/>

API Links:  
<http://irsa.ipac.caltech.edu/voapi.html>  
<http://wise2.ipac.caltech.edu/docs/release/allwise/expsup/sec1_5.html#api>  

### References

Field descriptions: <http://wise2.ipac.caltech.edu/docs/release/allwise/expsup/sec2_1a.html>  
Schema: <http://irsadist.ipac.caltech.edu/wise-allwise/wise-allwise-cat-schema.txt>  

------

## Processing Commands

The Level 1b data was found at NERSC (`cosmo/data/wise/allsky/4band_p1bm_frm`). The headers were extracted with the command: `nohup ~/repos/trillian/scripts/fits2header.py -d ~/cosmo/data/wise/allsky/4band_p1bm_frm --recursive -o ~/wise_level1b_headers --compressed --gzip --processes 25 &`

---

## Populating the Database

Navigate to data directory: 

    % cd datasets/wise-allwise

Using `tcsh`:

```
% foreach i (*bz2)
foreach? echo Importing $i ...
bzip2 -dc $i | sed 's/|$//' | psql --command "COPY dataset_wise.allwise FROM stdin WITH DELIMITER '|' NULL AS '' " 
```

This will take many (~10) hours. Next, define the primary key. We will use the [`cntr`](http://wise2.ipac.caltech.edu/docs/release/allwise/expsup/sec2_1a.html#cntr) field. This is also a very long process, so execute it in the background:

```
% nohup psql --command "ALTER TABLE dataset_wise.allwise ADD CONSTRAINT allwise_pk PRIMARY KEY (cntr);" &
```

Index more columns (in the background, as above):

```
CREATE INDEX allwise_sourceid_idx ON dataset_wise.allwise (source_id ASC NULLS LAST);
CREATE INDEX allwise_w1mpro_idx ON dataset_wise.allwise (w1mpro ASC NULLS LAST);
CREATE INDEX allwise_w2mpro_idx ON dataset_wise.allwise (w2mpro ASC NULLS LAST);
CREATE INDEX allwise_w3mpro_idx ON dataset_wise.allwise (w3mpro ASC NULLS LAST);
CREATE INDEX allwise_w4mpro_idx ON dataset_wise.allwise (w4mpro ASC NULLS LAST);
```

Index ra, dec coordinates:

```
CREATE INDEX q3c_allwise_idx ON dataset_wise.allwise (q3c_ang2ipix(ra, dec));
```

​    