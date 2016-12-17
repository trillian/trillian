--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.0
-- Dumped by pg_dump version 9.5.1

-- Started on 2016-08-19 23:33:56 EDT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 18 (class 2615 OID 16627)
-- Name: files; Type: SCHEMA; Schema: -; Owner: trillian_admin
--

CREATE SCHEMA files;


ALTER SCHEMA files OWNER TO trillian_admin;

SET search_path = files, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 203 (class 1259 OID 16679)
-- Name: base_path; Type: TABLE; Schema: files; Owner: trillian_admin
--

CREATE TABLE base_path (
    pk integer NOT NULL,
    path text
);


ALTER TABLE base_path OWNER TO trillian_admin;

--
-- TOC entry 202 (class 1259 OID 16677)
-- Name: base_path_pk_seq; Type: SEQUENCE; Schema: files; Owner: trillian_admin
--

CREATE SEQUENCE base_path_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE base_path_pk_seq OWNER TO trillian_admin;

--
-- TOC entry 3204 (class 0 OID 0)
-- Dependencies: 202
-- Name: base_path_pk_seq; Type: SEQUENCE OWNED BY; Schema: files; Owner: trillian_admin
--

ALTER SEQUENCE base_path_pk_seq OWNED BY base_path.pk;


--
-- TOC entry 221 (class 1259 OID 16919)
-- Name: file_kind; Type: TABLE; Schema: files; Owner: trillian_admin
--

CREATE TABLE file_kind (
    pk integer NOT NULL,
    label text
);


ALTER TABLE file_kind OWNER TO trillian_admin;

--
-- TOC entry 220 (class 1259 OID 16917)
-- Name: file_kind_pk_seq; Type: SEQUENCE; Schema: files; Owner: trillian_admin
--

CREATE SEQUENCE file_kind_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE file_kind_pk_seq OWNER TO trillian_admin;

--
-- TOC entry 3206 (class 0 OID 0)
-- Dependencies: 220
-- Name: file_kind_pk_seq; Type: SEQUENCE OWNED BY; Schema: files; Owner: trillian_admin
--

ALTER SEQUENCE file_kind_pk_seq OWNED BY file_kind.pk;


--
-- TOC entry 200 (class 1259 OID 16661)
-- Name: fits_file; Type: TABLE; Schema: files; Owner: trillian_admin
--

CREATE TABLE fits_file (
    pk bigint NOT NULL,
    dataset_release_pk integer NOT NULL,
    filename text,
    relative_path text,
    base_path_pk integer,
    size integer,
    sha256_hash text
);


ALTER TABLE fits_file OWNER TO trillian_admin;

--
-- TOC entry 3207 (class 0 OID 0)
-- Dependencies: 200
-- Name: COLUMN fits_file.size; Type: COMMENT; Schema: files; Owner: trillian_admin
--

COMMENT ON COLUMN fits_file.size IS 'size of file in bytes';


--
-- TOC entry 3208 (class 0 OID 0)
-- Dependencies: 200
-- Name: COLUMN fits_file.sha256_hash; Type: COMMENT; Schema: files; Owner: trillian_admin
--

COMMENT ON COLUMN fits_file.sha256_hash IS 'sha256 hash of file in hex format';


--
-- TOC entry 201 (class 1259 OID 16664)
-- Name: fits_file_pk_seq; Type: SEQUENCE; Schema: files; Owner: trillian_admin
--

CREATE SEQUENCE fits_file_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fits_file_pk_seq OWNER TO trillian_admin;

--
-- TOC entry 3210 (class 0 OID 0)
-- Dependencies: 201
-- Name: fits_file_pk_seq; Type: SEQUENCE OWNED BY; Schema: files; Owner: trillian_admin
--

ALTER SEQUENCE fits_file_pk_seq OWNED BY fits_file.pk;


--
-- TOC entry 240 (class 1259 OID 17272)
-- Name: fits_file_to_file_kind; Type: TABLE; Schema: files; Owner: trillian_admin
--

