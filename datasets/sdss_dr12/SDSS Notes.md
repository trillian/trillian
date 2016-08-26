## SDSS Data

These are the notes and directions for populating the SDSS data. This is comprised of a catalog and imaging data (spectra not yet included). Here I have designed a new schema that improves upon that found in CAS.

### PhotoObj Catalog

#### File Organization

###### DR13

The root location of the DR13 flat files is here:
<https://data.sdss.org/sas/dr13/>

###### DR12

The root location of the DR12 data release is here:
<http://data.sdss3.org/sas/dr12/boss/photoObj/301/>

The data model for SDSS-III data is located here: <http://data.sdss3.org/datamodel/>

Each directory is a plate ID. Within each plate directory is a directory for each camcol (1-6), a [photoField](http://data.sdss3.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/photoField.html) file, and a [photoRun file](http://data.sdss3.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/photoRun.html). Within each camcol directory are the [photoObj](http://data.sdss3.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html) files.

##### Import Order

There are three scripts to populate the database. The execution order is very important as each successive script creates objects that expects to reference the fields created before it.

 1. `photoRun2db.py`
 2. `photoField2db.py`
 3. `photoObj2db.py`

### Imaging Data

The root location of the imaging data is here:
<http://data.sdss3.org/sas/dr12/boss/photoObj/frames/301/>

There is a directory for each plate (named by plate ID). Within each plate directory is a directory for each camcol (1-6), and a `frames-run*.html` page that provides thumbnails for the plate (plus a checksum file). Within each camcol directory are the [frame](http://data.sdss3.org/datamodel/files/BOSS_PHOTOOBJ/frames/RERUN/RUN/CAMCOL/frame.html) files (imaging products) over *ugriz*.

Total size of gzipped imaging (`frame-*`) files: 18.81 TB (18813743111741 bytes)

##### FITS Header Extraction

Run on SDSS servers with base path:

    /uufs/chpc.utah.edu/common/home/sdss00/ebosswork/eboss/photoObj/frames/301
##### FITS Header database import

Importing JSON/FITS headers into database:

    fitsjson2db.py --recursive --directory ~/trillian_data/datasets/sdssDR12/dr12_frame_headers --source dr12 --base-path /uufs/chpc.utah.edu/common/home/sdss00/ebosswork/eboss/photoObj/frames/301
Query to check SDSS DR12 frame import:

    SELECT DISTINCT fits_header_value.numeric_value::integer, count(fits_header_value.numeric_value::integer) FROM fits_header_value
    JOIN fits_header_keyword ON fits_header_keyword.pk=fits_header_value.fits_header_keyword_pk
    JOIN fits_hdu ON fits_hdu.pk=fits_header_value.fits_hdu_pk
    --JOIN fits_file on fits_file.pk=fits_hdu.fits_file_pk
    WHERE fits_header_keyword.label='RUN' AND fits_hdu.number = 1
    AND fits_header_value.numeric_value > 0
    GROUP BY fits_header_value.numeric_value::integer
    ORDER BY fits_header_value.numeric_value::integer;



