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

#### [WISE AllSky](http://wise2.ipac.caltech.edu/docs/release/allsky/)

* Release date: 14 March 2012
* All-Sky source catalog, 563M objects.
* All-Sky co-added images, 18,240 FITS files x 4 bands
* All-Sky individual exposures, 17,916,180 FITS files – 4 bands of "int", mask, & "unc" files.
* Source databse from single exposure images, ~9.4B detections
* Reject table, 284M low signal to noise detections or image artifacts
* Data taken from 7 January 2010 to 6 August 2010 (full cryogenic phase)

#### [WISE AllWISE](http://wise2.ipac.caltech.edu/docs/release/allwise/)

* Release date: 13 November 2013
* New co-added images from All-Sky individual exposures, 18,240 FITS files x 4 bands, 1.56°x1.56°
* AllWISE multi-epoch photometry database, 42B objects.
* Reject table, 484M low signal to noise detections or image artifacts
* AllWISE supercedes the AllSky release.

#### [unWISE](http://unwise.me)

* Unofficial release; co-adds from All-Sky Level 1b single epoch images.
* Forum located here: [https://groups.google.com/forum/#!forum/unwise](https://groups.google.com/forum/#!forum/unwise)
* Forced photmetry code located here: [https://github.com/dstndstn/unwise-sdss-phot](https://github.com/dstndstn/unwise-sdss-phot)
* Image search / cutouts: [http://unwise.me/imgsearch/](http://unwise.me/imgsearch/)
* Direct file access: [http://unwise.me/data/](http://unwise.me/data/)
* SDSS/WISE forced photometry search: [http://unwise.me/photsearch/](http://unwise.me/photsearch/)
* See separate notes file.

The All-Sky co-added image and detection catalogs will not be used in Trillian. The single epoch All-Sky images will be included in Trillian.

---

### Data Availablility

#### NERSC

##### Level 1b Data Products

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

<u>Direct access URL</u>

Base URL: http://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band_p1bm_frm/

The URL then needs the path of the file, e.g. 0a/00720a/00720a001-w1-int-1b.fits

#### unWISE

Direct HTTP access: [http://unwise.me/data](http://unwise.me/data)

Files are generated on same tile centers as the WISE Atlas Images.

|                                   |                 |
| --------------------------------- | --------------- |
| Number of tiles / wavelength band | 18,240          |
| Total number of images            | 72,960          |
| Image size                        | 1.56 x 1.56 deg |

Files are organized in directories by first three digits of tile name, 000-358.

Files can be directly downloaded at:

http://unwise.me/[ttt]/[tilename]/[filename]

e.g.:

http://unwise.me/data/000/0000m016/unwise-0000m016-w1-img-m.fits

where `[ttt]` is the first three digits of the tile name.

In each directory (e.g. `000/0000m016`) are the following files in each of the four bands (`w1`,`w2`, `w3`, `w4` ).

| Filename                              | Description                              |
| ------------------------------------- | ---------------------------------------- |
| `unwise-0000m016-w1-frames.fits`      | List of frames that went into co-add.    |
| `unwise-0000m016-w1-img-m.fits`       | "Masked" image, 2048x2048 pixels, TAN projected at 2.75"/pixel. (Eq. 14 C$_m$ in paper.) |
| `unwise-0000m016-w1-img-u.fits`       |                                          |
| `unwise-0000m016-w1-invvar-m.fits.gz` | Inverse-variance of the co-add image. (Eq. 12 W$_m$ in paper.) |
| `unwise-0000m016-w1-invvar-u.fits.gz` |                                          |
| `unwise-0000m016-w1-mask.gz`          | A bitmap file for each of the individual L1b frames that contributed. |
| `unwise-0000m016-w1-n-m.fits.gz`      | Eq. 14 in paper, N$_m$. Number of exposures contributing to the coadd at this pixel. |
| `unwise-0000m016-w1-n-u.fits.gz`      | Eq. x in paper, N$_u$.                   |
| `unwise-0000m016-w1-std-m.fits.gz`    | Eq. 15 in paper, S$_m$. Sample standard deviation (scatter) of the individual-exposure pixels. This will be large if, for example, the source is variable.  This could be used to, for example, detect pixels that vary more than expected due to noise and source Poisson variation, which might indicate unmasked artifacts or variability. |
| `unwise-0000m016-w1-std-u.fits.gz`    |                                          |



Representative file sizes:

	  	 60K Feb 17  2014 unwise-0000m016-w1-frames.fits
		 17M Feb 17  2014 unwise-0000m016-w1-img-m.fits
		 17M Feb 17  2014 unwise-0000m016-w1-img-u.fits
		5.3M Feb 17  2014 unwise-0000m016-w1-invvar-m.fits.gz
		434K Feb 17  2014 unwise-0000m016-w1-invvar-u.fits.gz
		1.3M Feb 19  2014 unwise-0000m016-w1-mask.tgz
		1.6M Feb 17  2014 unwise-0000m016-w1-n-m.fits.gz
		352K Feb 17  2014 unwise-0000m016-w1-n-u.fits.gz
		8.4M Feb 17  2014 unwise-0000m016-w1-std-m.fits.gz
		8.4M Feb 17  2014 unwise-0000m016-w1-std-u.fits.gz



### References

Field descriptions: <http://wise2.ipac.caltech.edu/docs/release/allwise/expsup/sec2_1a.html>  
Schema: <http://irsadist.ipac.caltech.edu/wise-allwise/wise-allwise-cat-schema.txt>  

------

## Processing Commands

#### All-Sky Level 1b data

The Level 1b data was found at NERSC (`cosmo/data/wise/allsky/4band_p1bm_frm`). The headers were extracted with the command: `nohup ~/repos/trillian/scripts/fits2header.py -d ~/cosmo/data/wise/allsky/4band_p1bm_frm/0a --recursive -o $SCRATCH/wise_level1b_headers/0a --compressed --gzip --processes 26 &`

Each top level directory was processed alone by hand due to the sheer number of files.

#### unWISE

FITS headers extracted at NERSC:

```bash
% for path in `ls -d ~/cosmo/data/unwise/unwise-coadds/[0-9][0-9][0-9]`; do
> d=`basename $path`
> out="/scratch2/scratchdirs/muna/unWISE_headers/$d"
> ~/repos/trillian/scripts/fits2header.py --recursive -d $path -o $out --compressed --gzip -p 26
> echo "Processed: $out"
> done
```

Base directory: `/global/homes/m/muna/cosmo/data/unwise/unwise-coadds/`

Command to generate list of directories and count of FITS files in each (for later verification):

```bash
for i in `ls -d ???`; do echo $i `find $i -type f -name '*fits*' | lc`; done
```
---

## Populating the Database

#### All-WISE Catalog

Navigate to data directory: 

    % cd datasets/wise-allwise

Using `tcsh`:

```bash
% foreach i (*bz2)
foreach? echo Importing $i ...
bzip2 -dc $i | sed 's/|$//' | psql --command "COPY dataset_wise.allwise FROM stdin WITH DELIMITER '|' NULL AS '' " 
```

This will take many (~10) hours. Next, define the primary key. We will use the [`cntr`](http://wise2.ipac.caltech.edu/docs/release/allwise/expsup/sec2_1a.html#cntr) field. This is also a very long process, so execute it in the background:

```
% nohup psql --command "ALTER TABLE dataset_wise.allwise ADD CONSTRAINT allwise_pk PRIMARY KEY (cntr);" &
```

Index more columns (in the background, as above):

```sql
CREATE INDEX allwise_sourceid_idx ON dataset_wise.allwise (source_id ASC NULLS LAST);
CREATE INDEX allwise_w1mpro_idx ON dataset_wise.allwise (w1mpro ASC NULLS LAST);
CREATE INDEX allwise_w2mpro_idx ON dataset_wise.allwise (w2mpro ASC NULLS LAST);
CREATE INDEX allwise_w3mpro_idx ON dataset_wise.allwise (w3mpro ASC NULLS LAST);
CREATE INDEX allwise_w4mpro_idx ON dataset_wise.allwise (w4mpro ASC NULLS LAST);
```

Index ra, dec coordinates:

```sql
CREATE INDEX q3c_allwise_idx ON dataset_wise.allwise (q3c_ang2ipix(ra, dec));
```

#### unWISE

All unWISE FITS files read directly from "cosmo" data directory at NERSC.