CREATE TABLE fits_file_to_file_kind (
    fits_file_pk bigint NOT NULL,
    file_kind_pk integer NOT NULL
);


ALTER TABLE fits_file_to_file_kind OWNER TO trillian_admin;

--
-- TOC entry 208 (class 1259 OID 16724)
-- Name: fits_hdu; Type: TABLE; Schema: files; Owner: trillian_admin
--

CREATE TABLE fits_hdu (
    pk bigint NOT NULL,
    number smallint NOT NULL,
    header_start_offset integer,
    data_start_offset integer,
    data_end_offset integer,
    fits_file_pk bigint NOT NULL
);


ALTER TABLE fits_hdu OWNER TO trillian_admin;

--
-- TOC entry 3211 (class 0 OID 0)
-- Dependencies: 208
-- Name: COLUMN fits_hdu.number; Type: COMMENT; Schema: files; Owner: trillian_admin
--

COMMENT ON COLUMN fits_hdu.number IS 'the HDU number, starting from 1';


--
-- TOC entry 3212 (class 0 OID 0)
-- Dependencies: 208
-- Name: COLUMN fits_hdu.header_start_offset; Type: COMMENT; Schema: files; Owner: trillian_admin
--

COMMENT ON COLUMN fits_hdu.header_start_offset IS 'byte offset of the start of the header from the beginning of the file';


--
-- TOC entry 3213 (class 0 OID 0)
-- Dependencies: 208
-- Name: COLUMN fits_hdu.data_start_offset; Type: COMMENT; Schema: files; Owner: trillian_admin
--

COMMENT ON COLUMN fits_hdu.data_start_offset IS 'byte offset of the start of the data from the beginning of the file';


--
-- TOC entry 3214 (class 0 OID 0)
-- Dependencies: 208
-- Name: COLUMN fits_hdu.data_end_offset; Type: COMMENT; Schema: files; Owner: trillian_admin
--

COMMENT ON COLUMN fits_hdu.data_end_offset IS 'byte offset to the end of the data from the beginning of the file';


--
-- TOC entry 218 (class 1259 OID 16887)
-- Name: fits_hdu_pk_seq; Type: SEQUENCE; Schema: files; Owner: trillian_admin
--

CREATE SEQUENCE fits_hdu_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fits_hdu_pk_seq OWNER TO trillian_admin;

--
-- TOC entry 3216 (class 0 OID 0)
-- Dependencies: 218
-- Name: fits_hdu_pk_seq; Type: SEQUENCE OWNED BY; Schema: files; Owner: trillian_admin
--

ALTER SEQUENCE fits_hdu_pk_seq OWNED BY fits_hdu.pk;


--
-- TOC entry 219 (class 1259 OID 16907)
-- Name: fits_header_comment; Type: TABLE; Schema: files; Owner: trillian_admin
--

CREATE TABLE fits_header_comment (
    comment_string text,
    pk bigint NOT NULL
);


ALTER TABLE fits_header_comment OWNER TO trillian_admin;

--
-- TOC entry 234 (class 1259 OID 17044)
-- Name: fits_header_comment_pk_seq; Type: SEQUENCE; Schema: files; Owner: trillian_admin
--

CREATE SEQUENCE fits_header_comment_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fits_header_comment_pk_seq OWNER TO trillian_admin;

--
-- TOC entry 3218 (class 0 OID 0)
-- Dependencies: 234
-- Name: fits_header_comment_pk_seq; Type: SEQUENCE OWNED BY; Schema: files; Owner: trillian_admin
--

ALTER SEQUENCE fits_header_comment_pk_seq OWNED BY fits_header_comment.pk;


--
-- TOC entry 205 (class 1259 OID 16697)
-- Name: fits_header_keyword; Type: TABLE; Schema: files; Owner: trillian_admin
--

CREATE TABLE fits_header_keyword (
    pk integer NOT NULL,
    label text
);


ALTER TABLE fits_header_keyword OWNER TO trillian_admin;

