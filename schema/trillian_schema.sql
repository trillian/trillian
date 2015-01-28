--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.5
-- Dumped by pg_dump version 9.4.0
-- Started on 2015-01-28 07:50:11 EST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 2288 (class 1262 OID 16384)
-- Dependencies: 2287
-- Name: trilliandb; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON DATABASE trilliandb IS 'Trillian database';


--
-- TOC entry 6 (class 2615 OID 2200)
-- Name: trillian; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA trillian;


--
-- TOC entry 2289 (class 0 OID 0)
-- Dependencies: 6
-- Name: SCHEMA trillian; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA trillian IS 'initial Trillian schema';


--
-- TOC entry 186 (class 3079 OID 12018)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2290 (class 0 OID 0)
-- Dependencies: 186
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = trillian, pg_catalog;

SET default_with_oids = false;

--
-- TOC entry 178 (class 1259 OID 16449)
-- Name: dataset; Type: TABLE; Schema: trillian; Owner: -
--

CREATE TABLE dataset (
    pk integer NOT NULL,
    label text
);


--
-- TOC entry 177 (class 1259 OID 16447)
-- Name: dataset_pk_seq; Type: SEQUENCE; Schema: trillian; Owner: -
--

CREATE SEQUENCE dataset_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2291 (class 0 OID 0)
-- Dependencies: 177
-- Name: dataset_pk_seq; Type: SEQUENCE OWNED BY; Schema: trillian; Owner: -
--

ALTER SEQUENCE dataset_pk_seq OWNED BY dataset.pk;


--
-- TOC entry 171 (class 1259 OID 16396)
-- Name: node; Type: TABLE; Schema: trillian; Owner: -
--

CREATE TABLE node (
    pk integer NOT NULL,
    node_type_pk smallint,
    available_space integer,
    server_pk integer,
    username text,
    password text,
    server_path text,
    port integer,
    host_address inet
);


--
-- TOC entry 2292 (class 0 OID 0)
-- Dependencies: 171
-- Name: TABLE node; Type: COMMENT; Schema: trillian; Owner: -
--

COMMENT ON TABLE node IS 'Trillian nodes';


--
-- TOC entry 2293 (class 0 OID 0)
-- Dependencies: 171
-- Name: COLUMN node.available_space; Type: COMMENT; Schema: trillian; Owner: -
--

COMMENT ON COLUMN node.available_space IS 'unit: GB';


--
-- TOC entry 180 (class 1259 OID 16465)
-- Name: node_capability; Type: TABLE; Schema: trillian; Owner: -
--

CREATE TABLE node_capability (
    pk smallint NOT NULL,
    label text
);


--
-- TOC entry 179 (class 1259 OID 16463)
-- Name: node_capability_pk_seq; Type: SEQUENCE; Schema: trillian; Owner: -
--

CREATE SEQUENCE node_capability_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2294 (class 0 OID 0)
-- Dependencies: 179
-- Name: node_capability_pk_seq; Type: SEQUENCE OWNED BY; Schema: trillian; Owner: -
--

ALTER SEQUENCE node_capability_pk_seq OWNED BY node_capability.pk;


--
-- TOC entry 170 (class 1259 OID 16394)
-- Name: node_pk_seq; Type: SEQUENCE; Schema: trillian; Owner: -
--

CREATE SEQUENCE node_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2295 (class 0 OID 0)
-- Dependencies: 170
-- Name: node_pk_seq; Type: SEQUENCE OWNED BY; Schema: trillian; Owner: -
--

ALTER SEQUENCE node_pk_seq OWNED BY node.pk;


--
-- TOC entry 181 (class 1259 OID 16474)
-- Name: node_to_capability; Type: TABLE; Schema: trillian; Owner: -
--

CREATE TABLE node_to_capability (
    node_pk smallint NOT NULL,
    node_capability_pk integer NOT NULL
);


--
-- TOC entry 176 (class 1259 OID 16437)
-- Name: node_to_dataset; Type: TABLE; Schema: trillian; Owner: -
--

CREATE TABLE node_to_dataset (
    node_pk smallint NOT NULL,
    dataset_pk integer NOT NULL
);


--
-- TOC entry 173 (class 1259 OID 16407)
-- Name: node_type; Type: TABLE; Schema: trillian; Owner: -
--

CREATE TABLE node_type (
    pk smallint NOT NULL,
    label text
);


