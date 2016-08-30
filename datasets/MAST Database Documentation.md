# Mast Database Documentation

| Table                  | Row count  | Primary Key | Fields Containing Commas                 |
| ---------------------- | ---------- | ----------- | ---------------------------------------- |
| CaomArtifact           | 49,182,366 | artifactID  | none                                     |
| CaomChunk              | 41,871,056 | chunkID     | none                                     |
| CaomEnumFields         | 104        | enumID      |                                          |
| CaomMembers            | 1,662,927  | ??          | none                                     |
| CaomObservation        | 3,579,038  | obsID       | prpTitle, inskeywords, trgkeywords, tlskeywords, trgname, trgtype |
| CaomPart               | 49,182,366 | partID      | none                                     |
| CaomPlane              | 5,803,220  | planeID     |                                          |
| CaomProductDescription | 640        |             |                                          |
| MetaApertures          | 1,564      | id          |                                          |
| MetaFilters            | 496        |             |                                          |
| MetaInstruments        | 39         |             |                                          |
| UCD                    | 480        |             | none                                     |



## Tables

### CaomProductDescription

Row count: 640

`typeid` : Primary key.
`mission` : List of values: [K2, HUT, JWST, EUVE, KEPLER, Kepler, SWIFT, TESS, FUSE, All Missions, WUPPE, GALEX, IUE, ALL, BEFS, HST, TUES]
`project` : project names  294 (~half) values = literal string 'null'.
`producttype` : List of values: [PREVIEW1D, CATALOG, SCIENCE, CALIBRATION, PREVIEW2D, AUXILIARY, THUMBNAIL, null, PREVIEW, INFO]
`contenttype` : List of values: [TAR, BINARY, GEIS, TXT, FITS, JPG, PDF, PNG, null, GIF, PS, TEXT]
`description` : Description of file.
`groupdescription` : List of values: [Minimum Recommended Products, Pointer to service, OTFR, null]
`subgroupdescription` : 
`documentationurl ` : Mostly empty, a few links to FUSE documentation.

### CaomArtifact

This table lists files.

Row count: 75,879,368

`artifactID` : primary key
`planeID` : foreign key to CaomPlane
`productfilename` : data filename
`datauri` : direct URI to file
`contenttype` : List of values: [NULL, TAR, NULL, GEIS, FITS, JPG, PDF, PNG, GIF, PS, TEXT]
`contentlength` : Size in bytes of file in URL (if filename indicates compression, bytes are compressed size)
`producttype` : List of values: [AUXILIARY, CATALOG, THUMBNAIL, SCIENCE, CALIBRATION, PREVIEW, INFO]
`alternative` : All values NULL.
`producttypeid` : Foreign key to CaomProductDescription table (column `typeid`).
`creationdate` , `recordcreated` , `recordmodified ` ,`statuscode` 

### CaomPart

Row count: 49,182,366

`partID` : Primary key.
`artifactID` : Foreign key to CaomArtifact table.
`name` : Filenames.
`producttype` : List of values: [AUXILIARY, CATALOG, THUMBNAIL, SCIENCE, CALIBRATION, PREVIEW, INFO]
`recordcreated ` , `recordmodified` ,`statuscode` 

### CaomPlane

Describes footprints on the sky. The field `posboundsstcs` contains the geometry. The possible formats:

###### CIRCLE

The RA, dec center of the circle is given followed by the radius in [unit]. Examples (note case not consistent):

    CIRCLE ICRS 210.54223248 -32.68040676 0.625
    Circle J2000 106.3265625408 22.6373930106 0.00300694444444
###### POSITION

A single point on the sky. Example:

```
POSITION ICRS 319.02792112  14.48988917
Polygon ICRS Topocenter 284.329544 39.199606 285.288889 38.199522 286.507746 38.896366 285.556333 39.906430
```

###### POLYGON

A polygon, given by a list of RA, dec positions.

```
POLYGON ICRS 129.20117354   7.95365949 129.22981692   7.97845031 129.25289069   7.95318849 129.22353390   7.92776646 129.20117354   7.95365949
```

`planeid` : primary key
`obsid` : Foreign key to CaomObservation.
`productid` : 
`metadatarights` : 
`metarelease` : 
`datarights` : 
`datarelease` : data release date?
`dataproducttype` : Full list: ["spectrum", "NULL", "timeseries", "image", "cube"]
`calibrationlevel` : 
`previewuri` : Direct URI to preview jpeg image.
`producturi` : 
`prvname` : 
`prvreference` : 
`prvversion` : 
`prvproject` : 
`prvproducer` : Institution, e.g. `CALTECH`
`prvrunid` : 
`prvlastexecuted` : 
`prvkeywords` : 
`prvinputs` : 
`poslocationra` : RA
`poslocationdec` : DEC
`posboundsstcs` : Geometry - (see examples above). Complete list of prefixes: ["POLYGON", "Polygon", "CIRCLE", "Circle", POSITION", "Error"]
`posdimension1` : 
`posdimension2` : 
`posresolution` : All rows NULL.
`possamplesize` : 
`postimedependant` : All rows NULL.
`enrvalue` : 
`enrmin` : 
`enrmax` : 
`enrboundsstcs` : 
`enrdimension` : 
`enrresolution` : All rows NULL.
`enrsamplesize` : 
`enrresolvingpower` : All rows NULL.
`enrbandpassname` : 
`enremband` : 
`enrtransition` : 
`enrtransitionspecies` :  All rows NULL.
`enrrestwavelength` : All rows NULL.
`timvalue` : 
`timmin` : 
`timmax` : 
`timboundsstcs` : Time range? Sample format: `RANGE 52797.210058 52797.216354`. Looks like MJD values.
`timdimension` : Integer values in [0,695] and NULL.
`timresolution` : 
`timsamplesize` : 
`timexposure` : Exposure time in seconds?
`plrdimension` : All rows NULL.
`plrstate` : All rows NULL.
`dqflag` : All rows NULL.
`mtrsourcenumberdensity` : All rows NULL.
`mtrbackground` : All rows NULL.
`mtrbackgroundstddev` : All rows NULL.
`mtrfluxdensitylimit` : All rows NULL.
`mtrmaglimit` : All rows NULL.
`recordcreated` : Date record created.
`recordmodified` : Date record modified.
`statuscode` : All values -1.