--
-- TOC entry 204 (class 1259 OID 16695)
-- Name: fits_header_keyword_pk_seq; Type: SEQUENCE; Schema: files; Owner: trillian_admin
--

CREATE SEQUENCE fits_header_keyword_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fits_header_keyword_pk_seq OWNER TO trillian_admin;

--
-- TOC entry 3220 (class 0 OID 0)
-- Dependencies: 204
-- Name: fits_header_keyword_pk_seq; Type: SEQUENCE OWNED BY; Schema: files; Owner: trillian_admin
--

ALTER SEQUENCE fits_header_keyword_pk_seq OWNED BY fits_header_keyword.pk;


--
-- TOC entry 207 (class 1259 OID 16710)
-- Name: fits_header_value; Type: TABLE; Schema: files; Owner: trillian_admin
--

CREATE TABLE fits_header_value (
    pk bigint NOT NULL,
    value text,
    index integer NOT NULL,
    fits_header_keyword_pk integer NOT NULL,
    fits_hdu_pk bigint NOT NULL,
    fits_header_comment_pk bigint,
    string_value text NOT NULL,
    numeric_value numeric
);


ALTER TABLE fits_header_value OWNER TO trillian_admin;

--
-- TOC entry 3221 (class 0 OID 0)
-- Dependencies: 207
-- Name: COLUMN fits_header_value.string_value; Type: COMMENT; Schema: files; Owner: trillian_admin
--

COMMENT ON COLUMN fits_header_value.string_value IS 'the value field of the header card as a string';


--
-- TOC entry 3222 (class 0 OID 0)
-- Dependencies: 207
-- Name: COLUMN fits_header_value.numeric_value; Type: COMMENT; Schema: files; Owner: trillian_admin
--

COMMENT ON COLUMN fits_header_value.numeric_value IS 'numeric value if the card type is float or integer';


--
-- TOC entry 206 (class 1259 OID 16708)
-- Name: fits_header_value_pk_seq; Type: SEQUENCE; Schema: files; Owner: trillian_admin
--

CREATE SEQUENCE fits_header_value_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fits_header_value_pk_seq OWNER TO trillian_admin;

--
-- TOC entry 3224 (class 0 OID 0)
-- Dependencies: 206
-- Name: fits_header_value_pk_seq; Type: SEQUENCE OWNED BY; Schema: files; Owner: trillian_admin
--

ALTER SEQUENCE fits_header_value_pk_seq OWNED BY fits_header_value.pk;


--
-- TOC entry 3035 (class 2604 OID 16682)
-- Name: pk; Type: DEFAULT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY base_path ALTER COLUMN pk SET DEFAULT nextval('base_path_pk_seq'::regclass);


--
-- TOC entry 3040 (class 2604 OID 16922)
-- Name: pk; Type: DEFAULT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY file_kind ALTER COLUMN pk SET DEFAULT nextval('file_kind_pk_seq'::regclass);


--
-- TOC entry 3034 (class 2604 OID 16666)
-- Name: pk; Type: DEFAULT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_file ALTER COLUMN pk SET DEFAULT nextval('fits_file_pk_seq'::regclass);


--
-- TOC entry 3038 (class 2604 OID 16889)
-- Name: pk; Type: DEFAULT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_hdu ALTER COLUMN pk SET DEFAULT nextval('fits_hdu_pk_seq'::regclass);


--
-- TOC entry 3039 (class 2604 OID 17046)
-- Name: pk; Type: DEFAULT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_header_comment ALTER COLUMN pk SET DEFAULT nextval('fits_header_comment_pk_seq'::regclass);


--
-- TOC entry 3036 (class 2604 OID 16700)
-- Name: pk; Type: DEFAULT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_header_keyword ALTER COLUMN pk SET DEFAULT nextval('fits_header_keyword_pk_seq'::regclass);


--
-- TOC entry 3037 (class 2604 OID 16713)
-- Name: pk; Type: DEFAULT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_header_value ALTER COLUMN pk SET DEFAULT nextval('fits_header_value_pk_seq'::regclass);


