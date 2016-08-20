#!/usr/bin/env python

'''
ModelClasses file for schema "file".
'''
import ast

from ..DatabaseConnection import DatabaseConnection
from ..AstropyQuantitySQLAlchemyTypes import GigabyteType
from .TrillianModelClasses import DatasetRelease, Footprint

import sqlalchemy
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import func # for aggregate, other functions

from ...utilities import memoize

dbc = DatabaseConnection()

# ========================
# Define database classes
# ========================
#
Base = dbc.Base

class FitsHeaderKeyword(Base):
	__tablename__ = 'fits_header_keyword'
	__table_args__ = {'autoload' : True, 'schema' : 'files'}
	
	#@memoize
	@staticmethod
	def objectFromString(session=None, keywordString=None, add=True):
		'''
		Get the FITS header keyword object from the 'fits_header_keyword' table.
		
		@param keywordString The string value of the keyword.
		@param add Boolean to indicate if a new entry should be added to the database if not found.
		@returns A FitsHeaderKeyword object that matches `keywordString`, None otherwise.
		'''
		theKeyword = None
		
		if keywordString is None:
			raise Exception("keyword not specified!")
		try:
			theKeyword = session.query(FitsHeaderKeyword)\
								.filter(FitsHeaderKeyword.label==keywordString)\
								.one()
		except sqlalchemy.orm.exc.NoResultFound:
			if add:
				# create it here
				# use a new session in case another running process might be doing the same
				TempSession = scoped_session(sessionmaker(bind=dbc.engine, autocommit=True))
				tempSession = TempSession()

				tempSession.begin()
				theKeyword = FitsHeaderKeyword()
				theKeyword.label = keywordString
				tempSession.add(theKeyword)
				
				try:
					tempSession.commit()
				except sqlalchemy.exc.IntegrityError:
					# since this session is in a "bubble", another process elsewhere
					# (e.g. in a multiprocessing environment) could have beat us to it.
					#
					# Likely error:
					# sqlalchemy.exc.IntegrityError: (psycopg2.IntegrityError) duplicate key value violates unique constraint "fits_header_comment_uniq"
					#
					pass # since we know the value is there, the next query should succeed.
			
				# now pull it out into the given session
				theKeyword = session.query(FitsHeaderKeyword)\
						.filter(FitsHeaderKeyword.label==keywordString)\
						.one()

		except sqlalchemy.orm.exc.MultipleResultsFound:
			raise Exception("Database integrity error: multiple keyword records with label '{0}' found.".format(keyword))
		
		assert theKeyword is not None, "'keyword' should not be 'None'"
		return theKeyword
	
	def __repr__(self):
		return "<{0}.{1} object at {2}: '{3}'>".format(self.__module__, type(self).__name__, hex(id(self)), self.label)

class FitsHeaderValue(Base):
	__tablename__ = 'fits_header_value'
	__table_args__ = {'autoload' : True, 'schema' : 'files'}
	
	def __repr__(self):
		if self.keyword.label in ["COMMENT", "HISTORY"]:
			return "<{0}: [{1:8} {2}]".format(type(self).__name__, self.keyword.label, self.comment.comment_string)
		elif self.string_value in ["T", "F"]:
			if self.comment is not None:
				return "<{0}: [{1:8} = {2:>20} / {3}]>".format(type(self).__name__, self.keyword.label, self.string_value, self.comment.comment_string)
			else:
				return "<{0}: [{1:8} = {2:>20}]>".format(type(self).__name__, self.keyword.label, self.string_value)
		elif self.numeric_value is not None:
			if self.comment is not None:
				return "<{0}: [{1:8} = {2:>20} / {3}]>".format(type(self).__name__, self.keyword.label, self.string_value, self.comment.comment_string)
			else:
				return "<{0}: [{1:8} = {2:>20}]>".format(type(self).__name__, self.keyword.label, self.string_value)
		else:
			# value is string
			if self.comment is not None:
				return "<{0}: [{1:8} = {2:20} / {3}]>".format(type(self).__name__, self.keyword.label, self.string_value, self.comment.comment_string)
			else:
				return "<{0}: [{1:8} = {2:20}]>".format(type(self).__name__, self.keyword.label, self.string_value)

