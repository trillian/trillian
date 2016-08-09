#!/usr/bin/env python

'''
This script takes a set of URLs to FITS files and reads the header from them,
using as little bandwidth as possible.

Ref:
http://stackoverflow.com/questions/2986392/what-is-the-best-way-to-open-a-url-and-get-up-to-x-bytes-in-python
http://stackoverflow.com/questions/5787213/is-it-possible-to-read-only-first-n-bytes-from-the-http-server-using-linux-comma?lq=1

'''

from urllib import request
import multiprocessing

class FITSHeaderEndFound(Exception):
	pass
	
fitsEndCard = "{0:80s}".format("END")

# test code
# ---------

def download(url, bytes = 1024):
    """Copy the contents of a file from a given URL
    to a local file.
    """
    webFile = request.urlopen(url)
    #localFile = open(url.split('/')[-1], 'w')
    #localFile.write(webFile.read(bytes))
    s = webFile.read(bytes)
    webFile.close()
    #localFile.close()
    return s
    
#file_url = "http://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band_p1bm_frm/3b/05693b/154/05693b154-w1-int-1b.fits"
file_url = "http://data.sdss3.org/sas/dr12/boss/photoObj/301/4203/photoField-004203-1.fits"

header_bytes = download(url=file_url, bytes=500*80) # result is in bytes

cards = []
try:
	for i in range(0, len(header_bytes), 80):
		try:
			current_card = header_bytes[i:i+80].decode("utf-8")
			cards.append(current_card)
			if current_card == fitsEndCard:
				raise FITSHeaderEndFound()
		except UnicodeDecodeError:
			# reading beyond end of header
			raise FITSHeaderEndFound()
except FITSHeaderEndFound:
	pass

for card in cards:
	print(card)