--
-- TOC entry 3049 (class 2606 OID 16689)
-- Name: base_path_path_uniq; Type: CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY base_path
    ADD CONSTRAINT base_path_path_uniq UNIQUE (path);


--
-- TOC entry 3051 (class 2606 OID 16687)
-- Name: base_path_pk; Type: CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY base_path
    ADD CONSTRAINT base_path_pk PRIMARY KEY (pk);


--
-- TOC entry 3077 (class 2606 OID 16929)
-- Name: file_kind_label_uniq; Type: CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY file_kind
    ADD CONSTRAINT file_kind_label_uniq UNIQUE (label);


--
-- TOC entry 3079 (class 2606 OID 16927)
-- Name: file_kind_pk; Type: CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY file_kind
    ADD CONSTRAINT file_kind_pk PRIMARY KEY (pk);


--
-- TOC entry 3066 (class 2606 OID 16730)
-- Name: fits_file_hdu_pk_uniq; Type: CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_hdu
    ADD CONSTRAINT fits_file_hdu_pk_uniq UNIQUE (fits_file_pk, number);


--
-- TOC entry 3044 (class 2606 OID 16674)
-- Name: fits_file_pk; Type: CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_file
    ADD CONSTRAINT fits_file_pk PRIMARY KEY (pk);


--
-- TOC entry 3081 (class 2606 OID 17276)
-- Name: fits_file_to_file_kind_pk; Type: CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_file_to_file_kind
    ADD CONSTRAINT fits_file_to_file_kind_pk PRIMARY KEY (fits_file_pk, file_kind_pk);


--
-- TOC entry 3070 (class 2606 OID 16896)
-- Name: fits_hdu_pk; Type: CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_hdu
    ADD CONSTRAINT fits_hdu_pk PRIMARY KEY (pk);


--
-- TOC entry 3072 (class 2606 OID 17055)
-- Name: fits_header_comment_pk; Type: CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_header_comment
    ADD CONSTRAINT fits_header_comment_pk PRIMARY KEY (pk);


--
-- TOC entry 3075 (class 2606 OID 17057)
-- Name: fits_header_comment_uniq; Type: CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_header_comment
    ADD CONSTRAINT fits_header_comment_uniq UNIQUE (comment_string);


--
-- TOC entry 3055 (class 2606 OID 16705)
-- Name: fits_header_keyword_pk; Type: CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_header_keyword
    ADD CONSTRAINT fits_header_keyword_pk PRIMARY KEY (pk);


--
-- TOC entry 3057 (class 2606 OID 16707)
-- Name: fits_header_keyword_uniq; Type: CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_header_keyword
    ADD CONSTRAINT fits_header_keyword_uniq UNIQUE (label);


--
-- TOC entry 3064 (class 2606 OID 16718)
-- Name: fits_header_value_pk; Type: CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_header_value
    ADD CONSTRAINT fits_header_value_pk PRIMARY KEY (pk);


--
-- TOC entry 3047 (class 2606 OID 17028)
-- Name: release_filename_uniq; Type: CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_file
    ADD CONSTRAINT release_filename_uniq UNIQUE (filename, dataset_release_pk);


--
-- TOC entry 3052 (class 1259 OID 16741)
-- Name: bath_path_path_idx; Type: INDEX; Schema: files; Owner: trillian_admin
--

CREATE INDEX bath_path_path_idx ON base_path USING btree (path);


--
-- TOC entry 3041 (class 1259 OID 16743)
-- Name: fits_file_base_path_idx; Type: INDEX; Schema: files; Owner: trillian_admin
--

CREATE INDEX fits_file_base_path_idx ON fits_file USING btree (base_path_pk);


--
-- TOC entry 3042 (class 1259 OID 17316)
-- Name: fits_file_filename_parttern_ops_idx; Type: INDEX; Schema: files; Owner: trillian_admin
--