--
-- TOC entry 172 (class 1259 OID 16405)
-- Name: node_type_pk_seq; Type: SEQUENCE; Schema: trillian; Owner: -
--

CREATE SEQUENCE node_type_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2296 (class 0 OID 0)
-- Dependencies: 172
-- Name: node_type_pk_seq; Type: SEQUENCE OWNED BY; Schema: trillian; Owner: -
--

ALTER SEQUENCE node_type_pk_seq OWNED BY node_type.pk;


--
-- TOC entry 175 (class 1259 OID 16423)
-- Name: server; Type: TABLE; Schema: trillian; Owner: -
--

CREATE TABLE server (
    pk smallint NOT NULL,
    name text NOT NULL
);


--
-- TOC entry 2297 (class 0 OID 0)
-- Dependencies: 175
-- Name: TABLE server; Type: COMMENT; Schema: trillian; Owner: -
--

COMMENT ON TABLE server IS 'This table represents the central Trillian server.';


--
-- TOC entry 174 (class 1259 OID 16421)
-- Name: server_pk_seq; Type: SEQUENCE; Schema: trillian; Owner: -
--

CREATE SEQUENCE server_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2298 (class 0 OID 0)
-- Dependencies: 174
-- Name: server_pk_seq; Type: SEQUENCE OWNED BY; Schema: trillian; Owner: -
--

ALTER SEQUENCE server_pk_seq OWNED BY server.pk;


--
-- TOC entry 185 (class 1259 OID 16519)
-- Name: trixel; Type: TABLE; Schema: trillian; Owner: -
--

CREATE TABLE trixel (
    pk integer NOT NULL,
    healpix_pixel_id integer NOT NULL,
    node_pk smallint,
    healpix_n_side smallint,
    parent_trixel_pk integer
);


--
-- TOC entry 184 (class 1259 OID 16517)
-- Name: trixel_pk_seq; Type: SEQUENCE; Schema: trillian; Owner: -
--

CREATE SEQUENCE trixel_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2299 (class 0 OID 0)
-- Dependencies: 184
-- Name: trixel_pk_seq; Type: SEQUENCE OWNED BY; Schema: trillian; Owner: -
--

ALTER SEQUENCE trixel_pk_seq OWNED BY trixel.pk;


--
-- TOC entry 183 (class 1259 OID 16507)
-- Name: user; Type: TABLE; Schema: trillian; Owner: -
--

CREATE TABLE "user" (
    pk integer NOT NULL,
    first_name text,
    last_name text,
    password text
);


--
-- TOC entry 182 (class 1259 OID 16505)
-- Name: user_pk_seq; Type: SEQUENCE; Schema: trillian; Owner: -
--

CREATE SEQUENCE user_pk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2300 (class 0 OID 0)
-- Dependencies: 182
-- Name: user_pk_seq; Type: SEQUENCE OWNED BY; Schema: trillian; Owner: -
--

ALTER SEQUENCE user_pk_seq OWNED BY "user".pk;


--
-- TOC entry 2142 (class 2604 OID 16452)
-- Name: pk; Type: DEFAULT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY dataset ALTER COLUMN pk SET DEFAULT nextval('dataset_pk_seq'::regclass);


--
-- TOC entry 2139 (class 2604 OID 16399)
-- Name: pk; Type: DEFAULT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node ALTER COLUMN pk SET DEFAULT nextval('node_pk_seq'::regclass);


--
-- TOC entry 2143 (class 2604 OID 16468)
-- Name: pk; Type: DEFAULT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node_capability ALTER COLUMN pk SET DEFAULT nextval('node_capability_pk_seq'::regclass);


--
-- TOC entry 2140 (class 2604 OID 16410)
-- Name: pk; Type: DEFAULT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node_type ALTER COLUMN pk SET DEFAULT nextval('node_type_pk_seq'::regclass);


--
-- TOC entry 2141 (class 2604 OID 16426)
-- Name: pk; Type: DEFAULT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY server ALTER COLUMN pk SET DEFAULT nextval('server_pk_seq'::regclass);


--
-- TOC entry 2145 (class 2604 OID 16522)
-- Name: pk; Type: DEFAULT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY trixel ALTER COLUMN pk SET DEFAULT nextval('trixel_pk_seq'::regclass);


--
-- TOC entry 2144 (class 2604 OID 16510)
-- Name: pk; Type: DEFAULT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY "user" ALTER COLUMN pk SET DEFAULT nextval('user_pk_seq'::regclass);


