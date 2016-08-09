#!/usr/bin/env python

#import urllib
import urllib.request

#url = "http://api.sdss3/org"
url = "http://data.sdss3.org/sas/dr12/boss/photoObj/301/4203/photoField-004203-1.fits"

response = urllib.request.urlopen(url)
value = response.headers.get("Accept-Ranges")
if value in [None, 'none']:
	return False
elif value == 'bytes':
	return True
# server may not return a header value but may still accept range requests - add test

	
print(response.headers.response.headers.get("Accept-Ranges"))