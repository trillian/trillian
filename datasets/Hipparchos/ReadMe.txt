I/239           The Hipparcos and Tycho Catalogues                    (ESA 1997)
================================================================================
The Hipparcos and Tycho Catalogues
    ESA 1997
   <ESA, 1997, The Hipparcos Catalogue, ESA SP-1200>
   <ESA, 1997, The Tycho Catalogue, ESA SP-1200>
   =1997HIP...C......0E
================================================================================
ADC_Keywords: Positional data ; Proper motions ; Parallaxes, trigonometric ;
              Photometry ; Fundamental catalog ; Stars, double and multiple
Mission_Name: Hipparcos

Description:
    The Hipparcos and Tycho Catalogues are the primary products of the
    European Space Agency's astrometric mission, Hipparcos. The satellite,
    which operated for four years, returned high quality scientific data
    from November 1989 to March 1993.

    Each of the catalogues contains a large quantity of very high quality
    astrometric and photometric data. In addition there are associated
    annexes featuring variability and double/multiple star data, and solar
    system astrometric and photometric measurements. In the case of the
    Hipparcos Catalogue, the principal parts are provided in both printed
    and machine-readable form (on CDROM). In the case of the Tycho
    Catalogue, results are provided in machine-readable form only (on
    CDROM). Although in general only the final reduced and calibrated
    astrometric and photometric data are provided, some auxiliary files
    containing results from intermediate stages of the data processing, of
    relevance for the more-specialised user, have also been retained for
    publication. (Some, but not all, data files are available from the
    Centre de Donnees astronomiques de Strasbourg.)

    The global data analysis tasks, proceeding from nearly 1000 Gbit of
    raw satellite data to the final catalogues, was a lengthy and complex
    process, and was undertaken by the NDAC and FAST Consortia, together
    responsible for the production of the Hipparcos Catalogue, and the
    Tycho Consortium, responsible for the production of the Tycho
    Catalogue. A fourth scientific consortium, the INCA Consortium, was
    responsible for the construction of the Hipparcos observing programme,
    compiling the best-available data for the selected stars before launch
    into the Hipparcos Input Catalogue. The production of the Hipparcos
    and Tycho Catalogues marks the formal end of the involvement in the
    mission by the European Space Agency and the four scientific
    consortia.

    For more complete and detailed information on the data, the user is
    advised to refer to Volume 1 ("Introduction and Guide to the Data",
    ESA SP-1200) of the printed Hipparcos and Tycho Catalogues. The user
    should also note that in order to convert the Double and Multiple
    Systems (Component solutions) data file hip_dm_c.dat into FITS format
    it is first necessary to filter the file according to whether the
    entry is a component record (identified by COMP in field DCM5) or a
    correlation record (identified by CORR in field DCM5) because of the
    different structures of the respective records. On a Unix system this
    can be achieved as follows:

    grep COMP hip_dm_c.dat > h_dm_com.dat
    grep CORR hip_dm_c.dat > h_dm_cor.dat

    The catalogue description file (this file) gives the relevant
    information for converting the main data files, including h_dm_cor.dat
    and h_dm_com.dat, into FITS format.

    The machine readable data files (i.e. those available on CD-ROM and
    the subset available from the CDS) contain several extra fields in
    addition to the data from the printed catalogue. These fields are
    identified by the letter `M' in the data label (e.g. the field DGM1
    contains data only available in the machine readable file
    hip_dm_g.dat).

File Summary:
--------------------------------------------------------------------------------
 FileName    Lrecl    Records    Explanations
--------------------------------------------------------------------------------
ReadMe          80          .    This file
hip_main.dat   450     118218    The Hipparcos Main Catalogue
h_dm_com.dat   238      24588    Double and Multiples: Component solutions -COMP
h_dm_cor.dat   238      12591    Double and Multiples: Component solutions -CORR
hip_dm_g.dat   195       2622    Double and Multiples: Acceleration solutions
hip_dm_o.dat   337        235    Double and Multiples: Orbital solutions
hip_dm_v.dat   144        288    Double and Multiples: VIM solutions
hip_dm_x.dat    22       1561    Double and Multiples: Stochastic solutions
hip_va_1.dat   142       2712    Variability Annex: Periodic variables
hip_va_2.dat   142       5542    Variability Annex: Unsolved variables
solar_ha.dat    64       5609    Solar System Annex: Astrometric catalogue
solar_hp.dat    63       2639    Solar System Annex: Photometric catalogue
solar_t.dat     95        291    Solar System Annex: Tycho astrometry/photometry
hd_notes.doc    97       2622    Hipparcos notes: Double and multiple systems
hg_notes.doc    97       3898    Hipparcos notes: General notes
hp_notes.doc    97       2444    Hipparcos notes: Photometric notes
hp_refs.doc     19      33769    References Hipparcos stars
hp_auth.doc     80       4335    References of hp_notes.doc
dmsa_o.doc      80        118    References of hip_dm_o.dat
tyc_main.dat   350    1058332    The main part of Tycho Catalogue
--------------------------------------------------------------------------------

See also:
    I/196 : Hipparcos Input Catalog (HIC) (Turon et al., 1993)
    I/211 : CCDM (Components of Double and Multiple stars) (Dommanget,  1994)
    I/146 : PPM-North Catalogue (Roeser et al., 1988)
    I/193 : PPM-South Catalogue (Bastian et al., 1993)
    I/208 : 90000 stars Supplement to the PPM Catalogue (Roeser+, 1994)
    I/197 : Tycho Input Catalogue, Revised version (TICR) (Egret et al. 1992)
    http://astro.estec.esa.nl/Hipparcos/catalog.html : the ESA pages
            on Hipparcos and Tycho Catalogues
    I/246 : The ACT Reference Catalog (Urban+ 1997)
    I/250 : The Tycho Reference Catalogue (Hog+ 1998)

Byte-by-byte Description of file: hip_main.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
       1  A1    ---     Catalog   [H] Catalogue (H=Hipparcos)               (H0)
   9- 14  I6    ---     HIP       Identifier (HIP number)                   (H1)
      16  A1    ---     Proxy    *[HT] Proximity flag                       (H2)
  18- 28  A11   ---     RAhms     Right ascension in h m s, ICRS (J1991.25) (H3)
  30- 40  A11   ---     DEdms     Declination in deg ' ", ICRS (J1991.25)   (H4)
  42- 46  F5.2  mag     Vmag      ? Magnitude in Johnson V                  (H5)
      48  I1    ---     VarFlag  *[1,3]? Coarse variability flag            (H6)
      50  A1    ---   r_Vmag     *[GHT] Source of magnitude                 (H7)
  52- 63  F12.8 deg     RAdeg    *? alpha, degrees (ICRS, Epoch=J1991.25)   (H8)
  65- 76  F12.8 deg     DEdeg    *? delta, degrees (ICRS, Epoch=J1991.25)   (H9)
      78  A1    ---     AstroRef *[*+A-Z] Reference flag for astrometry    (H10)
  80- 86  F7.2  mas     Plx       ? Trigonometric parallax                 (H11)
  88- 95  F8.2 mas/yr   pmRA     *? Proper motion mu_alpha.cos(delta), ICRS(H12)
  97-104  F8.2 mas/yr   pmDE     *? Proper motion mu_delta, ICRS           (H13)
 106-111  F6.2  mas   e_RAdeg    *? Standard error in RA*cos(DEdeg)        (H14)
 113-118  F6.2  mas   e_DEdeg    *? Standard error in DE                   (H15)
 120-125  F6.2  mas   e_Plx       ? Standard error in Plx                  (H16)
 127-132  F6.2 mas/yr e_pmRA      ? Standard error in pmRA                 (H17)
 134-139  F6.2 mas/yr e_pmDE      ? Standard error in pmDE                 (H18)
 141-145  F5.2  ---     DE:RA     [-1/1]? Correlation, DE/RA*cos(delta)    (H19)
 147-151  F5.2  ---     Plx:RA    [-1/1]? Correlation, Plx/RA*cos(delta)   (H20)
 153-157  F5.2  ---     Plx:DE    [-1/1]? Correlation, Plx/DE              (H21)
 159-163  F5.2  ---     pmRA:RA   [-1/1]? Correlation, pmRA/RA*cos(delta)  (H22)
 165-169  F5.2  ---     pmRA:DE   [-1/1]? Correlation, pmRA/DE             (H23)
 171-175  F5.2  ---     pmRA:Plx  [-1/1]? Correlation, pmRA/Plx            (H24)
 177-181  F5.2  ---     pmDE:RA   [-1/1]? Correlation, pmDE/RA*cos(delta)  (H25)
 183-187  F5.2  ---     pmDE:DE   [-1/1]? Correlation, pmDE/DE             (H26)
 189-193  F5.2  ---     pmDE:Plx  [-1/1]? Correlation, pmDE/Plx            (H27)
 195-199  F5.2  ---     pmDE:pmRA [-1/1]? Correlation, pmDE/pmRA           (H28)
 201-203  I3    %       F1        ? Percentage of rejected data            (H29)
 205-209  F5.2  ---     F2       *? Goodness-of-fit parameter              (H30)
 211-216  I6    ---     ---       HIP number (repetition)                  (H31)
 218-223  F6.3  mag     BTmag     ? Mean BT magnitude                      (H32)
 225-229  F5.3  mag   e_BTmag     ? Standard error on BTmag                (H33)
 231-236  F6.3  mag     VTmag     ? Mean VT magnitude                      (H34)
 238-242  F5.3  mag   e_VTmag     ? Standard error on VTmag                (H35)
     244  A1    ---   m_BTmag    *[A-Z*-] Reference flag for BT and VTmag  (H36)
 246-251  F6.3  mag     B-V       ? Johnson B-V colour                     (H37)
 253-257  F5.3  mag   e_B-V       ? Standard error on B-V                  (H38)
     259  A1    ---   r_B-V       [GT] Source of B-V from Ground or Tycho  (H39)
 261-264  F4.2  mag     V-I       ? Colour index in Cousins' system        (H40)
 266-269  F4.2  mag   e_V-I       ? Standard error on V-I                  (H41)
     271  A1    ---   r_V-I      *[A-T] Source of V-I                      (H42)
     273  A1    ---     CombMag   [*] Flag for combined Vmag, B-V, V-I     (H43)
 275-281  F7.4  mag     Hpmag    *? Median magnitude in Hipparcos system   (H44)
 283-288  F6.4  mag   e_Hpmag    *? Standard error on Hpmag                (H45)
 290-294  F5.3  mag     Hpscat    ? Scatter on Hpmag                       (H46)
 296-298  I3    ---   o_Hpmag     ? Number of observations for Hpmag       (H47)
     300  A1    ---   m_Hpmag    *[A-Z*-] Reference flag for Hpmag         (H48)
 302-306  F5.2  mag     Hpmax     ? Hpmag at maximum (5th percentile)      (H49)
 308-312  F5.2  mag     HPmin     ? Hpmag at minimum (95th percentile)     (H50)
 314-320  F7.2  d       Period    ? Variability period (days)              (H51)
     322  A1    ---     HvarType *[CDMPRU]? variability type               (H52)
     324  A1    ---     moreVar  *[12] Additional data about variability   (H53)
     326  A1    ---     morePhoto [ABC] Light curve Annex                  (H54)
 328-337  A10   ---     CCDM      CCDM identifier                          (H55)
     339  A1    ---   n_CCDM     *[HIM] Historical status flag             (H56)
 341-342  I2    ---     Nsys      ? Number of entries with same CCDM       (H57)
 344-345  I2    ---     Ncomp     ? Number of components in this entry     (H58)
     347  A1    ---     MultFlag *[CGOVX] Double/Multiple Systems flag     (H59)
     349  A1    ---     Source   *[PFILS] Astrometric source flag          (H60)
     351  A1    ---     Qual     *[ABCDS] Solution quality                 (H61)
 353-354  A2    ---   m_HIP       Component identifiers                    (H62)
 356-358  I3    deg     theta     ? Position angle between components      (H63)
 360-366  F7.3  arcsec  rho       ? Angular separation between components  (H64)
 368-372  F5.3  arcsec  e_rho     ? Standard error on rho                  (H65)
 374-378  F5.2  mag     dHp       ? Magnitude difference of components     (H66)
 380-383  F4.2  mag   e_dHp       ? Standard error on dHp                  (H67)
     385  A1    ---     Survey    [S] Flag indicating a Survey Star        (H68)
     387  A1    ---     Chart    *[DG] Identification Chart                (H69)
     389  A1    ---     Notes    *[DGPWXYZ] Existence of notes             (H70)
 391-396  I6    ---     HD        [1/359083]? HD number <III/135>          (H71)
 398-407  A10   ---     BD        Bonner DM <I/119>, <I/122>               (H72)
 409-418  A10   ---     CoD       Cordoba Durchmusterung (DM) <I/114>      (H73)
 420-429  A10   ---     CPD       Cape Photographic DM <I/108>             (H74)
 431-434  F4.2  mag     (V-I)red  V-I used for reductions                  (H75)
 436-447  A12   ---     SpType    Spectral type                            (H76)
     449  A1    ---   r_SpType   *[1234GKSX]? Source of spectral type      (H77)
--------------------------------------------------------------------------------
Note on Proxy: this flag provides a coarse indication of the presence
     of nearby objects within 10arcsec of the given entry.
     If non-blank, it indicates that 
     'H' there is one or more distinct Hipparcos Catalogue entries, 
         or distinct components of system from h_dm_com.dat
     'T' there is one or more distinct Tycho entries
     If 'H' and 'T' apply, 'H' is adopted.
     The 'T' flag implies either an inconsistency between the Hipparcos
     and Tycho catalogues, or a deficiency in one or both of the 
     catalogues.
Note on RAdeg, DEdeg: right ascension and declination are
     expressed in degrees for epoch J1991.25 (JD2448349.0625 (TT)) in the
     ICRS (International Celestial Reference System, consistent with
     J2000) reference system.
     There are 263 cases where these fields are missing (no astrometric
     solution could be found)
Note on pmRA, pmDE:
     The proper motions refer to the ICRS and to the epoch J1991.25.
Note on e_RAdeg, e_DEdeg:
     The standard errors refer to the epoch J1991.25, and represent a
     minimum of the error on the position. The actual standard error
     on the positions is increasing for epochs increasingly differing
     from the nominal J1991.25 epoch.
Note on VarFlag: the values are
     1: < 0.06mag ; 2: 0.06-0.6mag ; 3: >0.6mag
Note on r_Vmag: the source is
     G = ground-based, H=HIP, T=Tycho
Note on AstroRef: this flag indicates that the astrometric parameters in H3-4
     and H8-30 refer to:
     A to Z: the letter indicates the component of a double or multiple system
     *: the photocentre of a double or multiple system
     +: the centre of mass
Note on F2: values exceeding +3 indicate a bad fit to the data.
Note on m_BTmag: this flag indicates the component or combined photometry:
     A to Z : the letter indicates the component measured in Tycho
              (non-single star)
     * : the photometry refers to all components of the Hipparcos entry
     - : single-pointing triple or quadruple system
Note on r_V-I: the origin of the V-I colour, in summary:
     'A'        for an observation of V-I in Cousins' system;
     'B' to 'K' when V-I derived from measurements in other
                bands/photoelectric systems
     'L' to 'P' when V-I derived from Hipparcos and Star Mapper photometry
     'Q'        for long-period variables
     'R' to 'T' when colours are unknown
Note on Hpmag, e_Hpmag:
     the Hipparcos magnitude could not be determined for 14 stars.
Note on m_Hpmag: this flag indicates for double or multiple entries:
     A to Z : the letter indicates the specified component measured
     * : combined Hpmag of a double system, corrected for attenuation
     - : combined Hpmag of a multiple system, not corrected for attenuation
Note on HvarType: Hipparcos-defined type of variability (a blank entry
     signifies that the entry could not be classified as variable or constant):
     C : no variability detected ("constant")
     D : duplicity-induced variability
     M : possibly micro-variable (amplitude < 0.03mag)
     P : periodic variable
     R : V-I colour index was revised due to variability analysis
     U : unsolved variable which does not fall in the other categories
Note on moreVar: more data about periodic variability are provided
Note on n_CCDM: the flag takes the following values:
     H : determined multiple by Hipparcos, previously unknown
     I : system previously identified as multiple in HIC <I/196> (annex1)
     M : miscellaneous (system identified after publication of HIC)
Note on MultFlag: indicates that further details are given in the Double
     and Multiple Systems Annex:
     C : solutions for the components
     G : acceleration or higher order terms
     O : orbital solutions
     V : variability-induced movers (apparent motion arises from variability)
     X : stochastic solution (probably astrometric binaries with short period)
Note on Source: qualifies the source of the astrometric parameters H8-30
        with a 'C' in MultFlag:
     P : primary target of a 2- or 3-pointing system
     F : secondary or tertiary of a 2- or 3-pointing 'fixed' system
         (common parallax and proper motions)
     I : secondary or tertiary of a 2- or 3-pointing 'independent' system
         (no constraints on parallax or proper motions)
     L : secondary or tertiary of a 2- or 3-pointing 'linear' system
         (common parallax)
     S : astrometric parameters from 'single-star merging' process.
Note on Qual: Reliability of the double or multiple star solution:
        A=good, B=fair, C=poor, D=uncertain, S=suspected non-single
Note on Chart: the chart was produced:
     D : from the STScI Digitized Sky Survey
     G : from the Guide Star Catalog
Note on Notes: the flag has the following meaning:
     D : double and multiple systems note only (note in hd_notes.doc file)
     G : general note only (note in hg_notes.doc file)
     P : photometric notes only (note in hp_notes.doc file)
     W : D + P
     X : D + G
     Y : G + P
     Z : D + G + P
Note on r_SpType: the flag indicates the source, as:
     1 : Michigan catalogue for the HD stars, vol. 1 (Houk+, 1975) <III/31>
     2 : Michigan catalogue for the HD stars, vol. 2 (Houk, 1978)  <III/51>
     3 : Michigan Catalogue for the HD stars, vol. 3 (Houk, 1982)  <III/80>
     4 : Michigan Catalogue for the HD stars, vol. 4 (Houk+, 1988) <III/133>
     G : updated after publication of the HIC <I/196>
     K : General Catalog of Variable Stars, 4th Ed. (Kholopov+ 1988) <II/214>
     S : SIMBAD data-base <http://cdsweb.u-strasbg.fr/Simbad.html>
     X : Miscellaneous
     A blank entry has no corresponding information.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: h_dm_com.dat
--------------------------------------------------------------------------------
   Bytes Format Units    Label    Explanations
--------------------------------------------------------------------------------
   1- 10  A10    ---     CCDM     CCDM number                              (DC1)
      12  I1     ---     S       *Solution identifier                      (DC2)
      14  A1     ---     Type    *[FIL]Type of solution                    (DC3)
      16  A1     ---     Source  *[CFN] Solution source                    (DC4)
      18  A1     ---     Qual    *[ABCD] Solution quality                  (DC5)
      20  A1     ---     Notes   *[DGPWXYZ] Existence of notes             (DC6)
      22  I1     ---     Nsys     Number of solutions for the system      (DCM1)
  24- 25  I2     ---     Ncomp    Number of components in this solution   (DCM2)
  27- 28  I2     ---     Nparm    Number of free parameters in solution   (DCM3)
  30- 31  I2     ---     Ncorr    Number of correlation records           (DCM4)
  33- 36  A4     ---     ---      [COMP] This field contains the word COMP(DCM5)
  38- 39  I2     ---     seq      Sequential component number             (DCM6)
      41  A1     ---     comp_id  Component identifier                     (DC7)
  43- 48  I6     ---     HIP      HIP number                               (DC8)
  50- 55  F6.3   mag     Hp       Magnitude of component                   (DC9)
  57- 61  F5.3   mag   e_Hp       Standard error of Hp magnitude          (DC10)
  63- 68  F6.3   mag     BT       ? Magnitude of component, BT            (DC11)
  70- 74  F5.3   mag   e_BT       ? Standard error of BT                  (DC12)
  76- 81  F6.3   mag     VT       ? Magnitude of component, VT            (DC13)
  83- 87  F5.3   mag   e_VT       ? Standard error of VT                  (DC14)
  89-100  F12.8  deg     RAdeg    alpha, degrees (ICRS, Epoch=J1991.25)   (DC15)
 102-113  F12.8  deg     DEdeg    delta, degrees (ICRS, Epoch=J1991.25)   (DC16)
 115-121  F7.2   mas     Plx      Trigonometric parallax                  (DC17)
 123-130  F8.2 mas/yr    pmRA     Proper motion in mu_alpha.cos(delta)ICRS(DC18)
 132-139  F8.2 mas/yr    pmDE     Proper motion in mu_delta in ICRS       (DC19)
 141-146  F6.2   mas   e_RAdeg    Standard error in RA*cos(DEdeg)         (DC20)
 148-153  F6.2   mas   e_DEdeg    Standard error in DE                    (DC21)
 155-160  F6.2   mas   e_Plx      Standard error in Plx                   (DC22)
 162-167  F6.2 mas/yr  e_pmRA     Standard error in pmRA                  (DC23)
 169-174  F6.2 mas/yr  e_pmDE     Standard error in pmDE                  (DC24)
     176  A1     ---     ref      Reference component for following data  (DC25)
 178-184  F7.3   deg     theta   *? Position angle                        (DC26)
 186-193  F8.3  arcsec   rho      ? Separation from reference component   (DC27)
 195-202  F8.3 deg/yr    d.theta  ? Rate of change of theta               (DC28)
 204-209  F6.3 arcsec/yr d.rho    ? Rate of change of separation          (DC29)
 211-212  I2     ---     seq_ref *Sequential record number                (DCM7)
 214-238  A25     ---    flag    *Status flags for parameters             (DCM8)
--------------------------------------------------------------------------------
Note on S: a digit identifies different solutions pertaining to the
     same CCDM number.
Note on Type: Summary of double or multiple star solution:
     F: fixed double or multiple system
        (identical proper motions and parallaxes)
     I: individual parallaxes and linear (relative) motion
        (possible optical double star)
     L: linear double or multiple system
        (may have different proper motions but assumed to have same parallax)
Note on Source: the source of the solution is given by this flag:
     C: combined FAST and NDAC solution
     F: solution taken from the FAST Consortium only
     N: solution taken from the NDAC Consortium only
Note on Qual: Reliability of the double or multiple star solution:
        A=good  B=fair  C=poor   D=uncertain
Note on Notes: the flag has the following meaning:
     D : double and multiple systems note only (note in hd_notes.doc file)
     G : general note only (note in hg_notes.doc file)
     P : photometric notes only (note in hp_notes.doc file)
     W : D + P
     X : D + G
     Y : G + P
     Z : D + G + P
Note on theta: position angle relative to reference component
Note on seq_ref: Sequential record number for the reference component, this
     field is set to zero if DC25 is blank.
Note on flag: Status flags for Hp, RAdeg, DEdeg, Plx, pmRA, pmDE.
     1 = estimated,
     0 = constrained to the value of the first component.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: h_dm_cor.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label    Explanations
--------------------------------------------------------------------------------
   1- 10  A10    ---    CCDM     CCDM number                               (DC1)
      12  I1     ---    S       *Solution identifier                       (DC2)
      14  A1     ---    Type    *[FIL]Type of solution                     (DC3)
      16  A1     ---    Source  *[CFN] Solution source                     (DC4)
      18  A1     ---    Qual    *[ABCD] Solution quality                   (DC5)
      20  A1     ---    Notes   *[DGPWXYZ] Existence of notes              (DC6)
      22  I1     ---    Nsys     Number of solutions for the system       (DCM1)
  24- 25  I2     ---    Ncomp    Number of components in this solution    (DCM2)
  27- 28  I2     ---    Nparm    Number of free parameters in solution    (DCM3)
  30- 31  I2     ---    Ncorr    Number of correlation records            (DCM4)
  33- 36  A4     ---    ---      [CORR] This field contains the word CORR (DCM5)
  38- 39  I2     ---    seq      Sequential component number              (DCM6)
  41- 238 66I3   ---    corr    *[-99/999]? Correlation coefficients      (DCM7)
--------------------------------------------------------------------------------
Note on S: a digit identifies different solutions pertaining to the
     same CCDM number.
Note on Type: Summary of double or multiple star solution:
     F: fixed double or multiple system
        (identical proper motions and parallaxes)
     I: individual parallaxes and linear (relative) motion
        (possible optical double star)
     L: linear double or multiple system
        (may have different proper motions but assumed to have same parallax)
Note on Source: the source of the solution is given by this flag:
     C: combined FAST and NDAC solution
     F: solution taken from the FAST Consortium only
     N: solution taken from the NDAC Consortium only
Note on Qual: Reliability of the double or multiple star solution:
        A=good  B=fair  C=poor   D=uncertain
Note on Notes: the flag has the following meaning:
     D : double and multiple systems note only (note in hd_notes.doc file)
     G : general note only (note in hg_notes.doc file)
     P : photometric notes only (note in hp_notes.doc file)
     W : D + P
     X : D + G
     Y : G + P
     Z : D + G + P
Note on corr: the correlation records contain the correlation coefficients among
     the maximum set of 6N_C parameters. The number of correlation coefficients
     is 6N_C(6N_C-1)/2=66, 153 and 276 for N_C=2,3,4. A correlation record
     contains up to 66 coefficients; thus respectively 1,3 and 5 records are
     needed for a double, triple or quadruple star. The correlation coefficients
     are coded as integers between -99 and 999 using the arcsine
     transformation. The order of the correlation coefficients is indicated by
     the following table:
            Hp1 RA1 DE1 Plx1 pmRA1 pmDE1  Hp2 RA2 DE2 Plx2 pmRA2 pmDE2  Hp3 ...
     Hp1    1   r1  r2   r4   r7    r11   r16 r22 r29  r37  r46   r56   r67 ...
     RA1    r1  1   r3   r5   r8    r12   r17 r23 r30  r38  r47   r57   r68 ...
     DE1    r2  r3  1    r6   r9    r13   r18 r24 r31  r39  r48   r58   r69 ...
     Plx1   r4  r5  r6   1    r10   r14   r19 r25 r32  r40  r49   r59   r70 ...
     pmRA1  r7  r8  r9   r10  1     r15   r20 r26 r33  r41  r50   r60   r71 ...
     pmDE1  r11 r12 r13  r14  r15   1     r21 r27 r34  r42  r51   r61   r72 ...
     Hp2    r16 r17 r18  r19  r20   r21   1   r28 r35  r43  r52   r62   r73 ...
     RA2    r22 r23 r24  r25  r26   r27   r28 1   r36  r44  r53   r63   r74 ...
     DE2    r29 r30 r31  r32  r33   r34   r35 r36 1    r45  r54   r64   r75 ...
     Plx2   r37 r38 r39  r40  r41   r42   r43 r44 r45  1    r55   r65   r76 ...
     pmRA2  r46 r47 r48  r49  r50   r51   r52 r53 r54  r55  1     r66   r77 ...
     pmDE2  r56 r57 r58  r59  r60   r61   r62 r63 r64  r65  r66   1     r78 ...
     Hp3    r67 r68 r69  r70  r71   r72   r73 r74 r75  r76  r77   r78   1  ...
     ...    ... ... ...  ...  ...   ...   ... ... ...  ...  ...  ...   ... ...
     These correlation coefficients are written as 66I3
--------------------------------------------------------------------------------

Byte-by-byte Description of file: hip_dm_g.dat
--------------------------------------------------------------------------------
   Bytes Format Units     Label  Explanations
--------------------------------------------------------------------------------
   1-  6  I6    ---       HIP    Identifier (HIP number)                   (DG1)
   8- 14  F7.2 mas/yr2    gRA   *Acceleration gRA = d(pmRA)/dt             (DG2)
  16- 22  F7.2 mas/yr2    gDE   *Acceleration gDE = d(pmDE)/dt             (DG3)
  24- 30  F7.2 mas/yr2 e_gRA     Standard error of gRA                     (DG4)
  32- 38  F7.2 mas/yr2 e_gDE     Standard error of gDE                     (DG5)
  40- 44  F5.2  ---      Fg     *Significance of the g terms               (DG6)
  46- 52  F7.2 mas/yr3   dgRA   *? dgRA = d2(pmRA)/dt2                     (DG7)
  54- 60  F7.2 mas/yr3   dgDE   *? dgDE = d2(pmDE)/dt2                     (DG8)
  62- 68  F7.2 mas/yr3 e_dgRA    ? Standard error of dgRA                  (DG9)
  70- 76  F7.2 mas/yr3 e_dgDE    ? Standard error of dgDE                 (DG10)
  78- 82  F5.2  ---      Fdg    *? Signifance of the dg terms             (DG11)
      84  A1    ---      Notes  *[DGPWXYZ] Existence of notes             (DG12)
      86  I1    ---      num    *[7,9] Number of astrometric parameters   (DGM1)
  88-195  36I3  ---      corr   *[-99/999]? Correlation coefficients      (DGM2)
--------------------------------------------------------------------------------
Note on gRA: component in right ascension of the apparent acceleration
     of the photocentre at epoch J1991.25.
Note on gDE: component in declination of the apparent acceleration
     of the photocentre at epoch J1991.25.
Note on Fg: the quadratic model is only adopted if the g terms
     are significant (Fg>3.44)
Note on dgRA: component in right ascension of the rate of change of the
     apparent acceleration of the photocentre at epoch J1991.25.
Note on dgDE: component in declination of the rate of change of the
     apparent acceleration of the photocentre at epoch J1991.25.
Note on Fdg: The cubic model is only adopted if the dg terms are
     significant (Fdg>3.44)
Note on Notes: the flag has the following meaning:
     D : double and multiple systems note only (note in hd_notes.doc file)
     G : general note only (note in hg_notes.doc file)
     P : photometric notes only (note in hp_notes.doc file)
     W : D + P
     X : D + G
     Y : G + P
     Z : D + G + P
Note on num: for a quadratic model of the photocentric motion this
     parameter is 7, for a cubic model it is 9.
Note on corr: the complete set of n(n-1)*0.5 correlation coefficients
     (where n=7 for a quadratic  and n=9 for a cubic model of the
     photocentric motion) is given in the order indicated by the
     following table:
              RA   Dec  Plx  pmRA pmDE gRA  gDE  dgRA dgDE
     RA       1    r1   r2   r4   r7   r11  r16  r22  r29
     Dec      r1   1    r3   r5   r8   r12  r17  r23  r30
     Plx      r2   r3   1    r6   r9   r13  r18  r24  r31
     pmRA     r4   r5   r6   1    r10  r14  r19  r25  r32
     pmDE     r7   r8   r9   r10  1    r15  r20  r26  r33
     gRA      r11  r12  r13  r14  r15  1    r21  r27  r34
     gDE      r16  r17  r18  r19  r20  r21  1    r28  r35
     dgRA     r22  r23  r24  r25  r26  r27  r28  1    r36
     dgDE     r29  r30  r31  r32  r33  r34  r35  r36  1
--------------------------------------------------------------------------------

Byte-by-byte Description of file: hip_dm_o.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  6  I6    ---      HIP      Identifier (HIP)                         (D01)
   8- 17  F10.4 d        P        Orbital period                           (DO2)
  19- 29  F11.4 d        T       *Time of periastron passage               (DO3)
  31- 38  F8.2  mas      a0       Semi-major axis of photocentric orbit    (DO4)
  40- 45  F6.4  ---      ecc      [0,1] Eccentricity                       (DO5)
  47- 52  F6.2  deg      w       *[0,360] Argument of periastron           (DO6)
  54- 59  F6.2  deg      i       *[0,180] Inclination                      (DO7)
  61- 66  F6.2  deg      Omega   *[0,360] Position angle of the node       (DO8)
  68- 75  F8.4  d      e_P        ? Standard error of P                    (DO9)
  77- 85  F9.4  d      e_T        ? Standard error of T                   (DO10)
  87- 91  F5.2  mas    e_a0       ? Standard error of a0                  (DO11)
  93- 98  F6.4  ---    e_ecc      ? Standard error of ecc                 (DO12)
 100-105  F6.2  deg    e_w        ? Standard error of w                   (DO13)
 107-112  F6.2  deg    e_i        ? Standard error of i                   (DO14)
 114-119  F6.2  deg    e_Omega    ? Standard error of Omega               (DO15)
 121-123  I3    ---      dmRef   *? reference to the literature           (DO16)
     125  A1    ---      Notes   *[DGPWXYZ] Existence of notes            (DO17)
 127-138  A12   ---      flag    *Status flags for the parameters         (DOM1)
 140-337  66I3  ---      corr    *[-99/999]?=450 Correlation coefficients (DOM2)
--------------------------------------------------------------------------------
Note on T: this is the date when the photocentre is closest to the
     centre of mass in the orbital plane. It is equivalent to the
     closest approach of the stellar components.
Note on w: this is the angle in the orbital plane from the line of
     nodes to the major axis, measured from the nodal point (DO8) to
     the periastron in the direction of motion.
Note on i: the inclination of the orbital plane to the tangent plane
     of the sky.  Taken to be in the first quadrant if the apparent
     motion is direct (counter-clockwise) and in the second quadrant
     for retrograde (clockwise) apparent motion.
Note on Omega: This is the position angle (measured counter-clockwise
     as seen on the sky from the +Dec direction) of the line of nodes,
     or the intersection of the orbital and tangent planes. If the
     radial motion of the components is known from spectroscopic studies,
     then Omega should give the position angle of the ascending node,
     at which the primary star crosses the tangent plane while receding
     from the observer. In the absence of spectroscopic information
     Omega refers to the mode with the smallest positive position angle.
Note on dmRef: A reference number in this field points to references in the
     printed catalogue, explained in dmsa_o.doc file.
Note on Notes: the flag has the following meaning:
     D : double and multiple systems note only (note in hd_notes.doc file)
     G : general note only (note in hg_notes.doc file)
     P : photometric notes only (note in hp_notes.doc file)
     W : D + P
     X : D + G
     Y : G + P
     Z : D + G + P
Note on flag: status flags for the 12 astrometric and orbital
     parameters taken in the order indicated below.
     1= estimated; 0= not estimated.
Note on corr: the correlation coefficients in bytes 140-337 are given
     in the table below. Correlation coefficients which are undefined
     (corresponding to blanks in DO9-15, and a status flag=0 in
     DOB127) are set to zero. All correlation coefficients are coded
     as integers between -99 and 999 using the arcsine transformation.
     Undefined values are coded as 450.
           RA   Dec  Plx  pmRA pmDE  P    T   a0    e    w    i Omega
     RA    1    r1   r2   r4   r7   r11  r16  r22  r29  r37  r46 r56
     Dec   r1   1    r3   r5   r8   r12  r17  r23  r30  r36  r47 r57
     Plx   r2   r3   1    r6   r9   r13  r18  r24  r31  r37  r46 r58
     pmRA  r4   r5   r6   1    r10  r14  r19  r25  r32  r38  r47 r59
     pmDE  r7   r8   r9   r10  1    r15  r20  r26  r33  r39  r48 r60
     P     r11  r12  r13  r14  r15  1    r21  r27  r34  r40  r49 r61
     T     r16  r17  r18  r19  r20  r21  1    r28  r35  r41  r50 r62
     a0    r22  r23  r24  r25  r26  r27  r28  1    r36  r42  r51 r63
     e     r29  r30  r31  r32  r33  r34  r35  r36  1    r43  r52 r64
     w     r37  r38  r39  r40  r41  r42  r43  r44  r45  1    r53 r65
     i     r46  r47  r48  r49  r50  r51  r52  r53  r54  r55  1   r66
     Omega r56  r57  r59  r59  r60  r61  r62  r63  r64  r65  r66 1
     These correlation coefficients are written as 66I3
--------------------------------------------------------------------------------

Byte-by-byte Description of file: hip_dm_v.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  6  I6    ---      HIP      Identifier (HIP)                         (DV1)
   8- 12  F5.2  mag      Hp_ref  *Reference magnitude                      (DV2)
  14- 20  F7.2  mas      DRA      VIM element in right ascension           (DV3)
  22- 28  F7.2  mas      DDE      VIM element in declination               (DV4)
  30- 36  F7.2  mas    e_DRA      Standard error of DRA                    (DV5)
  38- 44  F7.2  mas    e_DDE      Standard error of DDE                    (DV6)
  46- 50  F5.2  ---      FD      *Significance of the VIM elements         (DV7)
  52- 57  F6.2  deg      theta_C *Position angle of the constant component (DV8)
  59- 64  F6.2  deg    e_theta_C  Standard error of theta_C                (DV9)
  66- 71  F6.1  mas      minSep   Lower limit for separation of binary    (DV10)
  73- 78  F6.1  mas      dvar    *Displacement of photocentre             (DV11)
      80  A1    ---      Notes   *[DGPWXYZ] Existence of notes            (DV12)
  82-144  21I3  ---      corr    *[-99/999]Correlation coefficients       (DVM1)
--------------------------------------------------------------------------------
Note on Hp_ref: the reference magnitude is freely chosen and defines the
     reference point for the object. The positional parameters RA and Dec (H8,
     H9 in hip_main.dat) and the VIM elements DV3,DV4 depend on the chosen
     Hp_ref. DV7-11 do not depend on Hp_ref.
Note on FD: The VIM solution is only accepted if FD>2.15
Note on theta_C: position angle of the constant component of the binary with
     respect to the variable component, measured counterclockwise as seen on
     the sky from the +Dec direction.
Note on dvar: displacement of photocentre between minimum and maximum
     luminosity of the system. Indicates the size of the VIM effect.
Note on Notes: the flag has the following meaning:
     D : double and multiple systems note only (note in hd_notes.doc file)
     G : general note only (note in hg_notes.doc file)
     P : photometric notes only (note in hp_notes.doc file)
     W : D + P
     X : D + G
     Y : G + P
     Z : D + G + P
Note on corr: the correlation coefficients in bytes 82-144 are given in the
     following sequence:
           RA   Dec  Plx  pmRA pmDE DRA  DDE
     RA    1    r1   r2   r4   r7   r11  r16
     Dec   r1   1    r3   r5   r8   r12  r17
     Plx   r2   r3   1    r6   r9   r13  r18
     pmRA  r4   r5   r6   1    r10  r14  r19
     pmDE  r7   r8   r9   r10  1    r15  r20
     DRA   r11  r12  r13  r14  r15  1    r21
     DDE   r16  r17  r18  r19  r20  r21  1
     These correlation coefficients are written as 21I3
-------------------------------------------------------------------------------

Byte-by-byte Description of file: hip_dm_x.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  6  I6    ---     HIP       Identifier (HIP)                         (DX1)
   8- 13  F6.2  mas     epsilon   Cosmic error, epsilon                    (DX2)
  15- 20  F6.2  mas   e_epsilon   Standard error of epsilon                (DX3)
      22  A1    ---     Notes    *[DGPWXYZ] Existence of notes             (DX4)
--------------------------------------------------------------------------------
Note on Notes: the flag has the following meaning:
     D : double and multiple systems note only (note in hd_notes.doc file)
     G : general note only (note in hg_notes.doc file)
     P : photometric notes only (note in hp_notes.doc file)
     W : D + P
     X : D + G
     Y : G + P
     Z : D + G + P
--------------------------------------------------------------------------------

Byte-by-byte Description of file: hip_va_1.dat
--------------------------------------------------------------------------------
   Bytes Format Units Label       Explanations
--------------------------------------------------------------------------------
   1-  6  I6    ---   HIP         Identifier (HIP)                          (P1)
       8  A1    ---   NewVar      [*] Flag if new variable                  (P2)
  10- 21  A12   ---   SpType      Spectral type                             (P3)
      23  A1    ---   HvarType   *[CDMPRU] Variability type (1-letter)      (P4)
  25- 30  A6    ---   VarType    *Variability type as in GCVS/NSV           (P5)
      32  A1    --- n_VarType     [*] Flag if newly classified by Hipparcos (P6)
  34- 39  F6.3  mag   maxMag      Magnitude at max from curve fitting       (P7)
      41  A1    --- l_minMag     *[>] Limit flag (>)                        (P8)
  43- 48  F6.3  mag   minMag      Magnitude at min from curve fitting       (P9)
  50- 55  F6.1  ---   log(sA/A)   ? log_10(sigma_A / A)                    (P10)
  57- 68  F12.7 d     Period      ? Mean period in days                    (P11)
  70- 75  F6.1  [d]   log(sP)     ? log_10(sigma_P)                        (P12)
  77- 85  F9.4  d     Ep-2440000  ? Epoch (JD-2440000) of zero phase       (P13)
      87  I1    --- q_Ep-2440000 *[0/5]? Precision flag                    (P14)
      89  A1    ---   morePhoto   [ABC] Light curve Annex                  (P15)
      91  A1    ---   Notes      *[DGPWXYZ] Existence of notes             (P16)
  93-104  A12   ---   VarName     Variable star name                       (P17)
 106-115  F10.5 d     period      ? Period from literature                 (P18)
 117-126  F10.2 d     epoch       ? Epoch  from literature                 (P19)
 128-132  F5.2  mag   max         ? Magnitude at max from literature       (P20)
 134-138  F5.2  mag   min         ? Magnitude at min from literature       (P21)
     140  A1    ---   Band       *[UBVKIRPYb] Photometric band             (P22)
     142  A1    ---   refFlag     [R] Reference in printed catalogue       (P23)
--------------------------------------------------------------------------------
Note on HvarType: Hipparcos-defined type of variability:
     C : no variability detected ("constant")
     D : duplicity-induced variability
     M : possibly micro-variable (amplitude < 0.03mag)
     P : periodic variable
     R : V-I colour index was revised due to variability analysis
     U : unsolved variable which does not fall in the other categories
Note on VarType: this is the 6-letter type defined
        in the General Catalog of Variable Stars <II/214>
        (see also the "Types of Variability" section below)
Note on l_minMag: the flag (>) indicates that the true magnitude at minimum
     luminosity is likely to be larger than the value of minMag given in P9.
Note on q_Ep-2440000: the value is 1-log10(sigma_epoch), i.e.
     0 for an accuracy of about 10 days,
     1 for an accuracy of about 1 day,
     2 for an accuracy of about 0.1day,
     3 for an accuracy of about 0.01day,
     4 for an accuracy of about 0.001day,
     5 for an accuracy of about 0.0001day.
Note on Notes: the flag has the following meaning:
     D : double and multiple systems note only (note in hd_notes.doc file)
     G : general note only (note in hg_notes.doc file)
     P : photometric notes only (note in hp_notes.doc file)
     W : D + P
     X : D + G
     Y : G + P
     Z : D + G + P
Note on Band: U,B,V,K,I,R refer to Johnson system, or closely related
     systems; P refers to photographic magnitudes, Y and b for the
     Stroemgren y and b bands.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: hip_va_2.dat
--------------------------------------------------------------------------------
   Bytes Format Units  Label      Explanations
--------------------------------------------------------------------------------
   1-  6  I6    ---    HIP        Identifier (HIP number)                   (U1)
       8  A1    ---    NewVar     [*] Flag if new variable                  (U2)
  10- 21  A12   ---    SpType     Spectral type                             (U3)
      23  A1    ---    HvarType  *[CDMPRU] Variability type (1-letter)      (U4)
  25- 30  A6    ---    VarType   *Variability type (6-letter) as in GCVS/NSV(U5)
      32  A1    ---  n_VarType    [*] Flag if newly classified by Hipparcos (U6)
  34- 39  F6.3  mag    maxMag    *Magnitude at max from curve fitting       (U7)
      41  A1    ---  l_minMag     [>] Limit flag (>)                        (U8)
  43- 48  F6.3  mag    minMag    *Magnitude at min from curve fitting       (U9)
  50- 55  F6.3  mag    med_Hp     Median Hp                                (U10)
  57- 68  F12.3 mag    A          Intrinsic variability amplitude          (U11)
  70- 75  F6.3  mag  e_A          Standard error of A                      (U12)
  77- 85  A9    ---    ---        ? Blank for unsolved variables           (U13)
      87  A1    ---    ---        ? Blank for unsolved variables           (U14)
      89  A1    ---    morePhoto  [ABC] Light curve Annex                  (U15)
      91  A1    ---    Notes     *[DGPWXYZ] Notes                          (U16)
  93-104  A12   ---    VarName    Variable star name                       (U17)
 106-115  F10.5 d      period     ? Period from literature                 (U18)
 117-126  F10.2 d      Ep-2440000 ? Epoch (JD-2440000) from literature     (U19)
 128-132  F5.2  mag    max        ? Magnitude at max from literature       (U20)
 134-138  F5.2  mag    min        ? Magnitude at min from literature       (U21)
     140  A1    ---    Band      *[UBVKIRPYb] Photometric band             (U22)
     142  A1    ---    refFlag    [R] Reference in printed catalogue       (U23)
--------------------------------------------------------------------------------
Note on HvarType: Hipparcos-defined type of variability:
     C : no variability detected ("constant")
     D : duplicity-induced variability
     M : possibly micro-variable (amplitude < 0.03mag)
     P : periodic variable
     R : V-I colour index was revised due to variability analysis
     U : unsolved variable which does not fall in the other categories
Note on VarType: this is the 6-letter type defined
        in the General Catalog of Variable Stars <II/214>
        (see also the "Types of Variability" section below)
Note on maxMag: this is given if significant
Note on minMag: this is given if significant
Note on Notes: Note on Notes: the flag has the following meaning:
     D : double and multiple systems note only (note in hd_notes.doc file)
     G : general note only (note in hg_notes.doc file)
     P : photometric notes only (note in hp_notes.doc file)
     W : D + P
     X : D + G
     Y : G + P
     Z : D + G + P
Note on Band: U,B,V,K,I,R refer to Johnson system, or closely related
     systems; P refers to photographic magnitudes, Y and b for the
     Stroemgren y and b bands.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: solar_ha.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label       Explanations
--------------------------------------------------------------------------------
   1-  3  I3    ---     ID          Object number                         (SHA1)
   5- 15  F11.7 deg     RAdeg       Reference point RA  (ICRS system)     (SHA2)
  17- 27  F11.7 deg     DEdeg       Reference point Dec (ICRS system)     (SHA3)
  29- 41  F13.7 d       Ep-2440000 *Measurement epoch                     (SHA4)
  43- 47  F5.2  s       delay      *Light delay time                      (SHA5)
  49- 55  F7.3  deg     theta      *Position angle, theta                 (SHA6)
  57- 62  F6.2  mas   e_lambda      Estimated standard error of abscissa  (SHA7)
      64  I1    ---     flag       *[1,2]FAST or NDAC flag                (SHA8)
--------------------------------------------------------------------------------
Note on Ep-2440000: the measurement epoch is specified in JD with respect to
     JD(TT)2440000.0 and is corrected to the geocentre.
Note on delay: this gives the applied light time delay in the geocentric
     direction of the observed object between the satellite and the Earth.
Note on theta: The position angle of the slit coordinate direction w is
     reckoned positive from North through East.
Note on flag: If the transit corresponds to an NDAC record the flag is 1.
     For a FAST record the flag is 2.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: solar_hp.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label       Explanations
--------------------------------------------------------------------------------
   1-  3  I3    ---     ID          Object number                         (SHP1)
   5- 15  F11.5 d       Ep-2440000 *Measurement epoch                     (SHP2)
  17- 23  F7.4  mag     Hp_dc       Magnitude from unmodulated signal     (SHP3)
  25- 30  F6.4  mag   e_Hp_dc       Standard error on Hp_dc               (SHP4)
  32- 38  F7.4  mag     Hp_ac       Magnitude from modulated signal       (SHP5)
  40- 45  F6.4  mag   e_Hp_ac       Standard error on Hp_ac               (SHP6)
  47- 51  F5.3  AU      r           Distance: Sun-asteroid                (SHP7)
  53- 57  F5.3  AU      Delta       Distance: satellite-asteroid          (SHP8)
  59- 63  F5.2  deg     alpha      *Solar phase angle                     (SHP9)
--------------------------------------------------------------------------------
Note on Ep-2440000: the measurement epoch is specified in JD with respect
     to JD(TT)2440000.0 and is not corrected to the geocentre  (i.e. the
     light-time delay between the satellite and the earth is also neglected.
Note on alpha: the solar phase angle is the angle between the Sun and the
     satellite as viewed from the asteroid.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: solar_t.dat
--------------------------------------------------------------------------------
   Bytes Format Units  Label       Explanations
--------------------------------------------------------------------------------
   1-  3  I3    ---    ID          Object number                           (ST1)
   5- 17  F13.7 d      Ep-2440000 *Measurement epoch                       (ST2)
  19- 29  F11.7 deg    RAdeg       Right ascension (ICRS system)           (ST3)
  31- 41  F11.7 deg    DEdeg       Declination (ICRS system)               (ST4)
  43- 47  F5.2  mag    BTmag       ? Mean BT magnitude                     (ST5)
  49- 53  F5.2  mag    VTmag       ? Mean VT magnitude                     (ST6)
      55  I1    ---    Flag       *[1,2] Transit flag                      (ST7)
  57- 61  F5.1  mas  e_RAdeg       Standard error on RA                    (ST8)
  63- 67  F5.1  mas  e_DEdeg       Standard error on Dec                   (ST9)
  69- 73  F5.2  ---    DE/RA       Correlation, Dec/RA*cos(delta)         (ST10)
  75- 80  F6.2  deg    theta       Position angle of slit (direction w)   (ST11)
  82- 83  I2    ---    sign_z     *[-1/1] Inclined slit flag              (ST12)
  85- 89  F5.1  mas  e_incl        Standard error on slit pos. (inclined) (ST13)
  91- 95  F5.1  mas  e_vert        Standard error on slit pos. (vertical) (ST14)
--------------------------------------------------------------------------------
Note on Ep-2440000: the measurement epoch is specified in JD with respect
     to JD(TT)2440000.0 and is not corrected to the geocentre (i.e. the
     light-time delay between the satellite and the earth is also neglected.
Note on Flag: if flag =1 then only one crossing of the field of view has
     been detected or retained. If Flag n>1, then n candidate observed
     transits have been detected or retained for that predicted
     observation. ST1, ST2, ST7, ST11, ST12 are identical in those cases.
Note on sign_z: if the transit occurred in the upper branch of the
     inclined slits, the flag is +1, if the transit occurred in the
     lower branch of the inclined slits, the flag is -1.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: tyc_main.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
       1  A1    ---     Catalog   [T] Catalogue (T = Tycho)                 (T0)
   3- 14  A12   ---     TYC      *TYC1-3 (TYC number)                       (T1)
      16  A1    ---     Proxy     [HT]? Proximity flag                      (T2)
  18- 28  A11   ---     RAhms     Right ascension in h m s, ICRS (J1991.25) (T3)
  30- 40  A11   ---     DEdms     Declination in deg ' ", ICRS (J1991.25)   (T4)
  42- 46  F5.2  mag     Vmag      ? Magnitude in Johnson V                  (T5)
      48  A1    ---     ---       ? Blank for Tycho                         (T6)
      50  A1    ---   r_Vmag     *[BDTV] Source of magnitude                (T7)
  52- 63  F12.8 deg     RAdeg    *alpha, degrees (ICRS, Epoch=J1991.25)     (T8)
  65- 76  F12.8 deg     DEdeg    *delta, degrees (ICRS, Epoch=J1991.25)     (T9)
      78  A1    ---     AstroRef *[X]? Reference flag for astrometry       (T10)
  80- 86  F7.2  mas     Plx      *? Trigonometric parallax                 (T11)
  88- 95  F8.2 mas/yr   pmRA     *? Proper motion mu_alpha.cos(delta), ICRS(T12)
  97-104  F8.2 mas/yr   pmDE     *? Proper motion mu_delta, ICRS           (T13)
 106-111  F6.2  mas   e_RAdeg    *? Standard error in RA*cos(delta)        (T14)
 113-118  F6.2  mas   e_DEdeg    *? Standard error in DE                   (T15)
 120-125  F6.2  mas   e_Plx      *? Standard error in Plx                  (T16)
 127-132  F6.2 mas/yr e_pmRA     *? Standard error in pmRA                 (T17)
 134-139  F6.2 mas/yr e_pmDE     *? Standard error in pmDE                 (T18)
 141-145  F5.2  ---     DE:RA     [-1/1]? Correlation, DE/RA*cos(delta)    (T19)
 147-151  F5.2  ---     Plx:RA    [-1/1]? Correlation, Plx/RA*cos(delta)   (T20)
 153-157  F5.2  ---     Plx:DE    [-1/1]? Correlation, Plx/DE              (T21)
 159-163  F5.2  ---     pmRA:RA   [-1/1]? Correlation, pmRA/RA*cos(delta)  (T22)
 165-169  F5.2  ---     pmRA:DE   [-1/1]? Correlation, pmRA/DE             (T23)
 171-175  F5.2  ---     pmRA:Plx  [-1/1]? Correlation, pmRA/Plx            (T24)
 177-181  F5.2  ---     pmDE:RA   [-1/1]? Correlation, pmDE/RA*cos(delta)  (T25)
 183-187  F5.2  ---     pmDE:DE   [-1/1]? Correlation, pmDE/DE             (T26)
 189-193  F5.2  ---     pmDE:Plx  [-1/1]? Correlation, pmDE/Plx            (T27)
 195-199  F5.2  ---     pmDE:pmRA [-1/1]? Correlation, pmDE/pmRA           (T28)
 201-203  I3    ---     Nastro    ? Number of transits for astrometry      (T29)
 205-209  F5.2  ---     F2       *? Goodness-of-fit parameter              (T30)
 211-216  I6    ---     HIP       ? Hipparcos HIP number                   (T31)
 218-223  F6.3  mag     BTmag     ? Mean BT magnitude                      (T32)
 225-229  F5.3  mag   e_BTmag     ? Standard error in BTmag                (T33)
 231-236  F6.3  mag     VTmag     ? Mean VT magnitude                      (T34)
 238-242  F5.3  mag   e_VTmag     ? Standard error in VTmag                (T35)
     244  A1    ---   r_BTmag    *[DMNT] Source of photometry              (T36)
 246-251  F6.3  mag     B-V       ? Johnson B-V colour                     (T37)
 253-257  F5.3  mag   e_B-V       ? Standard error on B-V                  (T38)
     259  A1    ---     ---       ? Blank for Tycho                        (T39)
     261  I1    ---     Q        *? Astrometric quality flag, Q            (T40)
 263-266  F4.1  ---     Fs        ? Signal-to-noise ratio of the star image(T41)
     268  A1    ---     Source   *[HPR] Source of astrometric data         (T42)
 270-272  I3    ---     Nphoto    ? Number of transits for photometry      (T43)
 274-278  F5.3  mag     VTscat    ? Estimate of VTmag scatter              (T44)
 280-284  F5.2  mag     VTmax     ? VTmag at maximum (15th percentile)     (T45)
 286-290  F5.2  mag     VTmin     ? VTmag at minimum (85th percentile)     (T46)
     292  A1    ---     Var      *[GN]? Known variability from GCVS/NSV    (T47)
     294  A1    ---     VarFlag  *[UVW]? Variability from Tycho            (T48)
     296  A1    ---     MultFlag *[DRSYZ]? Duplicity from Tycho            (T49)
     298  A1    ---     morePhoto [AB]  Epoch photometry in Annex A or B   (T50)
 300-301  A2    ---   m_HIP       CCDM component identifier                (T51)
 303-308  I6    ---     PPM      *[1/789676]? PPM and Supplement           (T52)
 310-315  I6    ---     HD        [1/359083]? HD cat. <III/135>            (T53)
 317-326  A10   ---     BD        Bonner DM <I/119>, <I/122>               (T54)
 328-337  A10   ---     CoD       Cordoba DM <I/114>                       (T55)
 339-348  A10   ---     CPD       Cape Photographic DM <I/108>             (T56)
     350  A1    ---     Remark   *[JKLM] Notes                             (T57)
--------------------------------------------------------------------------------
Note on TYC: the designation of an object in the Tycho Catalogue uses the
     Guide Star Catalog numbering system (a region number (TYC1) and a number
     within the region (TYC2)) followed by a Tycho specific component number
     (TYC3).
Note on r_Vmag: if non blank, the field has the following meaning:
     B : no VTmag available, therefore BTmag was adopted
     D : derived from approximate BTmag and VTmag (r_BTmag field T36 is 'D')
     T : derived from approximate VTmag (r_BTmag field T36 is 'T')
     V : no BTmag available, therefore VTmag was adopted in Vmag
Note on RAdeg, DEdeg: right ascension and declination are
     expressed in degrees for epoch J1991.25 (JD2448349.0625 (TT)) in the
      ICRS (International Celestial Reference System, close to
     J2000) reference system.
Note on AstroRef: 'X' indicates a dubious astrometric reference star
     in the context of the Tycho catalogue.
Note on Plx, pmRA, pmDE, e_RAdeg, e_DEdeg, e_Plx, e_pmRA, e_pmDE:
     For these fields the second decimal digit is always blank
Note on F2: values exceeding +2.5 to +3 indicate a bad fit to the data.
Note on r_BTmag: the source flag has the following meaning:
     D : approximate BTmag, VTmag obtained for resolved double stars
     M : BTmag and VTmag are median values rather than de-censored means
     N : BTmag and VTmag are de-censored means
     T : BTmag is not given, and VTmag is an estimate; these magnitudes
         are systematically too bright by up to 1mag.
     A blank indicates an Hipparcos star not observed by Tycho (T42 = H).
Note on Q: the astrometric quality flag is defined by the following table,
     where sigma(max) is the largest of the 5 astrometric standard errors:
   ---------------------------------------------------------
     Q  sigma(max)   Astrometric quality
   ---------------------------------------------------------
     1     <   5     very high
     2     5- 10     very high
     3    10- 25     high
     4    25- 50     high
     5    50-150     medium
     6     < 150     perhaps non-single
     7     < 150     low
     8     < 150     perhaps non-stellar
     9     ~ 200     low, position derived from TICR
                     ('R' in Source field T42)
   blank     ---     unassigned, 'H' in Source field T42
                     (Hipparcos star not observed by Tycho)
   ---------------------------------------------------------
Note on Source:
     H : Hipparcos star not observed by Tycho
     P : only the position was determined (no proper motion, no parallax)
     R : the position is derived from TICR catalog <I/197>
Note on Var: this flag is set when the variability is known:
     G : variable known in General Catalog of Variable Stars <II/214>
     N : variable known in New Suspected Variables catalog <II/140>
Note on VarFlag: this flag has the following meaning:
     U : apparent variability in the Tycho data; may be due to duplicity
     V : strong evidence of intrinsic variability
     W : suspected intrinsic variability
Note on MultFlag: unresolved duplicity status from Tycho data analysis:
     D : duplicity clearly indicated (BTmag and VTmag refer to combined light)
     R : duplicity weakly indicated, combined with indication of variability
     S : duplicity suspected
     Y : investigation for duplicity carried out on Tycho data,
         no indication of duplicity was found
     Z : investigation for duplicity not carried out
 blank : Hipparcos star not observed by Tycho
Note on PPM: from the 3 parts of the PPM catalogue
    North <I/146>, South <I/193>, and 90000Supplement <I/208>
Note on Remark: if non-blank, the remark has the following meaning:
     J : disagreement with position of magnitude in GSC1.1 catalog <I/220>
     K : dubious Tycho parallax (Plx)
     L : dubious Tycho proper motion (disagrees with PPM catalogue)
     M : very uncertain Tycho magnitude (standard error larger than 0.3mag)
--------------------------------------------------------------------------------

Byte-by-byte Description of file: hd_notes.doc hg_notes.doc hp_notes.doc
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  6  I6    ---     HIP       HIP number
       8  A1    ---     Note1     [DG] Double and multiple or General note
      10  A1    ---     Note2     [DP] Double and multiple or Photometric note
  12- 13  I2    ---     Ntot      Total number of lines for the HIP object
  15- 16  I2    ---     Nline     Running line number in range [1,Ntot]
  18- 97  A80   ---     Text      Text of note.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: hp_refs.doc
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  6  I6    ---     HIP       HIP number
   8-  9  I2    ---     Ntot      Total number of lines for the HIP object
  11- 12  I2    ---     Nline     Running line number in range [1,Ntot]
  14- 19  F6.3  ---     nRef      Reference number (explained in hp_auth.doc)
--------------------------------------------------------------------------------

Byte-by-byte Description of file: hp_auth.doc
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  6  F6.3  ---     nRef      Reference number from hp_refs.doc
   8- 77  A70   ---     Text      Text of reference
--------------------------------------------------------------------------------

Byte-by-byte Description of file: dmsa_o.doc
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  3  I3    ---     dmRef     Reference number (hip_dm_o.dat file)
       5  I1    ---     Ntot      Total number of lines for the reference
       7  I1    ---     Nline     Running line number in range [1,Ntot]
   9- 80  A72   ---     Text      Text of reference
--------------------------------------------------------------------------------

Types of Variability: the 6-letter codes for variability are:
  -----------------------------------------------------------------------------
  Code    Description                                         Class of Variable
  -----------------------------------------------------------------------------
  ACV     {alpha}^2^ Canum Venaticorum type (including ACVO)  rotating
  ACYG    {alpha} Cygni type                                  pulsating
  BCEP    {beta} Cephei type (including BCEPS)                pulsating
  BY      BY Draconis type                                    rotating
  CEP     Cepheids (including CEP(B))                         pulsating
  CST     constant stars (considered as variable by 
                                          some observer(s))   -
  CW      W Virginis type                                     pulsating
  CWA     W Virginis type (periods > 8 days)                  pulsating
  CWB     W Virginis type (periods < 8 days)                  pulsating
  DCEP    {delta} Cephei type (including DCEPS)               pulsating
  DSCT    {delta} Scuti type (including DSCTC)                pulsating
  E       (E+, E/..)                                          eclipsing binary
  EA      Algol type (EA+, EA/..)                             eclipsing binary
  EB      {beta} Lyrae type (EB/..)                           eclipsing binary
  ELL     rotating ellipsoidal (ELL+.. or/..)                 rotating
  EW      W Ursae Majoris type (EW/i..)                       eclipsing binary
  FKCOM   FK Comae Berenices type                             rotating
  GCAS    {gamma} Cassiopeiae type                            eruptive
  I       irregular (I, IA, IB, In, InT, Is)                  eruptive
  IN      irregular (INA, INAT, INB, INSA, INSB, INST, INT)   eruptive
  IS      irregular (ISA, ISB)                                eruptive
  L       slow irregular (L, LB, LC)                          pulsating
  M       Mira Ceti type                                      pulsating
  N       slow novae (NB, NC)                                 cataclysmic
  NA      fast novae                                          cataclysmic
  NL      nova-like                                           cataclysmic
  NR      recurrent novae                                     cataclysmic
  PVTEL   PV Telescopii type                                  pulsating
  RCB     R Coronae Borealis type                             eruptive
  RR      RR Lyrae type (RR, RRAB, RRB, RRC)                  pulsating
  RS      RS Canum Venaticorum type                           eruptive
  RV      RV Tauri type (RV, RVA, RVB)                        pulsating
  SARV    small-amplitude red variables                       pulsating/rotating
  SDOR    S Doradus type                                      eruptive
  SPB     slowly pulsating B stars                            pulsating
  SR      semi-regular (SR, SRA, SRB, SRC, SRD)               pulsating
  SXARI   SX Arietis type                                     rotating
  SXPHE   SX Phoenicis type                                   pulsating
  UV      UV Ceti type                                        eruptive
  WR      Wolf-Rayet                                          eruptive
  XNG     X-ray nova-like system                              X-ray binary
  XP      X-ray pulsar                                        X-ray binary
  ZAND    Z Andromedae type                                   cataclysmic
  -----------------------------------------------------------------------------

References:
  Perryman M.A.C., Lindegren L., Kovalevsky J., Hog E., Bastian U.,
    Bernacca P.L., Creze M., Donati F., Grenon M., Grewing M., 
    van Leeuwen F., van der Marel H., Mignard F., Murray C.A., 
    Le Poole R.S., Schrijver H., Turon C., Arenou F., Froeschle M., 
    Petersen C.S., "The Hipparcos Catalogue" (1997A&A...323L..49P)
  Lindegren L., Mignard F., Soederhjelm S., Badiali M., Bernstein H.H.,
    Lampens P., Pannunzio R., Arenou F., Bernacca P.L., Falin J.L.,
    Froeschle M., Kovalevsky J., Martin C., Perryman M.A.C., Wielen R.
    "Double star data in the Hipparcos Catalogue" (1997A&A...323L..53L)
  Hog E., Baessgen G., Bastian U., Egret D., Fabricius C., Grossmann V.,
    Halbwachs J.L., Makarov V.V., Perryman M.A.C., Schwekendiek P., 
    Wagner K., Wicenec A., "The Tycho Catalogue"  (1997A&A...323L..57H)
  van Leeuwen F., Evans D.W., Grenon M., Grossmann V., Mignard F.,
    Perryman M.A.C., "The Hipparcos mission: photometric data."
    (1997A&A...323L..61V)
================================================================================
(End)   M.Perryman [ESA], K.O'Flaherty [ESTEC], F.Ochsenbein [CDS]   11-Feb-1997
