--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.4
-- Dumped by pg_dump version 9.4.0
-- Started on 2015-02-25 11:07:25 EST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'LATIN1';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 7 (class 2615 OID 16509)
-- Name: dataset_sdss_dr12; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA dataset_sdss_dr14;


SET search_path = dataset_sdss_dr14, pg_catalog;

SET default_with_oids = false;

--
-- TOC entry 195 (class 1259 OID 16721)
-- Name: field; Type: TABLE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE TABLE field (
    pk integer NOT NULL,
    fieldid text,
    camcol bigint,
    field bigint,
    ntotal integer,
    nobjects integer,
    nchild integer,
    ngals integer,
    nstars integer,
    ncr integer[],
    nbrightobj integer[],
    nfaintobj integer[],
    quality bigint,
    mjd numeric[],
    a numeric[],
    b numeric[],
    c numeric[],
    d numeric[],
    e numeric[],
    ff numeric[],
    drow0 numeric[],
    drow1 numeric[],
    drow2 numeric[],
    drow3 numeric[],
    dcol0 numeric[],
    dcol1 numeric[],
    dcol2 numeric[],
    dcol3 numeric[],
    csrow numeric[],
    cscol numeric[],
    ccrow numeric[],
    cccol numeric[],
    ricut numeric[],
    airmass numeric[],
    muerr numeric[],
    nuerr numeric[],
    pixscale numeric[],
    ra numeric,
    "dec" numeric,
    cx numeric,
    cy numeric,
    cz numeric,
    ramin numeric,
    ramax numeric,
    decmin numeric,
    decmax numeric,
    primaryarea numeric,
    rowoffset numeric[],
    coloffset numeric[],
    saturation_level bigint[],
    neff_psf numeric[],
    sky_psp numeric[],
    sky_frames numeric[],
    sky_frames_sub numeric[],
    sigpix numeric[],
    dev_ap_correction numeric[],
    dev_ap_correctionerr numeric[],
    exp_ap_correction numeric[],
    exp_ap_correctionerr numeric[],
    dev_model_ap_correction numeric[],
    dev_model_ap_correctionerr numeric[],
    exp_model_ap_correction numeric[],
    exp_model_ap_correctionerr numeric[],
    median_fibercolor numeric[],
    median_psfcolor numeric[],
    q numeric[],
    u numeric[],
    sky numeric[],
    skysig numeric[],
    skyerr numeric[],
    skyslope numeric[],
    lbias numeric[],
    rbias numeric[],
    psf_nstar bigint[],
    psf_ap_correctionerr numeric[],
    psf_sigma1 numeric[],
    psf_sigma2 numeric[],
    psf_b numeric[],
    psf_p0 numeric[],
    psf_beta numeric[],
    psf_sigmap numeric[],
    psf_width numeric[],
    psf_psfcounts numeric[],
    psf_sigma1_2g numeric[],
    psf_sigma2_2g numeric[],
    psf_b_2g numeric[],
    psfcounts numeric[],
    prof_nprof bigint[],
    prof_mean_nmgy numeric[],
    prof_med_nmgy numeric[],
    prof_sig_nmgy numeric[],
    gain numeric[],
    dark_variance numeric[],
    score numeric,
    aterm numeric[],
    kterm numeric[],
    kdot numeric[],
    ref_tai numeric[],
    tai numeric[],
    psp_status bigint,
    photo_status bigint,
    image_status bigint[],
    calib_status bigint[],
    nstars_offset bigint[],
    field_offset numeric[],
    nmgypercount numeric[],
    nmgypercount_ivar numeric[],
    ifield bigint,
    mu_start numeric,
    mu_end numeric,
    nu_start numeric,
    nu_end numeric,
    ifindx bigint,
    nbalkan bigint,
    contains_primary_polygon boolean,
    filename text,
    run_pk integer
);


--
-- TOC entry 4037 (class 0 OID 0)
-- Dependencies: 195
-- Name: TABLE field; Type: COMMENT; Schema: dataset_sdss_dr12; Owner: -
--

COMMENT ON TABLE field IS 'http://data.sdss3.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/photoField.html';


--
-- TOC entry 4038 (class 0 OID 0)
-- Dependencies: 195
-- Name: COLUMN field.fieldid; Type: COMMENT; Schema: dataset_sdss_dr12; Owner: -
--

COMMENT ON COLUMN field.fieldid IS 'this is the (text string) field id';


