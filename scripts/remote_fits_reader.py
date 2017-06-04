#!/usr/bin/env python

'''
This script takes a set of URLs to FITS files and reads the header from them,
using as little bandwidth as possible.

Ref:
http://stackoverflow.com/questions/2986392/what-is-the-best-way-to-open-a-url-and-get-up-to-x-bytes-in-python
http://stackoverflow.com/questions/5787213/is-it-possible-to-read-only-first-n-bytes-from-the-http-server-using-linux-comma?lq=1

'''

import re
import sys
import pdb
import json
from urllib.parse import urlparse
import os.path
import requests
import multiprocessing

#file_url = "http://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band_p1bm_frm/3b/05693b/154/05693b154-w1-int-1b.fits"
#file_url = "http://data.sdss3.org/sas/dr12/boss/photoObj/301/4203/photoField-004203-1.fits"
#file_url = "http://localhost/frame-g-006073-4-0063.fits"
file_url = "http://localhost/cosmos-01-G141-big_19586.2D.fits"

class LastHDUReachedException(Exception):
	pass
    
class FITSHeaderDataBlock(object):
	def __init__(self, n=None):
		self.number = n
		self.data = None		# this is a byte array
		self.firstByte = None	# offset location of byte in file
		self.lastByte = None
		self.containsEND = None
		self.containsXTENSION = None
    
class HDUHeader(object):
	def __init__(self):
		self.cards = list()
		self.byteHDUStart = None
		self.number = None
		self.bitpix = None
		self.naxis = None
		self.axes = list()
		
		# other properties:
		# byteHDUEnd
		# byteHeaderEnd
		# byteDataStart
		
		# default values that will have no effect on the dataLength
		self.pcount = 0
		self.gcount = 1
	
	@property
	def dataLength(self):
		''' Calculate data length in bytes based on header cards. '''
		if len(self.axes) == 0:
			return 0
		else:
			naxes_product = self.axes[0]
			for axis in self.axes[1:]:
				naxes_product = axis * naxes_product
			naxes_product = self.pcount + naxes_product
			
		# bitpix values -> bitpix:bytes
		bitpix2byteSize = {8:1, 16:2, 32:4, 64:8, -32:4, -64:8}
		
		try:
			element_byte_size = bitpix2byteSize[self.bitpix]
		except KeyError:
			raise Exception("Invalid bitpix value found ({0}).".format(self.bitpix))
		
		return naxes_product * element_byte_size * self.gcount
	
	@property
	def byteHDUEnd(self):
		''' '''
		if self.dataLength == 0:
			nblocks = len(self.cards) * 80 // 2880
			if (len(self.cards) * 80) % 2880 == 0:
				return self.byteHDUStart + nblocks * 2880 - 1
			else:
				return self.byteHDUStart + (nblocks + 1) * 2880 - 1
		else:
			nblocks = self.dataLength // 2880
			if self.dataLength % 2880 == 0:
				return self.byteDataStart + nblocks * 2880 - 1
			else:
				return self.byteDataStart + (nblocks + 1) * 2880 - 1
		
	@property
	def byteHeaderEnd(self):
		''' '''
		nblocks = (len(self.cards) * 80) // 2880 
		remainder = (len(self.cards) * 80) % 2880
		if remainder == 0:
			return self.byteHDUStart + nblocks * 2880 - 1
		else:
			return self.byteHDUStart + nblocks * 2880 + 2880 - 1
		
	@property
	def byteDataStart(self):
		if self.dataLength > 0:
			return self.byteHeaderEnd + 1
		else:
			raise Exception("Attempting to read data byte start for HDU with no data.")
	
	@property
	def byteDataEnd(self):
		if self.dataLength > 0:
			return self.byteDataStart + self.dataLength
		else:
			raise Exception("Attempting to read data byte end for HDU with no data.")
	
