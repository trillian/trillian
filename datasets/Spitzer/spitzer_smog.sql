CREATE TABLE dataset_spitzer.smog_a (
	designation text, -- IAU-style designation
	tmass_designation text, -- 2MASS designation
	tmass_cntr integer, --2MASS counter
	l numeric, -- Galactic longitude
	b numeric, -- Galactic latitude
	dl numeric, -- Galactic longitude uncertainty
	db numeric, -- Galactic latitude uncertainty
	ra numeric, -- equatorial RA J2000
	dec numeric, -- equatorial declination J2000
	dra numeric, -- equatorial RA uncertainty
	ddec numeric, -- equatorial dec uncertainty
	csf smallint, -- close course flag (0-6)
	mag_J numeric, --2MASS J magnitude
	dJ_m numeric, --2MASS J magnitude uncertainty
	mag_H numeric, --2MASS H magnitude
	dH_m numeric, --2MASS H magnitude uncertainty
	mag_Ks numeric, --2MASS Ks magnitude
	dKs_m numeric, --2MASS Ks magnitude uncertainty
	mag3_6 numeric, --IRAC 3.6 micron magnitude
	d3_6m numeric, --IRAC 3.6 micron magnitude uncertainty
	mag4_5 numeric, --IRAC 4.5 micron magnitude
	d4_5m numeric, --IRAC 4.5 micron magnitude uncertainty
	mag5_8 numeric, --IRAC 5.8 micron magnitude
	d5_8m numeric, --IRAC 5.8 micron magnitude uncertainty
	mag8_0 numeric, --IRAC 8.0 micron magnitude
	d8_0m numeric, --IRAC 8.0 micron magnitude uncertainty
	f_J numeric, --2MASS J flux (mJy)
	df_J numeric, --2MASS J flux uncertainty (mJy)
	f_H numeric, --2MASS H flux (mJy)
	df_H numeric, --2MASS H flux uncertainty (mJy)
	f_Ks numeric, --2MASS Ks flux (mJy)
	df_Ks numeric, --2MASS Ks flux uncertainty (mJy)
	f3_6 numeric, --IRAC 3.6 micron flux (mJy)
	df3_6 numeric, --IRAC 3.6 micron flux uncertainty (mJy)
	f4_5 numeric, --IRAC 4.5 micron flux (mJy)
	df4_5 numeric, --IRAC 4.5 micron flux uncertainty (mJy)
	f5_8 numeric, --IRAC 5.8 micron flux (mJy)
	df5_8 numeric, --IRAC 5.8 micron flux uncertainty (mJy)
	f8_0 numeric, --IRAC 8.0 micron flux (mJy)
	df8_0 numeric, --IRAC 8.0 micron flux uncertainty (mJy)
	rms_f3_6 numeric, --rms deviation, 3.6 micron
	rms_f4_5 numeric, --rms deviation, 4.5 micron
	rms_f5_8 numeric, --rms deviation, 5.8 micron
	rms_f8_0 numeric, --rms deviation, 8.0 micron
	sky_3_6 numeric, --local background level, 3.6 micron (MJy/sr)
	sky_4_5 numeric, --local background level, 4.5 micron (MJy/sr)
	sky_5_8 numeric, --local background level, 5.8 micron (MJy/sr)
	sky_8_0 numeric, --local background level, 8.0 micron (MJy/sr)
	sn_J numeric, --signal to noise J, (F/dF)
	sn_H numeric, --signal to noise H, (F/dF)
	sn_Ks numeric, --signal to noise Ks, (F/dF)
	sn_3_6 numeric, --signal to noise 3.6 micron, (F/dF)
	sn_4_5 numeric, --signal to noise 4.5 micron, (F/dF)
	sn_5_8 numeric, --signal to noise 5.8 micron, (F/dF)
	sn_8_0 numeric, --signal to noise 8.0 micron, (F/dF)
	dens_3_6 numeric, --source density 3.6 micron (# sources/ sq arcmin)
	dens_4_5 numeric, --source density 4.5 micron (# sources/ sq arcmin)
	dens_5_8 numeric, --source density 5.8 micron (# sources/ sq arcmin)
	dens_8_0 numeric, --source density 8.0 micron (# sources/ sq arcmin)
	m3_6 smallint, 
	m4_5 smallint, 
	m5_8 smallint, 
	m8_0 smallint, 
	n3_6 smallint, 
	n4_5 smallint, 
	n5_8 smallint, 
	n8_0 smallint, 
	sqf_J integer, --30 bit source quality flag
	sqf_H integer, --30 bit source quality flag
	sqf_Ks integer, --30 bit source quality flag
	sqf_3_6 integer, --30 bit source quality flag
	sqf_4_5 integer, --30 bit source quality flag
	sqf_5_8 integer, --30 bit source quality flag
	sqf_8_0 integer, --30 bit source quality flag
	mf3_6 smallint, --11 bit flux calculation method flag
	mf4_5 smallint, --11 bit flux calculation method flag
	mf5_8 smallint, --11 bit flux calculation method flag
	mf8_0 smallint --11 bit flux calculation method flag
);

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

