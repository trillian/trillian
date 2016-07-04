### Spitzer Mapping of the Outer Galaxy (SMOG)

This document describes the details of the SMOG catalog in the Trillian database. See the "Spitzer catalogs.md" file for more links and information about the catalog.

The SMOG catalog was released as two catalogs, an A catalog (the SMOG source list, a "more complete Archive") and a C catalog (the SMOG Catalog, a "highly reliable Catalog") (a more detailed description can be found [here](http://irsa.ipac.caltech.edu/data/SPITZER/GLIMPSE/catalogs/SMOG/SMOG_source_lists_jan2016.README)). Both are available in Trillian as `dataset_spitzer.smog_a` and `dataset_spitzer.smog_c`. To populate the database, use the SQL definition of the table in this directory and modify the table name to create each.

Use the following commands to fill in the comment fields in the table definition. Again, be sure to modify the table name for each `smog_a` and `smog_c` tables.

    COMMENT ON COLUMN dataset_spitzer.smog_a.designation IS 'IAU-style designation';
    COMMENT ON COLUMN dataset_spitzer.smog_a.tmass_designation IS '2MASS designation';
    COMMENT ON COLUMN dataset_spitzer.smog_a.tmass_cntr IS '2MASS counter';
    COMMENT ON COLUMN dataset_spitzer.smog_a.l IS 'Galactic longitude';
    COMMENT ON COLUMN dataset_spitzer.smog_a.b IS 'Galactic latitude';
    COMMENT ON COLUMN dataset_spitzer.smog_a.dl IS 'Galactic longitude uncertainty';
    COMMENT ON COLUMN dataset_spitzer.smog_a.db IS 'Galactic latitude uncertainty';
    COMMENT ON COLUMN dataset_spitzer.smog_a.ra IS 'equatorial RA J2000';
    COMMENT ON COLUMN dataset_spitzer.smog_a.dec IS 'equatorial declination J2000';
    COMMENT ON COLUMN dataset_spitzer.smog_a.dra IS 'equatorial RA uncertainty';
    COMMENT ON COLUMN dataset_spitzer.smog_a.ddec IS 'equatorial dec uncertainty';
    COMMENT ON COLUMN dataset_spitzer.smog_a.csf IS 'close course flag (0-6)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.mag_J IS '2MASS J magnitude';
    COMMENT ON COLUMN dataset_spitzer.smog_a.dJ_m IS '2MASS J magnitude uncertainty';
    COMMENT ON COLUMN dataset_spitzer.smog_a.mag_H IS '2MASS H magnitude';
    COMMENT ON COLUMN dataset_spitzer.smog_a.dH_m IS '2MASS H magnitude uncertainty';
    COMMENT ON COLUMN dataset_spitzer.smog_a.mag_Ks IS '2MASS Ks magnitude';
    COMMENT ON COLUMN dataset_spitzer.smog_a.dKs_m IS '2MASS Ks magnitude uncertainty';
    COMMENT ON COLUMN dataset_spitzer.smog_a.mag3_6 IS 'IRAC 3.6 micron magnitude';
    COMMENT ON COLUMN dataset_spitzer.smog_a.d3_6m IS 'IRAC 3.6 micron magnitude uncertainty';
    COMMENT ON COLUMN dataset_spitzer.smog_a.mag4_5 IS 'IRAC 4.5 micron magnitude';
    COMMENT ON COLUMN dataset_spitzer.smog_a.d4_5m IS 'IRAC 4.5 micron magnitude uncertainty';
    COMMENT ON COLUMN dataset_spitzer.smog_a.mag5_8 IS 'IRAC 5.8 micron magnitude';
    COMMENT ON COLUMN dataset_spitzer.smog_a.d5_8m IS 'IRAC 5.8 micron magnitude uncertainty';
    COMMENT ON COLUMN dataset_spitzer.smog_a.mag8_0 IS 'IRAC 8.0 micron magnitude';
    COMMENT ON COLUMN dataset_spitzer.smog_a.d8_0m IS 'IRAC 8.0 micron magnitude uncertainty';
    COMMENT ON COLUMN dataset_spitzer.smog_a.f_J IS '2MASS J flux (mJy)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.df_J IS '2MASS J flux uncertainty (mJy)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.f_H IS '2MASS H flux (mJy)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.df_H IS '2MASS H flux uncertainty (mJy)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.f_Ks IS '2MASS Ks flux (mJy)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.df_Ks IS '2MASS Ks flux uncertainty (mJy)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.f3_6 IS 'IRAC 3.6 micron flux (mJy)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.df3_6 IS 'IRAC 3.6 micron flux uncertainty (mJy)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.f4_5 IS 'IRAC 4.5 micron flux (mJy)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.df4_5 IS 'IRAC 4.5 micron flux uncertainty (mJy)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.f5_8 IS 'IRAC 5.8 micron flux (mJy)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.df5_8 IS 'IRAC 5.8 micron flux uncertainty (mJy)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.f8_0 IS 'IRAC 8.0 micron flux (mJy)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.df8_0 IS 'IRAC 8.0 micron flux uncertainty (mJy)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.rms_f3_6 IS 'rms deviation, 3.6 micron';
    COMMENT ON COLUMN dataset_spitzer.smog_a.rms_f4_5 IS 'rms deviation, 4.5 micron';
    COMMENT ON COLUMN dataset_spitzer.smog_a.rms_f5_8 IS 'rms deviation, 5.8 micron';
    COMMENT ON COLUMN dataset_spitzer.smog_a.rms_f8_0 IS 'rms deviation, 8.0 micron';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sky_3_6 IS 'local background level, 3.6 micron (MJy/sr)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sky_4_5 IS 'local background level, 4.5 micron (MJy/sr)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sky_5_8 IS 'local background level, 5.8 micron (MJy/sr)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sky_8_0 IS 'local background level, 8.0 micron (MJy/sr)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sn_J IS 'signal to noise J, (F/dF)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sn_H IS 'signal to noise H, (F/dF)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sn_Ks IS 'signal to noise Ks, (F/dF)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sn_3_6 IS 'signal to noise 3.6 micron, (F/dF)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sn_4_5 IS 'signal to noise 4.5 micron, (F/dF)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sn_5_8 IS 'signal to noise 5.8 micron, (F/dF)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sn_8_0 IS 'signal to noise 8.0 micron, (F/dF)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.dens_3_6 IS 'source density 3.6 micron (# sources/ sq arcmin)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.dens_4_5 IS 'source density 4.5 micron (# sources/ sq arcmin)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.dens_5_8 IS 'source density 5.8 micron (# sources/ sq arcmin)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.dens_8_0 IS 'source density 8.0 micron (# sources/ sq arcmin)';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sqf_J IS '30 bit source quality flag';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sqf_H IS '30 bit source quality flag';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sqf_Ks IS '30 bit source quality flag';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sqf_3_6 IS '30 bit source quality flag';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sqf_4_5 IS '30 bit source quality flag';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sqf_5_8 IS '30 bit source quality flag';
    COMMENT ON COLUMN dataset_spitzer.smog_a.sqf_8_0 IS '30 bit source quality flag';
    COMMENT ON COLUMN dataset_spitzer.smog_a.mf3_6 IS '11 bit flux calculation method flag';
    COMMENT ON COLUMN dataset_spitzer.smog_a.mf4_5 IS '11 bit flux calculation method flag';
    COMMENT ON COLUMN dataset_spitzer.smog_a.mf5_8 IS '11 bit flux calculation method flag';
    COMMENT ON COLUMN dataset_spitzer.smog_a.mf8_0 IS '11 bit flux calculation method flag';


##### TODO

 * define primary key
 * determine which fields to index
 * properly link 2MASS sources to the Trillian database
 * potentially remove redundant fields from the 2MASS catalog