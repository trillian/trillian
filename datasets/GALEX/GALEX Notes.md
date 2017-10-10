# Notes on GALEX Data

GALEX (Galaxy Evolution Explorer) is a NASA satellite that operated from 2003-? that performed an all-sky survey in the far- and near-ultraviolet.

| Range   | Wavelengths |
| ------- | ----------- |
| Far-UV  | 1400-1800 Å |
| Near-UV | 1800-2800 Å |

Survey Modes:

* direct imaging - all-sky survey covered 2/3 of the sky
* spectroscopic (grism)

Data was released in a series of “General Releases” (GR), as in GR2, GR3, etc. GR6/GR7 are the combined final release that supercede all previous releases. The release is "joint" as GR7 is a reprocessing of some of the data, but not all of GR6. [TODO: determine the exact delination here.]

GALEX team: <http://www.galex.caltech.edu/about/team.html>

## Data Access

FTP: `ftp://archive.stsci.edu/pub/galex`

HTTP: `http://archive.stsci.edu/pub/galex/`

## Surveys

Link to details of each survey: [http://www.galex.caltech.edu/researcher/techdoc-ch2.html](http://www.galex.caltech.edu/researcher/techdoc-ch2.html)

| Survey                     | Exposure Time (s) | Sky Coverage (sq deg) | Depth (m$_{AB}$) | GR2/3 tiles | GR4 tiles |
| -------------------------- | ----------------- | --------------------- | ---------------- | ----------- | --------- |
| All-sky imaging (AIS)      | 100               | 26,000                | 20.5             | 15,721      | ~28,000   |
| Medium Imaging (MIS)       | 1,500             | 1,000                 | 23.5             | 1,107       | 1,615     |
| Deep Imaging (DIS)         | 30,000            | 80                    | 25.0             | 165         | 193       |
| Nearby Galaxy (NGS)        | 1,500             | 300                   | 28               | 296         | 433       |
| Medium Spectroscopic (MSS) | 150m000           | 5                     | 22               | 3           | ~5        |



| Survey                                   | Associated Imaging Survey | No. Tiles |
| ---------------------------------------- | ------------------------- | --------: |
| All-Sky Imaging (AIS)                    |                           |    34,285 |
| Calibration Survey (CAI)                 |                           |        87 |
| Deep Imaging Survey (DIS)                |                           |       720 |
| Guest Investigator Data (GII)            |                           |     2,112 |
| Medium Imaging Survey (MIS)              |                           |     6,964 |
| Nearby Galaxy Survey (NGS)               |                           |       715 |
| Calibration Survey (Spectra) (CAS)       | CAI                       |        36 |
| Deep Spectroscopic Survey (DSS)          | DIS                       |         1 |
| Medium Spectroscopic Survey (MSS)        | DIS                       |         5 |
| Wide Spectroscopic Survey (WSS)          | DIS                       |        10 |
| Nearby Galaxy Spectroscopic Survey (ETS) | NGS                       |        24 |



#### All Sky Imaging Survey (AIS)

Number of tiles: 34,285.

Link to list all tiles (database form): [http://galex.stsci.edu/GR6/?page=tilelist&survey=ais&showall=Y](http://galex.stsci.edu/GR6/?page=tilelist&survey=ais&showall=Y)

TODO: Get a complete list of tiles.

#### Nearby Galaxy Survey (NGS)

Survey to target nearby galaxies with exposure times of 1,000-1,500s (some have much more). GR4/5 contain 458 pointings.

#### Deep Imaging Survey (DIS)

Deep imaging (30,000 s over 80 deg$^2$).

#### Medium Imaging Survey (MIS)

Exposures of 1,500s of 1,000 deg${^2}$ that match the SDSS footprint, extended to cover the Two Degree Field Galaxy Redshift Survey (2dFGRS) and the AA-Omega (WiggleZ) project.

#### Medium Spectroscopic Survey (MSS)

Spectroscopic observations as part of the Deep Imaging Survey.

#### Calibration Spectroscopy (CAS)

This survey observed white dwarfs for the purpose of calibration.



## Source Catalogs

These source catalogs:

* provide vetted and unique measurements of point and extended sources up to 1 arcminute diameter

* exclude duplicate observations

* include a S/N cut that reduces the number of spurious sources

* have accompanying files describing the footprint of the observations

* intended for cross-matching to WISE, SDSS, 2MASS

  ​

Description of the GASC and GMSC catalogs: [https://archive.stsci.edu/prepds/gcat/gcat_gasc_gmsc.html](https://archive.stsci.edu/prepds/gcat/gcat_gasc_gmsc.html)

Catalog search web interface: http://galex.stsci.edu/GR6/?page=mastform

"GCAT" appears to refer to GASC, GMSC, and the Kepler GCAT.

#### GALEX All-Sky Survey Source Catalog (GASC)

* covers 26,300 deg$^2$
* includes all GALEX observations with exposure times of ~100s, up to 800s
* reaches a depth of NUV 20.5 mag (m$_{AB}$)
* unique sources: ~40M
* data only up to GR6
* [documenation link](https://archive.stsci.edu/prepds/gcat/gcat_gasc_gmsc.html)

Number of rows: 39,570,031

There are two kinds of files:

`pricat`	: primary detections

`seccat` : secondary detections, [note](https://archive.stsci.edu/prepds/gcat/gcat_gasc_gmsc.html) these are:

> a mixture of sources that do not make the NUV S/N=3 cut or are overlap/duplicate data in some way…They are a way to dig deeper, but they should be used with extreme caution. They are there primarily for completeness, as they are mostly just noise. Keep inmind that the GALEX pipeline dug down to S/N 2-2.5.

Direct link to files: [https://archive.stsci.edu/pub/hlsp/gcat/asc/](https://archive.stsci.edu/pub/hlsp/gcat/asc/)

#### GALEX Medium Survey Source Catalog (GMSC)

* based on the GR6 data release
* covers 5,000 deg$^2$ with exposure times between 800-10,000 seconds.
* reaches a depth of NUV 23.5 mag (m$_{AB}$)n 
* unique sources: ~22M
* data only up to GR6

Direct link to files: [https://archive.stsci.edu/pub/hlsp/gcat/msc/](https://archive.stsci.edu/pub/hlsp/gcat/msc/)

#### Kepler GCAT

A GALEX source catalog in the Kepler field, reprocessed using the same software and analysis steps. The differences are detailed on this web page: [https://archive.stsci.edu/prepds/gcat/gcat_dataproducts.html](https://archive.stsci.edu/prepds/gcat/gcat_dataproducts.html)

Contains data up to GR7 but *only* covering the Kepler field.

Direct link to files: [https://archive.stsci.edu/pub/hlsp/gcat/kepler/](https://archive.stsci.edu/pub/hlsp/gcat/kepler/)

#### Links To Column Descriptions

*To be better organized*

<http://www.galex.caltech.edu/wiki/GCAT_Manual>
<http://www.galex.caltech.edu/wiki/Public:Documentation/Chapter_103>
<http://www.galex.caltech.edu/DATA/gr1_docs/GR1_Pipeline_and_advanced_data_description_v2.htm>
<http://www.galex.caltech.edu/DATA/gr1_docs/GR1_basic_data_description_v4.htm>
<http://www.galex.caltech.edu/DATA/gr1_docs/GR1_Pipeline_and_advanced_data_description_v2.htm>
<http://www.galex.caltech.edu/researcher/files/mcat_columns_long.txt>
<http://www.galex.caltech.edu/wiki/Public:Documentation/Chapter_103>

## Data Access

#### Imaging Data

Root location: <http://galex.stsci.edu/data/>
GR6: <http://galex.stsci.edu/data/GR6/>
GR7: <http://galex.stsci.edu/data/GR7/>

Pipeline data guide: <http://asd.gsfc.nasa.gov/archive/galex/Documents/ERO_data_description_3.htm>

##### Directory structure

Data from single-orbit visits are stored in a single directory with the format:

    <ROOT>/<proc ver>/<tile>/<obs mode>/<product>/<image>/<try>/.
`proc-ver` : processing version number [`01-vsn`, `02-vsn`]

`tile` : Tile identification string, e.g. "03000-MISDR1_24278_0266"

`obs-mode` : Instrument observing mode (`d`=direct, `g`=grism, `o`=opaque)

`product` : Data product type (single visit, multiple visits)

`try` : Pipeline processing try, e.g. `07-try`

#### Catalogs

Data access is through the MAST archive. Files can be directly access via HTTP from here:

* Top level:  <https://archive.stsci.edu/pub/hlsp/gcat/>
* GASC: <https://archive.stsci.edu/pub/hlsp/gcat/asc/>
* GMSC: <https://archive.stsci.edu/pub/hlsp/gcat/msc/>
* MCAT: ??

Web page describing the directory structure: <https://archive.stsci.edu/prepds/gcat/gcat_dataproducts.html>

The sky has been divided in 192 chunks numbered from 0-191. Each chunk corresponds to a HEALPix pixel at a resolution of Nside = 4 (nested scheme). Not all chunks have observations.

1 chunk = 215 deg$^2$

GASC : 189 chunks

GMSC : 174 chunks

There is one directory per chunk (named with the "chunk ID").

#### MAST

MAST database schema: <http://galex.stsci.edu/GR6/?page=dbinfo>

Database query: <http://galex.stsci.edu/GR6/?page=sqlform>

# Trillian Notes

### Import Commands

#### GASC Catalog

One file

```bash
fitstable2csv.py --file SP_000-007-asc-xd-pricat.fits --header --trim-strings --delimiter pipe | psql --command "COPY dataset_galex.asc_pricat FROM stdin WITH (FORMAT 'csv', DELIMITER '|', HEADER, NULL '')" --username=trillian_admin --dbname=trilliandb
```

All files:

```bash
for i in `ls *pricat*`
do
echo "Importing $i..."
fitstable2csv.py --file $i --header --trim-strings --delimiter pipe | psql --command "COPY dataset_galex.asc_pricat FROM stdin WITH (FORMAT 'csv', DELIMITER '|', HEADER, NULL '')" --username=trillian_admin --dbname=trilliandb
done
```



# Other Links

Getting started with GALEX data: http://www.galex.caltech.edu/wiki/Public:Documentation/Chapter_103



---

Data downloaded with:

`wget -r --no-parent  ftp://archive.stsci.edu/pub/galex/GCAT/asc/fullsky/catalog`

`wget -r --no-parent  ftp://archive.stsci.edu/pub/galex/GCAT/msc/fullsky/catalog`