CREATE INDEX fits_file_filename_parttern_ops_idx ON fits_file USING btree (filename text_pattern_ops);


--
-- TOC entry 3067 (class 1259 OID 16744)
-- Name: fits_file_pk_idx; Type: INDEX; Schema: files; Owner: trillian_admin
--

CREATE INDEX fits_file_pk_idx ON fits_hdu USING btree (fits_file_pk);


--
-- TOC entry 3068 (class 1259 OID 17123)
-- Name: fits_hdu_number_idx; Type: INDEX; Schema: files; Owner: trillian_admin
--

CREATE INDEX fits_hdu_number_idx ON fits_hdu USING btree (number);


--
-- TOC entry 3073 (class 1259 OID 17038)
-- Name: fits_header_comment_string_idx; Type: INDEX; Schema: files; Owner: trillian_admin
--

CREATE INDEX fits_header_comment_string_idx ON fits_header_comment USING btree (comment_string);


--
-- TOC entry 3058 (class 1259 OID 16745)
-- Name: fits_header_fits_hdu_idx; Type: INDEX; Schema: files; Owner: trillian_admin
--

CREATE INDEX fits_header_fits_hdu_idx ON fits_header_value USING btree (fits_hdu_pk);


--
-- TOC entry 3059 (class 1259 OID 16746)
-- Name: fits_header_keyword_idx; Type: INDEX; Schema: files; Owner: trillian_admin
--

CREATE INDEX fits_header_keyword_idx ON fits_header_value USING btree (fits_header_keyword_pk);


--
-- TOC entry 3053 (class 1259 OID 16750)
-- Name: fits_header_keyword_label_idx; Type: INDEX; Schema: files; Owner: trillian_admin
--

CREATE INDEX fits_header_keyword_label_idx ON fits_header_keyword USING btree (label);


--
-- TOC entry 3060 (class 1259 OID 16748)
-- Name: fits_header_value_idx; Type: INDEX; Schema: files; Owner: trillian_admin
--

CREATE INDEX fits_header_value_idx ON fits_header_value USING btree (index);


--
-- TOC entry 3061 (class 1259 OID 16747)
-- Name: fits_header_value_index_idx; Type: INDEX; Schema: files; Owner: trillian_admin
--

CREATE INDEX fits_header_value_index_idx ON fits_header_value USING btree (index);


--
-- TOC entry 3062 (class 1259 OID 17271)
-- Name: fits_header_value_numeric_value_idx; Type: INDEX; Schema: files; Owner: trillian_admin
--

CREATE INDEX fits_header_value_numeric_value_idx ON fits_header_value USING btree (numeric_value);


--
-- TOC entry 3045 (class 1259 OID 17034)
-- Name: fki_fits_file_dataset_release_fk; Type: INDEX; Schema: files; Owner: trillian_admin
--

CREATE INDEX fki_fits_file_dataset_release_fk ON fits_file USING btree (dataset_release_pk);