--
-- TOC entry 4039 (class 0 OID 0)
-- Dependencies: 195
-- Name: COLUMN field.field; Type: COMMENT; Schema: dataset_sdss_dr12; Owner: -
--

COMMENT ON COLUMN field.field IS 'this is the SDSS field number';


--
-- TOC entry 4040 (class 0 OID 0)
-- Dependencies: 195
-- Name: COLUMN field.contains_primary_polygon; Type: COMMENT; Schema: dataset_sdss_dr12; Owner: -
--

COMMENT ON COLUMN field.contains_primary_polygon IS 'flag to indicate whether this field contains a polygon that is marked as primary';


--
-- TOC entry 194 (class 1259 OID 16719)
-- Name: field_pk_seq; Type: SEQUENCE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE SEQUENCE field_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4041 (class 0 OID 0)
-- Dependencies: 194
-- Name: field_pk_seq; Type: SEQUENCE OWNED BY; Schema: dataset_sdss_dr12; Owner: -
--

ALTER SEQUENCE field_pk_seq OWNED BY field.pk;


--
-- TOC entry 205 (class 1259 OID 141923040)
-- Name: field_to_flag; Type: TABLE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE TABLE field_to_flag (
    field_pk integer NOT NULL,
    flag_value_pk integer NOT NULL
);


--
-- TOC entry 201 (class 1259 OID 141922990)
-- Name: flag_type; Type: TABLE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE TABLE flag_type (
    pk integer NOT NULL,
    label text NOT NULL,
    data_type smallint NOT NULL,
    description text NOT NULL
);


--
-- TOC entry 4042 (class 0 OID 0)
-- Dependencies: 201
-- Name: TABLE flag_type; Type: COMMENT; Schema: dataset_sdss_dr12; Owner: -
--

COMMENT ON TABLE flag_type IS 'Image status: http://www.sdss3.org/dr10/algorithms/bitmask_image_status.php
Calibration status: http://www.sdss3.org/dr10/algorithms/bitmask_calib_status.php
Resolve status: http://www.sdss3.org/dr10/algorithms/bitmask_resolve_status.php
OBJECT1/OBJECT2/OBJECT_TYPE enums: http://data.sdss3.org/datamodel/files/PHOTO_REDUX/RERUN/RUN/objcs/CAMCOL/fpObjc.html';


--
-- TOC entry 200 (class 1259 OID 141922988)
-- Name: flag_type_pk_seq; Type: SEQUENCE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE SEQUENCE flag_type_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4043 (class 0 OID 0)
-- Dependencies: 200
-- Name: flag_type_pk_seq; Type: SEQUENCE OWNED BY; Schema: dataset_sdss_dr12; Owner: -
--

ALTER SEQUENCE flag_type_pk_seq OWNED BY flag_type.pk;


--
-- TOC entry 203 (class 1259 OID 141923001)
-- Name: flag_value; Type: TABLE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE TABLE flag_value (
    pk integer NOT NULL,
    label text NOT NULL,
    description text NOT NULL,
    "bit" integer NOT NULL,
    flag_type_pk smallint NOT NULL,
    value bigint
);


--
-- TOC entry 202 (class 1259 OID 141922999)
-- Name: flag_value_pk_seq; Type: SEQUENCE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE SEQUENCE flag_value_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4044 (class 0 OID 0)
-- Dependencies: 202
-- Name: flag_value_pk_seq; Type: SEQUENCE OWNED BY; Schema: dataset_sdss_dr12; Owner: -
--

ALTER SEQUENCE flag_value_pk_seq OWNED BY flag_value.pk;


--
-- TOC entry 186 (class 1259 OID 16512)
-- Name: object_type; Type: TABLE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE TABLE object_type (
    pk integer NOT NULL,
    value smallint,
    label text,
    short_label text
);


--
-- TOC entry 4045 (class 0 OID 0)
-- Dependencies: 186
-- Name: TABLE object_type; Type: COMMENT; Schema: dataset_sdss_dr12; Owner: -
--

COMMENT ON TABLE object_type IS 'Object type is an enum value.
Ref: http://data.sdss3.org/datamodel/files/PHOTO_REDUX/RERUN/RUN/objcs/CAMCOL/fpObjc.html';


