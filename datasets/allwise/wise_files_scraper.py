#!/usr/local/anaconda/bin/python

'''
This script builds a list of all downloadable files from the
allwise data release.

NOTE: Don't run this; the recursion will break the script long
before it finishes.
'''


import sys
import urllib2
from bs4 import BeautifulSoup
from bs4.element import NavigableString

def scan_links(links=None, base=None):
	#print "Base:   {0}".format(base)
	for link in links:
		#print link
		content = str(link.contents[0]).strip()
		if content == 'Parent Directory':
			continue
		#elif content == '002' or content == '002/':
		#	sys.exit(1)
		elif "fits" in content or "tbl" in content:
			print base + link['href']
			continue
		else:
			new_url = base + "/" + link['href']
			print "new URL {0}".format(new_url)
			x = urllib2.urlopen(new_url)
			new_page = x.read()
			soup = BeautifulSoup(new_page)
			new_links = soup.find_all('a')
			if len(new_links) > 0:
				scan_links(links=new_links, base=base + "/" + link['href'])
		
base_url = "http://irsa.ipac.caltech.edu/ibe/data/wise/merge/merge_p1bm_frm"

c = urllib2.urlopen(base_url)
contents = c.read()
soup = BeautifulSoup(contents)
links = soup.find_all('a')

scan_links(links=links, base=base_url)

#print links[0]['href']
#print links.contents