--
-- TOC entry 2159 (class 2606 OID 16457)
-- Name: dataset_pk; Type: CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY dataset
    ADD CONSTRAINT dataset_pk PRIMARY KEY (pk);


--
-- TOC entry 2147 (class 2606 OID 16536)
-- Name: host_address_uniq; Type: CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node
    ADD CONSTRAINT host_address_uniq UNIQUE (host_address);


--
-- TOC entry 2161 (class 2606 OID 16473)
-- Name: node_capability_pk; Type: CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node_capability
    ADD CONSTRAINT node_capability_pk PRIMARY KEY (pk);


--
-- TOC entry 2149 (class 2606 OID 16404)
-- Name: node_pk; Type: CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node
    ADD CONSTRAINT node_pk PRIMARY KEY (pk);


--
-- TOC entry 2163 (class 2606 OID 16478)
-- Name: node_to_capability_pk; Type: CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node_to_capability
    ADD CONSTRAINT node_to_capability_pk PRIMARY KEY (node_pk, node_capability_pk);


--
-- TOC entry 2157 (class 2606 OID 16441)
-- Name: node_to_dataset_pk; Type: CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node_to_dataset
    ADD CONSTRAINT node_to_dataset_pk PRIMARY KEY (node_pk, dataset_pk);


--
-- TOC entry 2151 (class 2606 OID 16415)
-- Name: node_type_pk; Type: CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node_type
    ADD CONSTRAINT node_type_pk PRIMARY KEY (pk);


--
-- TOC entry 2153 (class 2606 OID 16540)
-- Name: server_name_uniq; Type: CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY server
    ADD CONSTRAINT server_name_uniq UNIQUE (name);


--
-- TOC entry 2155 (class 2606 OID 16431)
-- Name: server_pk; Type: CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY server
    ADD CONSTRAINT server_pk PRIMARY KEY (pk);


--
-- TOC entry 2167 (class 2606 OID 16524)
-- Name: trixel_pk; Type: CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY trixel
    ADD CONSTRAINT trixel_pk PRIMARY KEY (pk);


--
-- TOC entry 2165 (class 2606 OID 16515)
-- Name: user_pk; Type: CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_pk PRIMARY KEY (pk);


--
-- TOC entry 2173 (class 2606 OID 16484)
-- Name: node_to_capability_capability_fk; Type: FK CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node_to_capability
    ADD CONSTRAINT node_to_capability_capability_fk FOREIGN KEY (node_capability_pk) REFERENCES node_capability(pk) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2172 (class 2606 OID 16479)
-- Name: node_to_capability_node_fk; Type: FK CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node_to_capability
    ADD CONSTRAINT node_to_capability_node_fk FOREIGN KEY (node_pk) REFERENCES node(pk) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2171 (class 2606 OID 16458)
-- Name: node_to_dataset_dataset_fk; Type: FK CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node_to_dataset
    ADD CONSTRAINT node_to_dataset_dataset_fk FOREIGN KEY (dataset_pk) REFERENCES dataset(pk) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2170 (class 2606 OID 16442)
-- Name: node_to_dataset_node_fk; Type: FK CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node_to_dataset
    ADD CONSTRAINT node_to_dataset_node_fk FOREIGN KEY (node_pk) REFERENCES node(pk) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2168 (class 2606 OID 16416)
-- Name: node_type_fk; Type: FK CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node
    ADD CONSTRAINT node_type_fk FOREIGN KEY (node_type_pk) REFERENCES node_type(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 2169 (class 2606 OID 16432)
-- Name: server_fk; Type: FK CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY node
    ADD CONSTRAINT server_fk FOREIGN KEY (server_pk) REFERENCES server(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 2174 (class 2606 OID 16525)
-- Name: trixel_node_fk; Type: FK CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY trixel
    ADD CONSTRAINT trixel_node_fk FOREIGN KEY (node_pk) REFERENCES node(pk) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 2175 (class 2606 OID 16530)
-- Name: trixel_parent_fk; Type: FK CONSTRAINT; Schema: trillian; Owner: -
--

ALTER TABLE ONLY trixel
    ADD CONSTRAINT trixel_parent_fk FOREIGN KEY (parent_trixel_pk) REFERENCES trixel(pk) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2015-01-28 07:50:11 EST

--
-- PostgreSQL database dump complete
--