class FITSMetadata(object):

	def __init__(self, url=None):
		if url is None:
			raise Exception("A URL must be provided to create a FITSMetadata object.")
	
		self.hdus = list() # index by HDU number-1, value = HDUHeader
		self.fileLength = None
		self.url = url
		self.data_blocks = None
		self._byte_offset = 0 # keep track of where we've read in the file
		
		with requests.Session() as session:
		
			self._session = session
		
			# get initial info
			# ----------------
			head_response = session.head(url)
			# example response:
			#    {'Content-Length': '612', 'Connection': 'keep-alive',
			#     'Last-Modified': 'Sat, 20 May 2017 22:37:16 GMT',
			#     'Server': 'nginx/1.13.0', 'Accept-Ranges': 'bytes',
			#     'ETag': '"5920c51c-264"', 'Content-Type': 'text/html',
			#     'Date': 'Thu, 25 May 2017 06:56:59 GMT'}
			self.fileLength = int(head_response.headers['Content-Length'])
		
			# read all HDUs
			# -------------
			while True:
				try:
					self.readNextHDU()
				except LastHDUReachedException:
					break
			
			self._session = None
	
	@property
	def filename(self):
		u = urlparse(self.url)
		return os.path.basename(u.path)
	
	@property
	def path(self):
		 u = urlparse(self.url)
		 return os.path.dirname(u.path)
	
	def readNextHDU(self):
		'''
		This method tries to read the next HDU for this FITS file.
		If the last one is reached, return False.
		'''
		hdu = HDUHeader()

		if len(self.hdus) == 0:
			hdu.byteHDUStart = 0
			hdu.number = 1
			self._byte_offset = 0
		else:
			previous_hdu = self.hdus[-1]
			hdu.number = previous_hdu.number + 1
			self._byte_offset = previous_hdu.byteHDUEnd + 1
			if self._byte_offset >= self.fileLength:
				raise LastHDUReachedException()
			else:
				hdu.byteHDUStart = self._byte_offset
				
		self.data_blocks = list() # reset data blocks
		blocks_to_process = [self.nextBlock()]
			
		while blocks_to_process[-1].containsEND is not True:
			blocks_to_process.append(self.nextBlock())

		self.processBlocks(hdu=hdu, blocks=blocks_to_process)
		self.hdus.append(hdu)
		
		last_hdu = hdu
		
		while len(self.data_blocks) > 0:
			#
			# Maybe the next full header has been downloaded?
			# Process it instead of returning to the server if so.
			# Make sure not to fetch more blocks from the server.
			#
			# Skip any blocks that contain only data, try to find the next complete
			# header (which may also span multiple blocks).
			#
			blocks_to_process = list()
			header_found = False
			while len(self.data_blocks) > 0:
				next_block = self.nextBlock()
				if next_block.containsXTENSION:
					header_found = True
					blocks_to_process.append(next_block)
				elif header_found:
					blocks_to_process.append(next_block)
				if next_block.containsEND:
					break
					
			if header_found and blocks_to_process[-1].containsEND:
				nextHDU = HDUHeader()
				nextHDU.number = last_hdu.number + 1
				nextHDU.byteHDUStart = last_hdu.byteHDUEnd + 1
				#nextHDU.byteEnd = nextHDU.byteStart + len(blocks_to_process) * 2880
				self.processBlocks(hdu=nextHDU, blocks=blocks_to_process)
				self.hdus.append(nextHDU)
				last_hdu = nextHDU
		
	def processBlocks(self, hdu=None, blocks=None):
		'''
		This method takes raw blocks of data and extracts HDU header cards from them.
		'''
		assert hdu is not None, "Must specify an HDU to process blocks."
		assert blocks is not None and len(blocks) > 0, "Must provide data blocks to process blocks."

		for block in blocks:
			for i in range(36): # 36 cards in a block

				card = block.data[i*80:i*80 + 80].decode('utf-8')
				hdu.cards.append(card)

				#NAXIS match
				naxis_rexp = re.match("(NAXIS[0-9]+)", card)
				
				if card.startswith("BITPIX  ="):
					header, value = card.split("=")
					if "/" in value:
						value = value.split("/")[0]
					hdu.bitpix = int(value)
				elif card.startswith("NAXIS   ="):
					header, value = card.split("=")
					if "/" in value:
						value = value.split("/")[0]
					hdu.naxis = int(value)
				elif card.startswith("PCOUNT  ="):
					header, value = card.split("=")
					if "/" in value:
						value = value.split("/")[0]
					hdu.pcount = int(value)
				elif card.startswith("GCOUNT  ="):
					header, value = card.split("=")
					if "/" in value:
						value = value.split("/")[0]
					hdu.gcount = int(value)
				elif naxis_rexp is not None:
					# match for "NAXISn"
					header, value = card.split("=")
					if "/" in value:
						value = value.split("/")[0]
					hdu.axes.append(int(value))
				elif card == 'END'+77*' ':
					return
	
	def nextBlock(self):
		''' '''
		nblocks = 4 # number of blocks to read at a time

		if self._byte_offset == self.fileLength:
			return None

		try:
			next_block = self.data_blocks.pop(0)
		except IndexError:
			# need more blocks - fetch from server - don't read past length of file
			while self._byte_offset + nblocks*2880 > self.fileLength - 1:
				nblocks = nblocks - 1
			assert nblocks != 0, "Tried to read past end of file: '{0}'".format(self.url)
			self._session.headers.update({"Range":"bytes={0}-{1}".format(self._byte_offset, self._byte_offset + nblocks*2880)})
			response = self._session.get(url=self.url)
			
			for i in range(nblocks):
				block = FITSHeaderDataBlock() #n=block_idx)
				block.firstByte = self._byte_offset
				block.lastByte = self._byte_offset + 2880
				#block_index = block_index + 1
				block.data = response.content[i*2880:i*2880+2880]
				block.containsEND = bytes("END"+77*' ', 'utf-8') in block.data
				block.containsXTENSION = bytes("XTENSION=", 'utf-8') in block.data
				#block.containsHeader = block.data[7] == '=' # not complete
				self.data_blocks.append(block)

				self._byte_offset = self._byte_offset + 2880

			next_block = self.data_blocks.pop(0)

			# sanity check
			assert len(self.data_blocks) < 30, "END card not found in 30 blocks!"
		
		return next_block
	
	@property
	def jsonRepresentation(self):
		'''
		'''
		jsonDict = dict()
		jsonDict["filepath"] = self.path
		jsonDict["sha256"] = None
		jsonDict["filename"] = self.filename
		
		headers = list()
		for hdu in self.hdus:
			header = dict()
			header["hdu_number"] = hdu.number
			header["hdu_start"] = hdu.byteHDUStart
			header["hdu_end"] = hdu.byteHDUEnd
			header["data_length"] = hdu.dataLength
			if hdu.dataLength > 0:
				header["data_start"] = hdu.byteDataStart
				#header["data_end"] = hdu.byteDataEnd
			header["header"] = hdu.cards
			headers.append(header)
		
		jsonDict["headers"] = headers
		jsonDict["size"] = self.fileLength
		
		return json.dumps(jsonDict)
		
md = FITSMetadata(url=file_url)
print(md.jsonRepresentation)

