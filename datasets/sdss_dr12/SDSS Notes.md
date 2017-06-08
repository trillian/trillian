## SDSS Data

These are the notes and directions for populating the SDSS data. This is comprised of a catalog and imaging data (spectra not yet included). Here I have designed a new schema that improves upon that found in CAS.

### PhotoObj Catalog

#### File Organization

###### DR14

* No changes to photometry since DR13

* Pipeline version: ```v5_10_0```

* Spectra in individual files:

    ```sh
    module switch tree tree/dr14
    cd $BOSS_SPECTRO_REDUX/v5_10_0/spectra/lite
    pwd -P
    /uufs/chpc.utah.edu/common/home/sdss02/dr14/eboss/spectro/redux/v5_10_0/spectra/lite
    ```

* Top level DR14: <[http://data.sdss.org/sas/dr14](http://data.sdss.org/sas/dr14)>

* All releases: ```/uufs/chpc.utah.edu/common/home/sdss/```

* Pre-release documentation:

    * [http://testng.sdss.org/dr14/](http://testng.sdss.org/dr14/)
    * [http://testng.sdss.org/dr14/spectro/spectro_access/](http://testng.sdss.org/dr14/spectro/spectro_access/)
    * Data models: [https://internal.sdss.org/dr14/datamodel/files/BOSS_SPECTRO_REDUX/RUN2D/spectra/](https://internal.sdss.org/dr14/datamodel/files/BOSS_SPECTRO_REDUX/RUN2D/spectra/)



###### DR13

The root location of the DR13 flat files is here:
<https://data.sdss.org/sas/dr13/>

The data model is located here: <https://data.sdss.org/datamodel/>

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

### Data Size

Links:

**[DR13]** Data Volume Table: <http://www.sdss.org/dr13/data_access/volume/>

#### DR13

| Data                                   | Location                                 | Env                  | Size     | Dir Count | File Count |
| -------------------------------------- | ---------------------------------------- | -------------------- | -------- | --------- | ---------- |
| Complete photometric catalog (imaging) | [eboss/photoObj/301](https://data.sdss.org/sas/dr13/eboss/photoObj/301/) |                      | 3.40 TB  | 5,355     | 944,167    |
| 2d & 1d BOSS spectra (reduced)         | [eboss/spectro/redux](https://data.sdss.org/sas/dr13/eboss/spectro/redux/) | $ BOSS_SPECTRO_REDUX | 10.80 TB | 12,762    | 10,905,339 |
|                                        |                                          |                      |          |           |            |
|                                        |                                          |                      |          |           |            |
|                                        |                                          |                      |          |           |            |

| Data                          | Location            | Size     |
| ----------------------------- | ------------------- | -------- |
|                               | $BOSS_SPECTRO_REDUX | 11 TB    |
| DR 12 Imaging (gzipped files) |                     | 18.81 TB |
|                               |                     |          |
|                               |                     |          |
|                               |                     |          |



### Imaging Data

The root location of the imaging data is here:
**[DR12]** : <http://data.sdss3.org/sas/dr12/boss/photoObj/frames/301/>

**[DR13]** : https://data.sdss.org/sas/dr13/eboss/photoObj/

There is a directory for each plate (named by plate ID). Within each plate directory is a directory for each camcol (1-6), and a `frames-run*.html` page that provides thumbnails for the plate (plus a checksum file). Within each camcol directory are the [frame](http://data.sdss3.org/datamodel/files/BOSS_PHOTOOBJ/frames/RERUN/RUN/CAMCOL/frame.html) files (imaging products) over *ugriz*.

Total size of gzipped imaging (`frame-*`) files: **[DR12]** 18.81 TB (18813743111741 bytes)

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