--
-- TOC entry 185 (class 1259 OID 16510)
-- Name: object_type_id_seq; Type: SEQUENCE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE SEQUENCE object_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4046 (class 0 OID 0)
-- Dependencies: 185
-- Name: object_type_id_seq; Type: SEQUENCE OWNED BY; Schema: dataset_sdss_dr12; Owner: -
--

ALTER SEQUENCE object_type_id_seq OWNED BY object_type.pk;


--
-- TOC entry 199 (class 1259 OID 141922981)
-- Name: photo_flag; Type: TABLE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE TABLE photo_flag (
    pk integer NOT NULL,
    label text,
    value bigint,
    comment text,
    short_label text,
    "bit" smallint
);


--
-- TOC entry 198 (class 1259 OID 141922979)
-- Name: photo_flag_pk_seq; Type: SEQUENCE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE SEQUENCE photo_flag_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4047 (class 0 OID 0)
-- Dependencies: 198
-- Name: photo_flag_pk_seq; Type: SEQUENCE OWNED BY; Schema: dataset_sdss_dr12; Owner: -
--

ALTER SEQUENCE photo_flag_pk_seq OWNED BY photo_flag.pk;


--
-- TOC entry 190 (class 1259 OID 16631)
-- Name: photoobj; Type: TABLE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE TABLE photoobj (
    pk bigint NOT NULL,
    parent_photoobj_pk bigint,
    field_pk integer,
    objid bigint,
    mode smallint,
    clean smallint,
    id integer,
    objc_type smallint,
    objc_prob_psf smallint,
    objc_flags integer,
    objc_flags2 integer,
    objc_rowc numeric,
    objc_rowcerr numeric,
    objc_colc numeric,
    objc_colcerr numeric,
    rowvdeg numeric,
    rowvdegerr numeric,
    colvdeg numeric,
    colvdegerr numeric,
    rowc numeric[],
    rowcerr numeric[],
    colc numeric[],
    colcerr numeric[],
    petrotheta numeric[],
    petrothetaerr numeric[],
    petroth50 numeric[],
    petroth50err numeric[],
    petroth90 numeric[],
    petroth90err numeric[],
    q numeric[],
    qerr numeric[],
    u numeric[],
    uerr numeric[],
    m_e1 numeric[],
    m_e2 numeric[],
    m_e1e1err numeric[],
    m_e1e2err numeric[],
    m_e2e2err numeric[],
    m_rr_cc numeric[],
    m_rr_ccerr numeric[],
    m_cr4 numeric[],
    m_e1_psf numeric[],
    m_e2_psf numeric[],
    m_rr_cc_psf numeric[],
    m_cr4_psf numeric[],
    theta_dev numeric[],
    theta_deverr numeric[],
    ab_dev numeric[],
    ab_deverr numeric[],
    theta_exp numeric[],
    theta_experr numeric[],
    ab_exp numeric[],
    ab_experr numeric[],
    fracdev numeric[],
    photo_flags bigint[],
    photo_flags2 bigint[],
    type bigint[],
    prob_psf numeric[],
    nprof bigint[],
    profmean_nmgy numeric[],
    proferr_nmgy numeric[],
    star_lnl numeric[],
    exp_lnl numeric[],
    dev_lnl numeric[],
    psp_status bigint[],
    pixscale numeric[],
    ra numeric,
    "dec" numeric,
    cx numeric,
    cy numeric,
    cz numeric,
    raerr numeric,
    decerr numeric,
    l numeric,
    b numeric,
    offsetra numeric[],
    offsetdec numeric[],
    psf_fwhm numeric[],
    airmass numeric[],
    phi_offset numeric[],
    phi_dev_deg numeric[],
    phi_exp_deg numeric[],
    extinction numeric[],
    skyflux numeric[],
    skyflux_ivar numeric[],
    psfflux numeric[],
    psfflux_ivar numeric[],
    psfmag numeric[],
    psfmagerr numeric[],
    fiberflux numeric[],
    fiberflux_ivar numeric[],
    fibermag numeric[],
    fibermagerr numeric[],
    fiber2flux numeric[],
    fiber2flux_ivar numeric[],
    fiber2mag numeric[],
    fiber2magerr numeric[],
    cmodelflux numeric[],
    cmodelflux_ivar numeric[],
    cmodelmag numeric[],
    cmodelmagerr numeric[],
    modelflux numeric[],
    modelflux_ivar numeric[],
    modelmag numeric[],
    modelmagerr numeric[],
    petroflux numeric[],
    petroflux_ivar numeric[],
    petromag numeric[],
    petromagerr numeric[],
    devflux numeric[],
    devflux_ivar numeric[],
    devmag numeric[],
    devmagerr numeric[],
    expflux numeric[],
    expflux_ivar numeric[],
    expmag numeric[],
    expmagerr numeric[],
    aperflux numeric[],
    aperflux_ivar numeric[],
    cloudcam smallint[],
    calib_status smallint[],
    nmgypercount numeric[],
    nmgypercount_ivar numeric[],
    tai numeric[],
    balkan_id bigint,
    nobserve integer,
    ndetect integer,
    nedge integer,
    object_type_pk smallint
);


