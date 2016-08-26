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

`typeid` : 
`mission` : List of values: [K2, HUT, JWST, EUVE, KEPLER, Kepler, SWIFT, TESS, FUSE, All Missions, WUPPE, GALEX, IUE, ALL, BEFS, HST, TUES]
`project` : project names?
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
`planeID` : foreign key
`productfilename` : data filename
`datauri` : direct URI to file
`contenttype` : List of values: [NULL, TAR, NULL, GEIS, FITS, JPG, PDF, PNG, GIF, PS, TEXT]
`contentlength` : Size in bytes of file in URL (if filename indicates compression, bytes are compressed size)
`producttype` : List of values: [AUXILIARY, CATALOG, THUMBNAIL, SCIENCE, CALIBRATION, PREVIEW, INFO]
`alternative` : All values NULL.
`producttypeid` : Foreign key to CaomProductDescription table.
`creationdate` , `recordcreated` , `recordmodified ` ,`statuscode` 

### CaomPart

Row count: 49,182,366

`partID` : Primary key.
`artifactID` : Foreign key to CaomArtifact table.
`name` : Filenames.
`producttype` : List of values: [AUXILIARY, CATALOG, THUMBNAIL, SCIENCE, CALIBRATION, PREVIEW, INFO]
`recordcreated ` , `recordmodified` ,`statuscode` 

