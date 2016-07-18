-----------------------------------
     unWISE coadds: flat files
-----------------------------------

http://unwise.me/data

The unWISE coadds are on the same tile centers as the WISE Atlas
Images: 18,240 tiles per band, 1.56 x 1.56 degrees, in rings of equal
Dec.  The tiles are named by their RA,Dec center: tile "0591p530" is
at RA = 59.1, Dec = +53.0 degrees; ie, the first four digits of the
tile name is int(RA*10), then "p" for +Dec and "m" for -Dec, then
three digits of int(abs(Dec)*10).  The files are organized into
subdirectories of the first three digits of the tile name;

  http://unwise.me/data/000/0000m016/
  http://unwise.me/data/000/0000m031/
  ...
  http://unwise.me/data/001/0015m016/
  http://unwise.me/data/001/0015m031/
  ...
etc.

The tiles are listed in the file:
  http://unwise.me/data/allsky-atlas.fits

All the unWISE data product files along with their md5sums are listed
in the file "md5sums".  md5sums per top-level directory ("000", etc)
are in md5sums-by-dir/000.md5

For each tile and band W1-W4, the following files exist:

-- unwise-0000p000-w1-frames.

A FITS table listing the frames (individual L1b exposures) that went
into this coadd.

-- unwise-0000p000-w1-img-m.fits

C_m (equation 14) in the paper.

"Masked" image, 2048 x 2048 pixels, TAN projected at 2.75"/pixel.
Background-subtracted, in units of "Vega nanomaggies" per pixel:
  mag = -2.5 * (log10(flux) - 9)

The "masked" images (with "-m" in the filename) use outlier detection
to mask cosmic rays and other artifacts, but will also have transients
masked.  The "masked" coadds simply ignore masked pixels (omitting
them from the coadd), so some pixels will have no unmasked pixels and
no measurement at all: pixel value 0 and infinite uncertainty.

-- unwise-0000p000-w1-invvar-m.fits.gz

W_m (equation 12) in the paper.

Inverse-variance of the coadd image.  The coadd pixel value is
  img  +- (1 / sqrt(invvar))
based on the sum of inverse-variances of the input pixels; ie,
assuming independent Gaussian measurements.  An inverse-variance of
zero indicates that no unmasked pixels contributed to the coadd; ie,
blank pixels.

Note that the weight used is a per-image average inverse-variance,
rather than per-pixel, so bright stars do *not* have larger variance
than faint stars (Poisson noise).

-- unwise-0000p000-w1-n-m.fits.gz

N_m (equation 13) in the paper.

Number of exposures contributing to the coadd at this pixel.

-- unwise-0000p000-w1-std-m.fits.gz

S_m (equation 15) in the paper.

Sample standard deviation (scatter) of the individual-exposure pixels
contributing to this coadd pixel.  This will be large if, for example,
the source is variable.  This could be used to, for example, detect
pixels that vary more than expected due to noise and source Poisson
variation, which might indicate unmasked artifacts or variability.

-- unwise-0000p000-w1-mask.tgz

A bitmap file for each of the individual L1b frames that contributed
to this coadd, indicating which pixels were masked as outliers.

-- unwise-0000p000-w1-img-u.fits          (C_u)
-- unwise-0000p000-w1-invvar-u.fits.gz    (W_u)
-- unwise-0000p000-w1-std-u.fits.gz       (S_u)
-- unwise-0000p000-w1-n-u.fits.gz         (N_u)

"Unmasked" image and other data products, as above.  The "unmasked"
("-u" in filename) ones use "patched" values (roughly interpolated)
for pixels that are masked.  (See equations 9-15 in the paper.)  Thus
every pixel contains a value.



Additional questions can be posted here:
 https://groups.google.com/forum/#!forum/unwise
 