--
-- TOC entry 4048 (class 0 OID 0)
-- Dependencies: 190
-- Name: TABLE photoobj; Type: COMMENT; Schema: dataset_sdss_dr12; Owner: -
--

COMMENT ON TABLE photoobj IS 'Ref: http://data.sdss3.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html';


--
-- TOC entry 4049 (class 0 OID 0)
-- Dependencies: 190
-- Name: COLUMN photoobj.objc_flags; Type: COMMENT; Schema: dataset_sdss_dr12; Owner: -
--

COMMENT ON COLUMN photoobj.objc_flags IS '32-bit integer bitmask';


--
-- TOC entry 4050 (class 0 OID 0)
-- Dependencies: 190
-- Name: COLUMN photoobj.objc_flags2; Type: COMMENT; Schema: dataset_sdss_dr12; Owner: -
--

COMMENT ON COLUMN photoobj.objc_flags2 IS '32-bit integer bitmask';


--
-- TOC entry 4051 (class 0 OID 0)
-- Dependencies: 190
-- Name: COLUMN photoobj.photo_flags; Type: COMMENT; Schema: dataset_sdss_dr12; Owner: -
--

COMMENT ON COLUMN photoobj.photo_flags IS 'http://www.sdss3.org/dr10/algorithms/bitmask_flags1.php';


--
-- TOC entry 4052 (class 0 OID 0)
-- Dependencies: 190
-- Name: COLUMN photoobj.photo_flags2; Type: COMMENT; Schema: dataset_sdss_dr12; Owner: -
--

COMMENT ON COLUMN photoobj.photo_flags2 IS 'http://www.sdss3.org/dr10/algorithms/bitmask_flags2.php';