class FitsHeaderComment(Base):
	__tablename__ = 'fits_header_comment'
	__table_args__ = {'autoload' : True, 'schema' : 'files'}
	
	#@memoize
	@staticmethod
	def objectFromString(session=None, commentString=None, add=True):
		'''
		Get the FITS header comment object from the 'fits_header_comment' table.
		
		@param commentString The string value of the comment.
		@param add Boolean to indicate if a new entry should be added to the database if not found.
		@returns A FitsHeaderComment object that matches `commentString`, None otherwise.
		'''
		theComment = None
		
		if commentString is None:
			raise Exception("comment not specified!")
		if session is None:
			raise Exception("A session must be provided.")
	
		try:
			theComment = session.query(FitsHeaderComment)\
								.filter(FitsHeaderComment.comment_string==commentString)\
								.one()
		except sqlalchemy.orm.exc.NoResultFound:
			if add:
				# create it here
				# use a new session in case another running process might be doing the same
				TempSession = scoped_session(sessionmaker(bind=dbc.engine, autocommit=True))
				tempSession = TempSession()
				
				tempSession.begin()
				theComment = FitsHeaderComment()
				theComment.comment_string = commentString
				tempSession.add(theComment)
				
				try:
					tempSession.commit()
				except sqlalchemy.exc.IntegrityError:
					# since this session is in a "bubble", another process elsewhere
					# (e.g. in a multiprocessing environment) could have beat us to it.
					#
					# Likely error:
					# sqlalchemy.exc.IntegrityError: (psycopg2.IntegrityError) duplicate key value violates unique constraint "fits_header_comment_uniq"
					#
					pass # since we know the value is there, the next query should succeed.

				# now pull it out into the given session
				theComment = session.query(FitsHeaderComment)\
									.filter(FitsHeaderComment.comment_string==commentString)\
									.one()
				
			else:
				theComment = None
		except sqlalchemy.orm.exc.MultipleResultsFound:
			raise Exception("Database integrity error: multiple keyword records with label '{0}' found.".format(keyword))

		return theComment

class FitsHDU(Base):
	__tablename__ = 'fits_hdu'
	__table_args__ = {'autoload' : True, 'schema' : 'files'}
	
	def __repr__(self):
		return "<{3}: pk={0}, file='{1}', hdu={2}>".format(self.pk, self.fitsFile.filename, self.number, type(self).__name__)
	
	def pseudoHeader(self, comments=False):
		'''
		
		'''
		session = Session.object_session(self)
		headerValues = self.headerValues
		fakeHeader = list()
		for hv in headerValues:
			keyword = hv.keyword.label
			if keyword in ["HISTORY", "COMMENT"]:
				fakeHeader.append("{0:8}{1}".format(keyword, hv.string_value))
			elif hv.numeric_value is not None:
				fakeHeader.append("{0:8}={1:>21}".format(keyword, hv.string_value))
			elif hv.string_value in ["T", "F"]:
				fakeHeader.append("{0:8}={1:>21}".format(keyword, hv.string_value))
			elif hv.string_value[0] == "'":
				fakeHeader.append("{0:8}= {1}".format(keyword, hv.string_value))
			else:
				raise Exception("Header type not handled: '{0}'".format(hv.string_value))
		return fakeHeader
	
	def pseudoHeader2(self, comments=False):
		'''
		A FITS header reconstructed from metadata in the database.
		The header is not intended to exact reproduce the original file,
		but may be good enough to pass to programs attempting to parse a real header.
		'''
		session = Session.object_session(self)
		# the values are returned as single element tuples
		return [x[0] for x in session.query(func.fits_header(self.pk)).all()]

	def headerDict(self):
		'''
		A dictionary of header values by keyword. Excludes COMMENT and HISTORY.
		'''
		import ast

		session = Session.object_session(self)
		hd = dict() # header dictionary
		for headerValue in self.headerValues:
			keyword = headerValue.keyword.label
			if keyword in ["COMMENT", "HISTORY"]:
				continue
			s = headerValue.string_value
			try:
				# handles (float, int), converted to the correct type
				value = ast.literal_eval(s)
			except ValueError:
				# string value
				if s == "T":
					value = True
				elif s == "F":
					value = False
				else:
					# a regular string - remove leading and trailing quotes if present
					if s[0] == "'" and s[-1] == "'":
						value = s[1:-1]
					else:
						value = s
				
			hd[keyword] = value
			
		return hd

