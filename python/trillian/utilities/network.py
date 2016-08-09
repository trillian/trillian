
import urllib
from urllib import request

def server_accepts_range_requests(url=None):
	'''
	Given a URL, tests whether the host supports range requests.
	The URL may be a full URL to a resource or just to the top level domain.
	'''
	if url is None:
		raise Exception("A URL must be specified.")

	response = urllib.request.urlopen(url)
	value = response.headers.get("Accept-Ranges")
	if value in [None, 'none']:
		return False
	elif value == 'bytes':
		return True

	# TODO:
	# server may not return a header value but may still accept range requests - add test
		
def read_byte_range(url=None, start=0, length=None):
	'''
	Read the specified range of bytes from an HTTP resource.
	'''
	if url is None:
		raise Exception("A URL must be specified.")
	elif length is None:
		raise Exception("The number of bytes to read from this resource ('length') must be specified.")
	
	request = request.Request(url)
	request.add_header(key="Range", val="bytes={0}-{1}".format(start, start+length-1))
	
	response = request.urlopen(url)
	bytes_read = response.read(bytes)
	