--
-- TOC entry 208 (class 1259 OID 635785333)
-- Name: photoobj2; Type: TABLE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE TABLE photoobj2 (
    pk bigint NOT NULL,
    parent_photoobj_pk bigint,
    field_pk integer,
    objid bigint,
    mode smallint,
    clean smallint,
    id integer,
    objc_type smallint,
    objc_prob_psf smallint,
    objc_flags integer,
    objc_flags2 integer,
    objc_rowc numeric,
    objc_rowcerr numeric,
    objc_colc numeric,
    objc_colcerr numeric,
    rowvdeg numeric,
    rowvdegerr numeric,
    colvdeg numeric,
    colvdegerr numeric,
    rowc numeric[],
    rowcerr numeric[],
    colc numeric[],
    colcerr numeric[],
    petrotheta numeric[],
    petrothetaerr numeric[],
    petroth50 numeric[],
    petroth50err numeric[],
    petroth90 numeric[],
    petroth90err numeric[],
    q numeric[],
    qerr numeric[],
    u numeric[],
    uerr numeric[],
    m_e1 numeric[],
    m_e2 numeric[],
    m_e1e1err numeric[],
    m_e1e2err numeric[],
    m_e2e2err numeric[],
    m_rr_cc numeric[],
    m_rr_ccerr numeric[],
    m_cr4 numeric[],
    m_e1_psf numeric[],
    m_e2_psf numeric[],
    m_rr_cc_psf numeric[],
    m_cr4_psf numeric[],
    theta_dev numeric[],
    theta_deverr numeric[],
    ab_dev numeric[],
    ab_deverr numeric[],
    theta_exp numeric[],
    theta_experr numeric[],
    ab_exp numeric[],
    ab_experr numeric[],
    fracdev numeric[],
    photo_flags bigint[],
    photo_flags2 bigint[],
    type bigint[],
    prob_psf numeric[],
    nprof bigint[],
    profmean_nmgy numeric[],
    proferr_nmgy numeric[],
    star_lnl numeric[],
    exp_lnl numeric[],
    dev_lnl numeric[],
    psp_status bigint[],
    pixscale numeric[],
    ra numeric,
    "dec" numeric,
    cx numeric,
    cy numeric,
    cz numeric,
    raerr numeric,
    decerr numeric,
    l numeric,
    b numeric,
    offsetra numeric[],
    offsetdec numeric[],
    psf_fwhm numeric[],
    airmass numeric[],
    phi_offset numeric[],
    phi_dev_deg numeric[],
    phi_exp_deg numeric[],
    extinction numeric[],
    skyflux numeric[],
    skyflux_ivar numeric[],
    psfflux numeric[],
    psfflux_ivar numeric[],
    psfmag numeric[],
    psfmagerr numeric[],
    fiberflux numeric[],
    fiberflux_ivar numeric[],
    fibermag numeric[],
    fibermagerr numeric[],
    fiber2flux numeric[],
    fiber2flux_ivar numeric[],
    fiber2mag numeric[],
    fiber2magerr numeric[],
    cmodelflux numeric[],
    cmodelflux_ivar numeric[],
    cmodelmag numeric[],
    cmodelmagerr numeric[],
    modelflux numeric[],
    modelflux_ivar numeric[],
    modelmag numeric[],
    modelmagerr numeric[],
    petroflux numeric[],
    petroflux_ivar numeric[],
    petromag numeric[],
    petromagerr numeric[],
    devflux numeric[],
    devflux_ivar numeric[],
    devmag numeric[],
    devmagerr numeric[],
    expflux numeric[],
    expflux_ivar numeric[],
    expmag numeric[],
    expmagerr numeric[],
    aperflux numeric[],
    aperflux_ivar numeric[],
    cloudcam smallint[],
    calib_status smallint[],
    nmgypercount numeric[],
    nmgypercount_ivar numeric[],
    tai numeric[],
    balkan_id bigint,
    nobserve integer,
    ndetect integer,
    nedge integer,
    object_type_pk smallint
);


--
-- TOC entry 207 (class 1259 OID 635785331)
-- Name: photoobj2_pk_seq; Type: SEQUENCE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE SEQUENCE photoobj2_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4053 (class 0 OID 0)
-- Dependencies: 207
-- Name: photoobj2_pk_seq; Type: SEQUENCE OWNED BY; Schema: dataset_sdss_dr12; Owner: -
--

ALTER SEQUENCE photoobj2_pk_seq OWNED BY photoobj2.pk;


--
-- TOC entry 189 (class 1259 OID 16629)
-- Name: photoobj_pk_seq; Type: SEQUENCE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE SEQUENCE photoobj_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4054 (class 0 OID 0)
-- Dependencies: 189
-- Name: photoobj_pk_seq; Type: SEQUENCE OWNED BY; Schema: dataset_sdss_dr12; Owner: -
--

ALTER SEQUENCE photoobj_pk_seq OWNED BY photoobj.pk;


--
-- TOC entry 204 (class 1259 OID 141923025)
-- Name: photoobj_to_flag; Type: TABLE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE TABLE photoobj_to_flag (
    photoobj_pk bigint NOT NULL,
    flag_value_pk integer NOT NULL,
    filter character(1),
    pk bigint NOT NULL
);


--
-- TOC entry 206 (class 1259 OID 141923560)
-- Name: photoobj_to_flag_pk_seq; Type: SEQUENCE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE SEQUENCE photoobj_to_flag_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4055 (class 0 OID 0)
-- Dependencies: 206
-- Name: photoobj_to_flag_pk_seq; Type: SEQUENCE OWNED BY; Schema: dataset_sdss_dr12; Owner: -
--

ALTER SEQUENCE photoobj_to_flag_pk_seq OWNED BY photoobj_to_flag.pk;


--
-- TOC entry 193 (class 1259 OID 16663)
-- Name: photoobj_to_thing; Type: TABLE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE TABLE photoobj_to_thing (
    photoobj_pk bigint NOT NULL,
    thing_pk bigint NOT NULL
);