# 	def header(self, comments=False):
# 		'''
# 		Returns an array of strings that is a close approximation of the file's original header.
# 		
# 		@param Sepcify whether comments should also be retrieved.
# 		'''
# 		header = []
# 		session = Session.object_session(self)
# 		for header_value in self.headerValues:
# 			header.append[
# 			
# 		return header

class FitsFile(Base):
	__tablename__ = 'fits_file'
	__table_args__ = {'autoload' : True, 'schema' : 'files'}

class DirectoryPath(Base):
	__tablename__ = 'directory_path'
	__table_args__ = {'autoload' : True, 'schema' : 'files'}

	def __init__(self, path=None):
		if not isinstance(path, str):
			raise Exception("DirectoryPath: expected 'path' to be of string type.")
		self.path = path
		
	def __repr__(self):
		return "<{0}.{1} object at {2}: '{3}'>".format(self.__module__, type(self).__name__, hex(id(self)), self.path)

	@staticmethod
	def objectFromString(session=None, path=None, add=False, type_string=None):
		'''
		
		'''
		theDirectoryPath = None
		
		if path is None:
			raise Exception("A path was not provided!")
		if session is None:
			raise Exception("A session must be provided.")
		
		try:
			theDirectoryPath = session.query(DirectoryPath)\
									  .join(DirectoryPathType)\
									  .filter(DirectoryPath.path==path)\
									  .filter(DirectoryPathType.label==type_string)\
									  .one()
		except sqlalchemy.orm.exc.NoResultFound:
			if add:
				# create it here
				# use a new session in case another running process might be doing the same
				TempSession = scoped_session(sessionmaker(bind=dbc.engine, autocommit=True))
				tempSession = TempSession()
				
				tempSession.begin()
				theDirectoryPath = DirectoryPath()
				theDirectoryPath.path = path
				theDirectoryPath.type = tempSession.query(DirectoryPathType).filter(DirectoryPathType.label==type_string).one()
				tempSession.add(theDirectoryPath)
				
				try:
					tempSession.commit()
				except sqlalchemy.exc.IntegrityError:
					# since this session is in a "bubble", another process elsewhere
					# (e.g. in a multiprocessing environment) could have beat us to it.
					#
					# Likely error:
					# sqlalchemy.exc.IntegrityError: (psycopg2.IntegrityError) duplicate key value violates unique constraint "fits_header_comment_uniq"
					#
					pass # since we know the value is there, the next query should succeed.

				# now pull it out into the given session
				theDirectoryPath = session.query(DirectoryPath)\
										  .join(DirectoryPathType)\
										  .filter(DirectoryPath.path==path)\
										  .filter(DirectoryPathType.label==type_string)\
										  .one()
			else:
				theDirectoryPath = None
		except sqlalchemy.orm.exc.MultipleResultsFound:
			raise Exception("Database integrity error: multiple keyword records with label '{0}' found.".format(keyword))

		return theDirectoryPath

	@staticmethod
	def relativePathFromString(session=None, path=None, add=False):
		'''
		Get the DirectoryPath database object that matches the given path.
		
		@param session An SQLAlchemy Session instance.
		@param path The 'path' value of the DirectoryPath.
		@param add Boolean to indicate if a new entry should be added to the database if not found.
		@returns A DirectoryPath object that matches `path`, None otherwise.
		'''
		return DirectoryPath.objectFromString(session=session, path=path, type_string="relative path", add=add)

	@staticmethod
	def basePathFromString(session=None, path=None, add=False):
		'''
		Get the DirectoryPath database object that matches the given path.
		
		@param session An SQLAlchemy Session instance.
		@param path The 'path' value of the DirectoryPath.
		@param add Boolean to indicate if a new entry should be added to the database if not found.
		@returns A DirectoryPath object that matches `path`, None otherwise.
		'''
		return DirectoryPath.objectFromString(session=session, path=path, type_string="base path", add=add)

