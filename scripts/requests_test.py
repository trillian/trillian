#!/usr/bin/env python 

import requests

# r = requests.put(url)
# r = requests.head(url)
# r = requests.delete(url)
# r = requests.options(url)

# GET requests
#r = requests.get(url, payload={"key1":value1, "key2":value2})

# without a session
# -----------------
#resp = requests.get(url="http://localhost/index.html")
#print(resp.headers)

url = "http://localhost/cosmos-01-G141-big_19586.2D.fits" #index.html"

# with a session
# --------------
with requests.Session() as session:
	# session.auth = ('user', 'password')
	
	r = session.head(url)
	print("HEAD response headers: ", r.headers, "\n")
	
	# add headers to requests
	#session.headers.update({"":""})
	# or in the get request:
	# session.get(url, headers=headers)
	
	# send data via POST:
	# session.post(url, data=dataDict) # e.g. {"key":"value", "key2":"value2"}, can also be a string
	
	# json support - will encode dictionary to JSON
	# session.post(url, json={"key":"value", "key2":"value2"})
	
	# Request a range of bytes to read via this request header:
	session.headers.update({"Range":"bytes={0}-{1}".format(5,10)})

	print("Range request response headers: ", session.headers, "\n")
	
	resp = session.get(url="http://localhost/index.html")
	print(resp.headers)
	print(resp.text) # <-- HTML text, unicode automatically decoded
	# resp.content # <-- binary data
	# resp.json()  # if response is json, will be decoded, no JSON raises ValueError

	# get another range
	session.headers.update({"Range":"bytes={0}-{1}".format(50,60)})
	resp = session.get(url="http://localhost/index.html")
	print(resp.text)