--
-- TOC entry 197 (class 1259 OID 71339797)
-- Name: run; Type: TABLE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE TABLE run (
    pk integer NOT NULL,
    filename text,
    skyversion smallint,
    run bigint,
    rerun character varying(3),
    mjd bigint,
    datestring character varying(10),
    stripe bigint,
    strip text,
    xbore numeric,
    field_ref bigint,
    lastfield bigint,
    flavor character varying(7),
    xbin bigint,
    ybin bigint,
    nrow bigint,
    mjd_ref numeric,
    mu_ref numeric,
    linestart bigint,
    tracking numeric,
    node numeric,
    incl numeric,
    comments text,
    qterm numeric,
    maxmuresid numeric,
    maxnuresid numeric,
    startfield bigint,
    endfield bigint,
    photo_version character varying(8),
    dervish_version character varying(11),
    astrom_version character varying(11),
    sas_version character varying(5)
);


--
-- TOC entry 196 (class 1259 OID 71339795)
-- Name: run_pk_seq; Type: SEQUENCE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE SEQUENCE run_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4056 (class 0 OID 0)
-- Dependencies: 196
-- Name: run_pk_seq; Type: SEQUENCE OWNED BY; Schema: dataset_sdss_dr12; Owner: -
--

ALTER SEQUENCE run_pk_seq OWNED BY run.pk;


--
-- TOC entry 192 (class 1259 OID 16642)
-- Name: thing; Type: TABLE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE TABLE thing (
    pk bigint NOT NULL,
    thing_id bigint
);


--
-- TOC entry 191 (class 1259 OID 16640)
-- Name: thing_pk_seq; Type: SEQUENCE; Schema: dataset_sdss_dr12; Owner: -
--

CREATE SEQUENCE thing_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4057 (class 0 OID 0)
-- Dependencies: 191
-- Name: thing_pk_seq; Type: SEQUENCE OWNED BY; Schema: dataset_sdss_dr12; Owner: -
--

ALTER SEQUENCE thing_pk_seq OWNED BY thing.pk;


--
-- TOC entry 3851 (class 2604 OID 16724)
-- Name: pk; Type: DEFAULT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY field ALTER COLUMN pk SET DEFAULT nextval('field_pk_seq'::regclass);


--
-- TOC entry 3854 (class 2604 OID 141922993)
-- Name: pk; Type: DEFAULT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY flag_type ALTER COLUMN pk SET DEFAULT nextval('flag_type_pk_seq'::regclass);


--
-- TOC entry 3855 (class 2604 OID 141923004)
-- Name: pk; Type: DEFAULT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY flag_value ALTER COLUMN pk SET DEFAULT nextval('flag_value_pk_seq'::regclass);


--
-- TOC entry 3848 (class 2604 OID 16515)
-- Name: pk; Type: DEFAULT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY object_type ALTER COLUMN pk SET DEFAULT nextval('object_type_id_seq'::regclass);


--
-- TOC entry 3853 (class 2604 OID 141922984)
-- Name: pk; Type: DEFAULT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photo_flag ALTER COLUMN pk SET DEFAULT nextval('photo_flag_pk_seq'::regclass);


--
-- TOC entry 3849 (class 2604 OID 16634)
-- Name: pk; Type: DEFAULT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj ALTER COLUMN pk SET DEFAULT nextval('photoobj_pk_seq'::regclass);


--
-- TOC entry 3857 (class 2604 OID 635785336)
-- Name: pk; Type: DEFAULT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj2 ALTER COLUMN pk SET DEFAULT nextval('photoobj2_pk_seq'::regclass);


--
-- TOC entry 3856 (class 2604 OID 141923562)
-- Name: pk; Type: DEFAULT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj_to_flag ALTER COLUMN pk SET DEFAULT nextval('photoobj_to_flag_pk_seq'::regclass);


--
-- TOC entry 3852 (class 2604 OID 71339800)
-- Name: pk; Type: DEFAULT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY run ALTER COLUMN pk SET DEFAULT nextval('run_pk_seq'::regclass);


--
-- TOC entry 3850 (class 2604 OID 16645)
-- Name: pk; Type: DEFAULT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY thing ALTER COLUMN pk SET DEFAULT nextval('thing_pk_seq'::regclass);


--
-- TOC entry 3876 (class 2606 OID 16729)
-- Name: field_pk; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY field
    ADD CONSTRAINT field_pk PRIMARY KEY (pk);


--
-- TOC entry 3895 (class 2606 OID 141923044)
-- Name: field_to_flag_pk; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY field_to_flag
    ADD CONSTRAINT field_to_flag_pk PRIMARY KEY (field_pk, flag_value_pk);