# 		theDirectoryPath = None
# 		relative_path_label = "relative path"
# 		
# 		if path is None:
# 			raise Exception("A path was not provided!")
# 		if session is None:
# 			raise Exception("A session must be provided.")
# 		
# 		try:
# 			theDirectoryPath = session.query(DirectoryPath)\
# 									  .join(DirectoryPathType)\
# 									  .filter(DirectoryPath.path==path)\
# 									  .filter(DirectoryPathType.label==relative_path_label)\
# 									  .one()
# 		except sqlalchemy.orm.exc.NoResultFound:
# 			if add:
# 				# create it here
# 				# use a new session in case another running process might be doing the same
# 				TempSession = scoped_session(sessionmaker(bind=dbc.engine, autocommit=True))
# 				tempSession = TempSession()
# 				
# 				tempSession.begin()
# 				theDirectoryPath = DirectoryPath()
# 				theDirectoryPath.path = path
# 				theDirectoryPath.type = tempSession.query(DirectoryPathType).filter(DirectoryPathType.label==relative_path_label).one()
# 				tempSession.add(theDirectoryPath)
# 				
# 				try:
# 					tempSession.commit()
# 				except sqlalchemy.exc.IntegrityError:
# 					# since this session is in a "bubble", another process elsewhere
# 					# (e.g. in a multiprocessing environment) could have beat us to it.
# 					#
# 					# Likely error:
# 					# sqlalchemy.exc.IntegrityError: (psycopg2.IntegrityError) duplicate key value violates unique constraint "fits_header_comment_uniq"
# 					#
# 					pass # since we know the value is there, the next query should succeed.
# 
# 				# now pull it out into the given session
# 				theDirectoryPath = session.query(DirectoryPath)\
# 										  .join(DirectoryPathType)\
# 										  .filter(DirectoryPath.path==path)\
# 										  .filter(DirectoryPathType.label==relative_path_label)\
# 										  .one()
# 			else:
# 				theDirectoryPath = None
# 		except sqlalchemy.orm.exc.MultipleResultsFound:
# 			raise Exception("Database integrity error: multiple keyword records with label '{0}' found.".format(keyword))
# 
# 		return theDirectoryPath

class FitsFileToDirectoryPath(Base):
	__tablename__ = "fits_file_to_directory_path"
	__table_args__ = {'autoload' : True, 'schema' : 'files'}

class DirectoryPathType(Base):
	__tablename__ = "directory_path_type"
	__table_args__ = {'autoload' : True, 'schema' : 'files'}

	def __repr__(self):
		return "<{0}.{1} object at {2}: '{3}'>".format(self.__module__, type(self).__name__, hex(id(self)), self.label)

class FileKind(Base):
	__tablename__ = "file_kind"
	__table_args__ = {'autoload' : True, 'schema' : 'files'}

	def __repr__(self):
		return "<{0}.{1} object at {2}: '{3}'>".format(self.__module__, type(self).__name__, hex(id(self)), self.label)

class FitsFileToFileKind(Base):
	__tablename__ = "fits_file_to_file_kind"
	__table_args__ = {'autoload' : True, 'schema' : 'files'}

# =========================
# Define relationships here
# =========================
#
FitsFile.datasetRelease = relationship(DatasetRelease, backref="fitsFiles")

FitsFile.hdus = relationship(FitsHDU,
							 order_by="asc(FitsHDU.number)",
							 backref="fitsFile")
#FitsFile.directoryPath = relationship(DirectoryPath, backref="fitsFiles")
#FitsFile.relativePath = relationship(DirectoryPath, backref="fitsFiles")

FitsFile.directoryPaths = relationship(DirectoryPath,
									   secondary=FitsFileToDirectoryPath.__table__,
									   backref="fitsFile")


FitsFile.fileKinds = relationship(FileKind,
								  secondary=FitsFileToFileKind.__table__,
								  backref="fitsFiles")

DirectoryPath.type = relationship(DirectoryPathType, backref="directories")

FitsHDU.headerValues = relationship(FitsHeaderValue,
									order_by="asc(FitsHeaderValue.index)",
									backref="hdu")
FitsHDU.footprint = relationship(Footprint, backref="hdu")

FitsHeaderValue.keyword = relationship(FitsHeaderKeyword, backref="headerValues")
FitsHeaderValue.comment = relationship(FitsHeaderComment, backref="headerValues")

# ---------------------------------------------------------
# Test that all relations/mappings are self-consistent.
# ---------------------------------------------------------
#
from sqlalchemy.orm import configure_mappers
try:
	configure_mappers()
#	raise Exception("")
except RuntimeError as error:
	print("""
An error occurred when verifying the relations between the database tables.
Most likely this is an error in the definition of the SQLAlchemy relations - 
see the error message below for details.
""")
	print("Error type: %s" % sys.exc_info()[0])
	print("Error value: %s" % sys.exc_info()[1])
	print("Error trace: %s" % sys.exc_info()[2])
	sys.exit(1)
	
	



