CREATE TABLE dataset_other.tycho2
(
--  id serial NOT NULL, --primary key -- add after import
  tycho2_id character varying(12) NOT NULL,
  p_flag character varying(1), --mean position flag "P", "X"=no mean position, no proper motion
  m_ra numeric, --ra, mean position, ICRS J2000, unit=degrees
  m_dec numeric, --dec, mean position, ICRS J2000, unit=degrees
  pm_ra numeric, --proper motion RA, ISRC at J2000, unit=mas/yr
  pm_dec numeric, --proper motion dec, ISRC at J2000, unit=mas/yr
  e_m_ra smallint, --(model-based) RA error at mean epoch, unit=mas
  e_m_dec smallint, --(model-based) dec error at mean epoch, unit=mas
  e_pm_ra numeric, --(model-based) proper motion RA error, unit=mas/yr
  e_pm_dec numeric, --(model-based) proper motion dec error, unit=mas/yr
  mep_ra numeric, --mean epoch of ra, unit=yr
  mep_dec numeric, --mean epoch of dec, unit=yr
  n_upos smallint, --number of positions used
  g_m_ra numeric, --goodness of fit for mean RA
  g_m_dec numeric, --goodness of fit for mean dec
  g_pm_ra numeric, --goodness of fit for mean RA proper motion
  g_pm_dec numeric, --goodness of fit for mean dec proper motion
  bt_mag numeric, --Tycho-2 B_T magnitude, unit=mag
  e_bt_mag numeric, --error of Tycho 2 B_T magnitude, unit=mag
  vt_mag numeric, --Tycho-2 V_T magnitude, unit=mag
  e_vt_mag numeric, --error of Tycho 2 B_T magnitude, unit=mag
  prox smallint NOT NULL, --proximity indicator
  tycho1_flag character varying(1), --Tycho-1 star flag
  hip_id text, --Hipparcos number
  ccdm_hip character varying(3), --CCDM component identifier for HIP stars
  ra numeric NOT NULL, --observed Tycho2- position, ICRS, ra, unit=degrees
  "dec" numeric NOT NULL, --observed Tycho2- position, ICRS, dec, unit=degrees
  ep_ra numeric NOT NULL, --epoch-1990 of observed Tycho-2 position, ra, unit=a
  ep_dec numeric NOT NULL, --epoch-1990 of observed Tycho-2 position, dec, unit=a
  e_ra numeric NOT NULL, --model-based sigma, ra, observed position, unit=mas
  e_dec numeric NOT NULL, --model-based sigma, dec, observed position, unit=mas
  pos_flag character varying(1), --position flag, "D"=double star treatment, "P"=photo-center treatment
  corr numeric NOT NULL --correlation, observed position
);