--
-- TOC entry 3887 (class 2606 OID 141922998)
-- Name: flag_type_pkey; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY flag_type
    ADD CONSTRAINT flag_type_pkey PRIMARY KEY (pk);


--
-- TOC entry 3889 (class 2606 OID 141923024)
-- Name: flag_value_pk; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY flag_value
    ADD CONSTRAINT flag_value_pk PRIMARY KEY (pk);


--
-- TOC entry 3859 (class 2606 OID 16520)
-- Name: object_type_pk; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY object_type
    ADD CONSTRAINT object_type_pk PRIMARY KEY (pk);


--
-- TOC entry 3897 (class 2606 OID 635785343)
-- Name: objid2_uniq; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj2
    ADD CONSTRAINT objid2_uniq UNIQUE (objid);


--
-- TOC entry 3863 (class 2606 OID 18300)
-- Name: objid_uniq; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj
    ADD CONSTRAINT objid_uniq UNIQUE (objid);


--
-- TOC entry 3899 (class 2606 OID 635785341)
-- Name: photoobj2_pk; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj2
    ADD CONSTRAINT photoobj2_pk PRIMARY KEY (pk);


--
-- TOC entry 3865 (class 2606 OID 16639)
-- Name: photoobj_pk; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj
    ADD CONSTRAINT photoobj_pk PRIMARY KEY (pk);


--
-- TOC entry 3891 (class 2606 OID 141923568)
-- Name: photoobj_to_flag_pk; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj_to_flag
    ADD CONSTRAINT photoobj_to_flag_pk PRIMARY KEY (pk);


--
-- TOC entry 3893 (class 2606 OID 141923559)
-- Name: photoobj_to_flag_uniq; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj_to_flag
    ADD CONSTRAINT photoobj_to_flag_uniq UNIQUE (photoobj_pk, flag_value_pk, filter);


--
-- TOC entry 3871 (class 2606 OID 16667)
-- Name: photoobj_to_thing_pk; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj_to_thing
    ADD CONSTRAINT photoobj_to_thing_pk PRIMARY KEY (photoobj_pk, thing_pk);


--
-- TOC entry 3882 (class 2606 OID 71339805)
-- Name: run_pk; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY run
    ADD CONSTRAINT run_pk PRIMARY KEY (pk);


--
-- TOC entry 3867 (class 2606 OID 18310)
-- Name: thing_id_uniq; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY thing
    ADD CONSTRAINT thing_id_uniq UNIQUE (thing_id);


--
-- TOC entry 3869 (class 2606 OID 16647)
-- Name: thing_pk; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY thing
    ADD CONSTRAINT thing_pk PRIMARY KEY (pk);


--
-- TOC entry 3861 (class 2606 OID 18317)
-- Name: value_uniq; Type: CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY object_type
    ADD CONSTRAINT value_uniq UNIQUE (value);


--
-- TOC entry 3872 (class 1259 OID 141922945)
-- Name: field_camcol_idx; Type: INDEX; Schema: dataset_sdss_dr12; Owner: -
--

CREATE INDEX field_camcol_idx ON field USING btree (camcol);


--
-- TOC entry 3873 (class 1259 OID 141922946)
-- Name: field_fieldid_idx; Type: INDEX; Schema: dataset_sdss_dr12; Owner: -
--

CREATE INDEX field_fieldid_idx ON field USING btree (fieldid);


--
-- TOC entry 3874 (class 1259 OID 141922947)
-- Name: field_idx; Type: INDEX; Schema: dataset_sdss_dr12; Owner: -
--

CREATE INDEX field_idx ON field USING btree (field);


--
-- TOC entry 3877 (class 1259 OID 16740)
-- Name: filename_idx; Type: INDEX; Schema: dataset_sdss_dr12; Owner: -
--

CREATE INDEX filename_idx ON field USING btree (filename);


--
-- TOC entry 3878 (class 1259 OID 141922948)
-- Name: mjd_idx; Type: INDEX; Schema: dataset_sdss_dr12; Owner: -
--

CREATE INDEX mjd_idx ON field USING btree (mjd);


--
-- TOC entry 3879 (class 1259 OID 141922949)
-- Name: run_filename_idx; Type: INDEX; Schema: dataset_sdss_dr12; Owner: -
--

CREATE INDEX run_filename_idx ON run USING btree (filename);