--
-- TOC entry 3082 (class 2606 OID 16690)
-- Name: base_path_fk; Type: FK CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_file
    ADD CONSTRAINT base_path_fk FOREIGN KEY (base_path_pk) REFERENCES base_path(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3088 (class 2606 OID 17277)
-- Name: file_kind_fk; Type: FK CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_file_to_file_kind
    ADD CONSTRAINT file_kind_fk FOREIGN KEY (file_kind_pk) REFERENCES file_kind(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3086 (class 2606 OID 17058)
-- Name: fits_comment_fk; Type: FK CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_header_value
    ADD CONSTRAINT fits_comment_fk FOREIGN KEY (fits_header_comment_pk) REFERENCES fits_header_comment(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3083 (class 2606 OID 17039)
-- Name: fits_file_dataset_release_fk; Type: FK CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_file
    ADD CONSTRAINT fits_file_dataset_release_fk FOREIGN KEY (dataset_release_pk) REFERENCES trillian.dataset_release(pk) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3087 (class 2606 OID 16897)
-- Name: fits_file_fk; Type: FK CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_hdu
    ADD CONSTRAINT fits_file_fk FOREIGN KEY (fits_file_pk) REFERENCES fits_file(pk) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3089 (class 2606 OID 17282)
-- Name: fits_file_fk; Type: FK CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_file_to_file_kind
    ADD CONSTRAINT fits_file_fk FOREIGN KEY (fits_file_pk) REFERENCES fits_file(pk) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3085 (class 2606 OID 16902)
-- Name: fits_hdu_fk; Type: FK CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_header_value
    ADD CONSTRAINT fits_hdu_fk FOREIGN KEY (fits_hdu_pk) REFERENCES fits_hdu(pk) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3084 (class 2606 OID 16719)
-- Name: fits_header_keyword_fk; Type: FK CONSTRAINT; Schema: files; Owner: trillian_admin
--

ALTER TABLE ONLY fits_header_value
    ADD CONSTRAINT fits_header_keyword_fk FOREIGN KEY (fits_header_keyword_pk) REFERENCES fits_header_keyword(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3203 (class 0 OID 0)
-- Dependencies: 203
-- Name: base_path; Type: ACL; Schema: files; Owner: trillian_admin
--

REVOKE ALL ON TABLE base_path FROM PUBLIC;
REVOKE ALL ON TABLE base_path FROM trillian_admin;
GRANT ALL ON TABLE base_path TO trillian_admin;


--
-- TOC entry 3205 (class 0 OID 0)
-- Dependencies: 221
-- Name: file_kind; Type: ACL; Schema: files; Owner: trillian_admin
--

REVOKE ALL ON TABLE file_kind FROM PUBLIC;
REVOKE ALL ON TABLE file_kind FROM trillian_admin;
GRANT ALL ON TABLE file_kind TO trillian_admin;


--
-- TOC entry 3209 (class 0 OID 0)
-- Dependencies: 200
-- Name: fits_file; Type: ACL; Schema: files; Owner: trillian_admin
--

REVOKE ALL ON TABLE fits_file FROM PUBLIC;
REVOKE ALL ON TABLE fits_file FROM trillian_admin;
GRANT ALL ON TABLE fits_file TO trillian_admin;


--
-- TOC entry 3215 (class 0 OID 0)
-- Dependencies: 208
-- Name: fits_hdu; Type: ACL; Schema: files; Owner: trillian_admin
--

REVOKE ALL ON TABLE fits_hdu FROM PUBLIC;
REVOKE ALL ON TABLE fits_hdu FROM trillian_admin;
GRANT ALL ON TABLE fits_hdu TO trillian_admin;


--
-- TOC entry 3217 (class 0 OID 0)
-- Dependencies: 219
-- Name: fits_header_comment; Type: ACL; Schema: files; Owner: trillian_admin
--

REVOKE ALL ON TABLE fits_header_comment FROM PUBLIC;
REVOKE ALL ON TABLE fits_header_comment FROM trillian_admin;
GRANT ALL ON TABLE fits_header_comment TO trillian_admin;


--
-- TOC entry 3219 (class 0 OID 0)
-- Dependencies: 205
-- Name: fits_header_keyword; Type: ACL; Schema: files; Owner: trillian_admin
--

REVOKE ALL ON TABLE fits_header_keyword FROM PUBLIC;
REVOKE ALL ON TABLE fits_header_keyword FROM trillian_admin;
GRANT ALL ON TABLE fits_header_keyword TO trillian_admin;


--
-- TOC entry 3223 (class 0 OID 0)
-- Dependencies: 207
-- Name: fits_header_value; Type: ACL; Schema: files; Owner: trillian_admin
--

REVOKE ALL ON TABLE fits_header_value FROM PUBLIC;
REVOKE ALL ON TABLE fits_header_value FROM trillian_admin;
GRANT ALL ON TABLE fits_header_value TO trillian_admin;


-- Completed on 2016-08-19 23:34:06 EDT

--
-- PostgreSQL database dump complete
--

