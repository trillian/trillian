#!/usr/bin/env python

'''
ModelClasses file for schema "file".
'''

from ..DatabaseConnection import DatabaseConnection
from ..AstropyQuantitySQLAlchemyTypes import GigabyteType
from .TrillianModelClasses import DatasetRelease

import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, scoped_session

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

class FitsFile(Base):
	__tablename__ = 'fits_file'
	__table_args__ = {'autoload' : True, 'schema' : 'files'}
#	dataset_release_pk = Column(Integer, ForeignKey('trillian.dataset_release.pk'))

class BasePath(Base):
	__tablename__ = 'base_path'
	__table_args__ = {'autoload' : True, 'schema' : 'files'}

	@staticmethod
	def objectFromString(session=None, path=None, add=False):
		'''
		Get the BasePath database object that matches the given path.
		
		@param session An SQLAlchemy Session instance.
		@param path The base_path value of the BasePath.
		@param add Boolean to indicate if a new entry should be added to the database if not found.
		@returns A BasePath object that matches `base_path`, None otherwise.
		'''
		theBasePath = None
		
		if path is None:
			raise Exception("A path was not provided!")
		if session is None:
			raise Exception("A session must be provided.")
		
		try:
			theBasePath = session.query(BasePath)\
									   .filter(BasePath.path==path)\
									   .one()
		except sqlalchemy.orm.exc.NoResultFound:
			if add:
				# create it here
				# use a new session in case another running process might be doing the same
				TempSession = scoped_session(sessionmaker(bind=dbc.engine, autocommit=True))
				tempSession = TempSession()
				
				tempSession.begin()
				theBasePath = BasePath()
				theBasePath.path = path
				tempSession.add(theBasePath)
				
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
				theBasePath = session.query(BasePath)\
									.filter(BasePath.path==path)\
									.one()
			else:
				theBasePath = None
		except sqlalchemy.orm.exc.MultipleResultsFound:
			raise Exception("Database integrity error: multiple keyword records with label '{0}' found.".format(keyword))

		return theBasePath


class FileKind(Base):
	__tablename__ = "file_kind"
	__table_args__ = {'autoload' : True, 'schema' : 'files'}

# =========================
# Define relationships here
# =========================
#
FitsFile.datasetRelease = relationship(DatasetRelease, backref="fitsFiles")

FitsFile.hdus = relationship(FitsHDU,
							 order_by="asc(FitsHDU.number)",
							 backref="fitsFile")
FitsFile.basePath = relationship(BasePath, backref="fitsFiles")
FitsFile.fileKind = relationship(FileKind, backref="fitsFiles")

FitsHDU.headerValues = relationship(FitsHeaderValue,
									order_by="asc(FitsHeaderValue.index)",
									backref="hdu")

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
	
	