COMMENT ON COLUMN dataset_other.tycho2.p_flag IS 'mean position flag "P", "X"=no mean position, no proper motion';
COMMENT ON COLUMN dataset_other.tycho2.m_ra IS 'ra, mean position, ICRS J2000, unit=degrees';
COMMENT ON COLUMN dataset_other.tycho2.m_dec IS 'dec, mean position, ICRS J2000, unit=degrees';
COMMENT ON COLUMN dataset_other.tycho2.pm_ra IS 'proper motion RA, ISRC at J2000, unit=mas/yr';
COMMENT ON COLUMN dataset_other.tycho2.pm_dec IS 'proper motion dec, ISRC at J2000, unit=mas/yr';
COMMENT ON COLUMN dataset_other.tycho2.e_m_ra IS '(model-based) RA error at mean epoch, unit=mas';
COMMENT ON COLUMN dataset_other.tycho2.e_m_dec IS '(model-based) dec error at mean epoch, unit=mas';
COMMENT ON COLUMN dataset_other.tycho2.e_pm_ra IS '(model-based) proper motion RA error, unit=mas/yr';
COMMENT ON COLUMN dataset_other.tycho2.e_pm_dec IS '(model-based) proper motion dec error, unit=mas/yr';
COMMENT ON COLUMN dataset_other.tycho2.mep_ra IS 'mean epoch of ra, unit=yr';
COMMENT ON COLUMN dataset_other.tycho2.mep_dec IS 'mean epoch of dec, unit=yr';
COMMENT ON COLUMN dataset_other.tycho2.n_upos IS 'number of positions used';
COMMENT ON COLUMN dataset_other.tycho2.g_m_ra IS 'goodness of fit for mean RA';
COMMENT ON COLUMN dataset_other.tycho2.g_m_dec IS 'goodness of fit for mean dec';
COMMENT ON COLUMN dataset_other.tycho2.g_pm_ra IS 'goodness of fit for mean RA proper motion';
COMMENT ON COLUMN dataset_other.tycho2.g_pm_dec IS 'goodness of fit for mean dec proper motion';
COMMENT ON COLUMN dataset_other.tycho2.bt_mag IS 'Tycho-2 B_T magnitude, unit=mag';
COMMENT ON COLUMN dataset_other.tycho2.e_bt_mag IS 'error of Tycho 2 B_T magnitude, unit=mag';
COMMENT ON COLUMN dataset_other.tycho2.vt_mag IS 'Tycho-2 V_T magnitude, unit=mag';
COMMENT ON COLUMN dataset_other.tycho2.e_vt_mag IS 'error of Tycho 2 B_T magnitude, unit=mag';
COMMENT ON COLUMN dataset_other.tycho2.prox IS 'proximity indicator';
COMMENT ON COLUMN dataset_other.tycho2.tycho1_flag IS 'Tycho-1 star flag';
COMMENT ON COLUMN dataset_other.tycho2.hip_id IS 'Hipparcos number';
COMMENT ON COLUMN dataset_other.tycho2.ccdm_hip IS 'CCDM component identifier for HIP stars';
COMMENT ON COLUMN dataset_other.tycho2.ra IS 'observed Tycho2- position, ICRS, ra, unit=degrees';
COMMENT ON COLUMN dataset_other.tycho2.dec IS 'observed Tycho2- position, ICRS, dec, unit=degrees';
COMMENT ON COLUMN dataset_other.tycho2.ep_ra IS 'epoch-1990 of observed Tycho-2 position, ra, unit=a';
COMMENT ON COLUMN dataset_other.tycho2.ep_dec IS 'epoch-1990 of observed Tycho-2 position, dec, unit=a';
COMMENT ON COLUMN dataset_other.tycho2.e_ra IS 'model-based sigma, ra, observed position, unit=mas';
COMMENT ON COLUMN dataset_other.tycho2.e_dec IS 'model-based sigma, dec, observed position, unit=mas';
COMMENT ON COLUMN dataset_other.tycho2.pos_flag IS 'position flag, "D"=double star treatment, "P"=photo-center treatment';
COMMENT ON COLUMN dataset_other.tycho2.corr IS 'correlation, observed position';

-- add after import
CREATE SEQUENCE dataset_other.tycho2_pk_seq;

-- add primary key
ALTER TABLE dataset_other.tycho2
  ADD COLUMN pk integer NOT NULL DEFAULT nextval('dataset_other.tycho2_pk_seq');
COMMENT ON COLUMN datasets.pk IS 'primary key';
ALTER TABLE dataset_other.tycho2 ADD CONSTRAINT tycho2_pk PRIMARY KEY (pk);

-- other constraints
ALTER TABLE dataset_other.tycho2 ADD CONSTRAINT tycho2_id_uniq UNIQUE (tycho2_id);

-- indices
CREATE INDEX tycho2_bt_mag_idx ON dataset_other.tycho2 USING btree (bt_mag);
CREATE INDEX tycho2_vt_mag_idx ON dataset_other.tycho2 USING btree (vt_mag);
CREATE INDEX tycho2_m_ra_idx ON dataset_other.tycho2 USING btree (m_ra);
CREATE INDEX tycho2_m_dec_idx ON dataset_other.tycho2 USING btree (m_dec);
CREATE INDEX tycho2_pm_ra_idx ON dataset_other.tycho2 USING btree (pm_ra);
CREATE INDEX tycho2_pm_dec_idx ON dataset_other.tycho2 USING btree (pm_dec);
