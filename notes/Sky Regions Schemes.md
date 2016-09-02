# Sky Regions Schemes

## Calculating Polygons

### AST Polygon

Starlink AST software (C, Python)

* can calculate a polygon based on the FITS header alone
* with pixel data, can calculate a polygon to exclude values, e.g. NaN



### footprintfinder

Python 2.x script.

* <http://hla.stsci.edu/Footprintfinder/FootprintFinder.html>
* Code needs updating.
* Generates DS9 polygon files.


### Mangle

Link: <http://space.mit.edu/~molly/mangle/manual/pixelize.html>

- Only a command line program.
- All regions circle/sphere cross sections





## Region Indexing Schemes

### HEALPix

Pixel indexing.

Base shape: diamond

### Quad Tree Cube (Q3C)

The [Q3C PostgreSQL plugin](https://github.com/segasai/q3c) is based on this scheme.

Basic shape: square

[Download paper](https://listserv.slac.stanford.edu/cgi-bin/wa?A3=ind1505&L=QSERV-L&E=base64&P=262180&B=--------------090800060107040501010008&T=application%2Fpdf;%20name=%22351-0735.pdf%22&N=351-0735.pdf&attachment=q&XSS=3)

### HEALPix Multi-Order Coverage map (MOC)

Links:

* Specification: <http://www.ivoa.net/documents/MOC/>

### Google S2 (Hilbert curves)

<http://blog.christianperone.com/2015/08/googles-s2-geometry-on-the-sphere-cells-and-hilbert-curve/>

### Hierarchical Progressive Surveys (HiPS)

Links:

* <http://aladin.u-strasbg.fr/hips/>
* <http://www.cosmos.esa.int/web/esdc/esasky-skies>
* VO specification: <http://www.ivoa.net/documents/Notes/HiPS/>
* Journal paper: <http://cdsads.u-strasbg.fr/abs/2015A%26A...578A.114F>


Notes

* Java-based


### Hierarchical Triangular Mesh (HTM)

Used by WWT.

Basic shape: triangle.

### Tessellated octahedral adaptive subdivision transform (TOAST)

Extension of HTM.			
​		

## Links	

[Splitting the Sky – HTM and HEALPix](https://www.researchgate.net/publication/226874931_Splitting_the_sky_-_HTM_and_HEALPix)