--
-- TOC entry 3880 (class 1259 OID 141922952)
-- Name: run_mjd_idx; Type: INDEX; Schema: dataset_sdss_dr12; Owner: -
--

CREATE INDEX run_mjd_idx ON run USING btree (mjd);


--
-- TOC entry 3883 (class 1259 OID 141922951)
-- Name: run_rerun_idx; Type: INDEX; Schema: dataset_sdss_dr12; Owner: -
--

CREATE INDEX run_rerun_idx ON run USING btree (rerun);


--
-- TOC entry 3884 (class 1259 OID 141922950)
-- Name: run_run_idx; Type: INDEX; Schema: dataset_sdss_dr12; Owner: -
--

CREATE INDEX run_run_idx ON run USING btree (run);


--
-- TOC entry 3885 (class 1259 OID 141922953)
-- Name: run_stripe_idx; Type: INDEX; Schema: dataset_sdss_dr12; Owner: -
--

CREATE INDEX run_stripe_idx ON run USING btree (stripe);


--
-- TOC entry 3913 (class 2606 OID 635785344)
-- Name: field2_fk; Type: FK CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj2
    ADD CONSTRAINT field2_fk FOREIGN KEY (field_pk) REFERENCES field(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3902 (class 2606 OID 16735)
-- Name: field_fk; Type: FK CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj
    ADD CONSTRAINT field_fk FOREIGN KEY (field_pk) REFERENCES field(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3909 (class 2606 OID 141923050)
-- Name: field_fk; Type: FK CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY field_to_flag
    ADD CONSTRAINT field_fk FOREIGN KEY (field_pk) REFERENCES field(pk) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3906 (class 2606 OID 141923008)
-- Name: flag_type_fk; Type: FK CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY flag_value
    ADD CONSTRAINT flag_type_fk FOREIGN KEY (flag_type_pk) REFERENCES flag_type(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3907 (class 2606 OID 141923035)
-- Name: flag_value_fk; Type: FK CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj_to_flag
    ADD CONSTRAINT flag_value_fk FOREIGN KEY (flag_value_pk) REFERENCES flag_value(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3910 (class 2606 OID 141923045)
-- Name: flag_value_fk; Type: FK CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY field_to_flag
    ADD CONSTRAINT flag_value_fk FOREIGN KEY (flag_value_pk) REFERENCES flag_value(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3912 (class 2606 OID 635785349)
-- Name: object2_type_fk; Type: FK CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj2
    ADD CONSTRAINT object2_type_fk FOREIGN KEY (object_type_pk) REFERENCES object_type(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3901 (class 2606 OID 18311)
-- Name: object_type_fk; Type: FK CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj
    ADD CONSTRAINT object_type_fk FOREIGN KEY (object_type_pk) REFERENCES object_type(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3911 (class 2606 OID 635785354)
-- Name: parent2_fk; Type: FK CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj2
    ADD CONSTRAINT parent2_fk FOREIGN KEY (parent_photoobj_pk) REFERENCES photoobj2(pk);


--
-- TOC entry 3900 (class 2606 OID 18364)
-- Name: parent_fk; Type: FK CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj
    ADD CONSTRAINT parent_fk FOREIGN KEY (parent_photoobj_pk) REFERENCES photoobj(pk);


--
-- TOC entry 3904 (class 2606 OID 18369)
-- Name: photoobj_fk; Type: FK CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj_to_thing
    ADD CONSTRAINT photoobj_fk FOREIGN KEY (photoobj_pk) REFERENCES photoobj(pk) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3908 (class 2606 OID 141923030)
-- Name: photoobj_fk; Type: FK CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj_to_flag
    ADD CONSTRAINT photoobj_fk FOREIGN KEY (photoobj_pk) REFERENCES photoobj(pk) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3905 (class 2606 OID 71342131)
-- Name: run_fk; Type: FK CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY field
    ADD CONSTRAINT run_fk FOREIGN KEY (run_pk) REFERENCES run(pk) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3903 (class 2606 OID 18374)
-- Name: think_fk; Type: FK CONSTRAINT; Schema: dataset_sdss_dr12; Owner: -
--

ALTER TABLE ONLY photoobj_to_thing
    ADD CONSTRAINT think_fk FOREIGN KEY (thing_pk) REFERENCES thing(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


-- Completed on 2015-02-25 11:07:48 EST

--
-- PostgreSQL database dump complete
--

