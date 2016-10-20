-- Table: dataset_gaia.dr1

-- DROP TABLE dataset_gaia.dr1;

CREATE TABLE dataset_gaia.dr1
(
  solution_id bigint, -- Solution Identifier
  source_id bigint NOT NULL, -- Unique source identifier
  random_index bigint, -- Random index used to select subsets
  ref_epoch numeric, -- Reference epoch (Julian Year)
  ra numeric NOT NULL, -- Right ascension (deg)
  ra_error numeric NOT NULL, -- Standard error of right ascension (mas)
  "dec" numeric NOT NULL, -- Declination (deg)
  dec_error numeric NOT NULL, -- Standard error of declination (mas)
  parallax numeric, -- Parallax (mas)
  parallax_error numeric, -- Standard error of parallax (mas)
  pmra numeric, -- Proper motion in right ascension direction (mas/year)
  pmra_error numeric, -- Standard error of proper motion in right ascension direction (mas/year)
  pmdec numeric, -- Proper motion in declination direction (mas/year)
  pmdec_error numeric, -- Standard error of proper motion in declination direction (mas/year)
  ra_dec_corr numeric, -- Correlation between right ascension and declination
  ra_parallax_corr numeric, -- Correlation between right ascension and parallax
  ra_pmra_corr numeric, -- Correlation between right ascension and p.m. in r.a.
  ra_pmdec_corr numeric, -- Correlation between right ascension and p.m. in declination
  dec_parallax_corr numeric, -- Correlation between declination and parallax
  dec_pmra_corr numeric, -- Correlation between declination and p.m. in right ascension
  dec_pmdec_corr numeric, -- Correlation between declination and p.m. in declination
  parallax_pmra_corr numeric, -- Correlation between parallax and p.m. in right ascension
  parallax_pmdec_corr numeric, -- Correlation between parallax and p.m. in declination
  pmra_pmdec_corr numeric, -- Correlation between p.m. in r.a. and p.m. in declination
  astrometric_n_obs_al smallint NOT NULL, -- Total number of observations AL
  astrometric_n_obs_ac smallint NOT NULL, -- Total number of observations AC
  astrometric_n_good_obs_al smallint, -- Number of good observations AL
  astrometric_n_good_obs_ac smallint, -- Number of good observations AC
  astrometric_n_bad_obs_al smallint NOT NULL, -- Number of bad observations AL
  astrometric_n_bad_obs_ac smallint NOT NULL, -- Number of bad observations AC
  astrometric_delta_q numeric, -- Hipparcos/Gaia discrepancy (Hipparcos TGAS subset only)
  astrometric_excess_noise numeric NOT NULL, -- Excess noise of the source (mas)
  astrometric_excess_noise_sig numeric NOT NULL, -- Significance of excess noise
  astrometric_primary_flag boolean, -- Primary or seconday
  astrometric_relegation_factor numeric NOT NULL, -- Relegation factor
  astrometric_weight_al numeric NOT NULL, -- Mean astrometric weight of the source (mas^−2)
  astrometric_weight_ac numeric, -- Mean astrometric weight of the source (mas^−2)
  astrometric_priors_used smallint, -- Type of prior used in in the astrometric solution
  matched_observations smallint, -- Amount of observations matched to this source
  duplicated_source boolean, -- Source with duplicate sources
  scan_direction_strength_k1 numeric NOT NULL, -- Degree of concentration of scan directions across the source
  scan_direction_strength_k2 numeric NOT NULL, -- Degree of concentration of scan directions across the source
  scan_direction_strength_k3 numeric NOT NULL, -- Degree of concentration of scan directions across the source
  scan_direction_strength_k4 numeric NOT NULL, -- Degree of concentration of scan directions across the source
  scan_direction_mean_k1 numeric NOT NULL, -- Mean position angle of scan directions across the source (deg)
  scan_direction_mean_k2 numeric NOT NULL, -- Mean position angle of scan directions across the source (deg)
  scan_direction_mean_k3 numeric NOT NULL, -- Mean position angle of scan directions across the source (deg)
  scan_direction_mean_k4 numeric NOT NULL, -- Mean position angle of scan directions across the source (deg)
  phot_g_n_obs integer, -- Number of observations contributing to G photometry
  phot_g_mean_flux numeric, -- G band mean flux (e^−1 s^−1)
  phot_g_mean_flux_error numeric, -- Error on G band mean flux (e^−1 s^−1)
  phot_g_mean_mag numeric, -- G band mean magnitude (mag)
  phot_variable_flag text, -- Photometric variability flag
  l numeric, -- Galactic longitude (deg)
  b numeric, -- Galactic latitude (deg)
  ecl_lon numeric, -- Ecliptic longitude (deg)
  ecl_lat numeric, -- Ecliptic latitude (deg)
  CONSTRAINT gaia_dr1_main_source_id_pk PRIMARY KEY (source_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE dataset_gaia.dr1
  OWNER TO trillian_admin;
COMMENT ON COLUMN dataset_gaia.dr1.solution_id IS 'Solution Identifier';
COMMENT ON COLUMN dataset_gaia.dr1.source_id IS 'Unique source identifier';
COMMENT ON COLUMN dataset_gaia.dr1.random_index IS 'Random index used to select subsets';
COMMENT ON COLUMN dataset_gaia.dr1.ref_epoch IS 'Reference epoch (Julian Year)';
COMMENT ON COLUMN dataset_gaia.dr1.ra IS 'Right ascension (deg)';
COMMENT ON COLUMN dataset_gaia.dr1.ra_error IS 'Standard error of right ascension (mas)';
COMMENT ON COLUMN dataset_gaia.dr1."dec" IS 'Declination (deg)';
COMMENT ON COLUMN dataset_gaia.dr1.dec_error IS 'Standard error of declination (mas)';
COMMENT ON COLUMN dataset_gaia.dr1.parallax IS 'Parallax (mas)';
COMMENT ON COLUMN dataset_gaia.dr1.parallax_error IS 'Standard error of parallax (mas)';
COMMENT ON COLUMN dataset_gaia.dr1.pmra IS 'Proper motion in right ascension direction (mas/year)';
COMMENT ON COLUMN dataset_gaia.dr1.pmra_error IS 'Standard error of proper motion in right ascension direction (mas/year)';
COMMENT ON COLUMN dataset_gaia.dr1.pmdec IS 'Proper motion in declination direction (mas/year)';
COMMENT ON COLUMN dataset_gaia.dr1.pmdec_error IS 'Standard error of proper motion in declination direction (mas/year)';
COMMENT ON COLUMN dataset_gaia.dr1.ra_dec_corr IS 'Correlation between right ascension and declination';
COMMENT ON COLUMN dataset_gaia.dr1.ra_parallax_corr IS 'Correlation between right ascension and parallax';
COMMENT ON COLUMN dataset_gaia.dr1.ra_pmra_corr IS 'Correlation between right ascension and p.m. in r.a.';
COMMENT ON COLUMN dataset_gaia.dr1.ra_pmdec_corr IS 'Correlation between right ascension and p.m. in declination';
COMMENT ON COLUMN dataset_gaia.dr1.dec_parallax_corr IS 'Correlation between declination and parallax';
COMMENT ON COLUMN dataset_gaia.dr1.dec_pmra_corr IS 'Correlation between declination and p.m. in right ascension';
COMMENT ON COLUMN dataset_gaia.dr1.dec_pmdec_corr IS 'Correlation between declination and p.m. in declination';
COMMENT ON COLUMN dataset_gaia.dr1.parallax_pmra_corr IS 'Correlation between parallax and p.m. in right ascension';
COMMENT ON COLUMN dataset_gaia.dr1.parallax_pmdec_corr IS 'Correlation between parallax and p.m. in declination';
COMMENT ON COLUMN dataset_gaia.dr1.pmra_pmdec_corr IS 'Correlation between p.m. in r.a. and p.m. in declination';
COMMENT ON COLUMN dataset_gaia.dr1.astrometric_n_obs_al IS 'Total number of observations AL';
COMMENT ON COLUMN dataset_gaia.dr1.astrometric_n_obs_ac IS 'Total number of observations AC';
COMMENT ON COLUMN dataset_gaia.dr1.astrometric_n_good_obs_al IS 'Number of good observations AL';
COMMENT ON COLUMN dataset_gaia.dr1.astrometric_n_good_obs_ac IS 'Number of good observations AC';
COMMENT ON COLUMN dataset_gaia.dr1.astrometric_n_bad_obs_al IS 'Number of bad observations AL';
COMMENT ON COLUMN dataset_gaia.dr1.astrometric_n_bad_obs_ac IS 'Number of bad observations AC';
COMMENT ON COLUMN dataset_gaia.dr1.astrometric_delta_q IS 'Hipparcos/Gaia discrepancy (Hipparcos TGAS subset only)';
COMMENT ON COLUMN dataset_gaia.dr1.astrometric_excess_noise IS 'Excess noise of the source (mas)';
COMMENT ON COLUMN dataset_gaia.dr1.astrometric_excess_noise_sig IS 'Significance of excess noise';
COMMENT ON COLUMN dataset_gaia.dr1.astrometric_primary_flag IS 'Primary or seconday';
COMMENT ON COLUMN dataset_gaia.dr1.astrometric_relegation_factor IS 'Relegation factor';
COMMENT ON COLUMN dataset_gaia.dr1.astrometric_weight_al IS 'Mean astrometric weight of the source (mas^−2)';
COMMENT ON COLUMN dataset_gaia.dr1.astrometric_weight_ac IS 'Mean astrometric weight of the source (mas^−2)';
COMMENT ON COLUMN dataset_gaia.dr1.astrometric_priors_used IS 'Type of prior used in in the astrometric solution';
COMMENT ON COLUMN dataset_gaia.dr1.matched_observations IS 'Amount of observations matched to this source';
COMMENT ON COLUMN dataset_gaia.dr1.duplicated_source IS 'Source with duplicate sources';
COMMENT ON COLUMN dataset_gaia.dr1.scan_direction_strength_k1 IS 'Degree of concentration of scan directions across the source';
COMMENT ON COLUMN dataset_gaia.dr1.scan_direction_strength_k2 IS 'Degree of concentration of scan directions across the source';
COMMENT ON COLUMN dataset_gaia.dr1.scan_direction_strength_k3 IS 'Degree of concentration of scan directions across the source';
COMMENT ON COLUMN dataset_gaia.dr1.scan_direction_strength_k4 IS 'Degree of concentration of scan directions across the source';
COMMENT ON COLUMN dataset_gaia.dr1.scan_direction_mean_k1 IS 'Mean position angle of scan directions across the source (deg)';
COMMENT ON COLUMN dataset_gaia.dr1.scan_direction_mean_k2 IS 'Mean position angle of scan directions across the source (deg)';
COMMENT ON COLUMN dataset_gaia.dr1.scan_direction_mean_k3 IS 'Mean position angle of scan directions across the source (deg)';
COMMENT ON COLUMN dataset_gaia.dr1.scan_direction_mean_k4 IS 'Mean position angle of scan directions across the source (deg)';
COMMENT ON COLUMN dataset_gaia.dr1.phot_g_n_obs IS 'Number of observations contributing to G photometry';
COMMENT ON COLUMN dataset_gaia.dr1.phot_g_mean_flux IS 'G band mean flux (e^−1 s^−1)';
COMMENT ON COLUMN dataset_gaia.dr1.phot_g_mean_flux_error IS 'Error on G band mean flux (e^−1 s^−1)';
COMMENT ON COLUMN dataset_gaia.dr1.phot_g_mean_mag IS 'G band mean magnitude (mag)';
COMMENT ON COLUMN dataset_gaia.dr1.phot_variable_flag IS 'Photometric variability flag';
COMMENT ON COLUMN dataset_gaia.dr1.l IS 'Galactic longitude (deg)';
COMMENT ON COLUMN dataset_gaia.dr1.b IS 'Galactic latitude (deg)';
COMMENT ON COLUMN dataset_gaia.dr1.ecl_lon IS 'Ecliptic longitude (deg)';
COMMENT ON COLUMN dataset_gaia.dr1.ecl_lat IS 'Ecliptic latitude (deg)';


-- Index: dataset_gaia.q3c_gaia_dr1_main_idx

-- DROP INDEX dataset_gaia.q3c_gaia_dr1_main_idx;

CREATE INDEX q3c_gaia_dr1_main_idx
  ON dataset_gaia.dr1
  USING btree
  (q3c_ang2ipix(ra::double precision, "dec"::double precision));

