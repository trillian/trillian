#!/usr/bin/env python

'''
This script takes a set of URLs to FITS files and reads the header from them,
using as little bandwidth as possible.

Ref:
http://stackoverflow.com/questions/2986392/what-is-the-best-way-to-open-a-url-and-get-up-to-x-bytes-in-python
http://stackoverflow.com/questions/5787213/is-it-possible-to-read-only-first-n-bytes-from-the-http-server-using-linux-comma?lq=1

'''

import urllib
import multiprocessing

# test code
# ---------

def download(url, bytes = 1024):
    """Copy the contents of a file from a given URL
    to a local file.
    """
    webFile = urllib.urlopen(url)
    #localFile = open(url.split('/')[-1], 'w')
    #localFile.write(webFile.read(bytes))
    s = webFile.read(bytes)
    webFile.close()
    #localFile.close()
    return s
    
file_url = "http://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band_p1bm_frm/3b/05693b/154/05693b154-w1-int-1b.fits"

print download(url=file_url, bytes=500*80)
