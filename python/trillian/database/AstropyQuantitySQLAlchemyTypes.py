#!/usr/bin/env python

'''
These classes provide translation between Astropy Quantity objects and SQLAlchemy model classes.

To set a custom class type for a single column of a table, use autoload as usual
and set the class of just the columns needed. In this example, the column named
'xxx' in the database is being modified to be of type "GigabyteType"):

class SomeTableClass(Base):
	__table__ = 'tablename'
	__table_args__ = {'autoload' : True}
	
	xxx = Column(name='xxx', type_=GigabyteType)

To replace *all* columns of a certain type with a custom class, use an event.
In this example, all DateTime columns of any table are changed to be of type "MyCustomDateTimeClass".

from sqlalchemy.schema import Table
from sqlalchemy import event

@event.listens_for(Table, "column_reflect")
def set_utc_date(inspector, table, column_info):
    if isinstance(column_info['type'], DateTime):
        column_info['type'] = MyCustomDateTimeClass()

'''

from sqlalchemy.types import TypeDecorator, Numeric
import astropy.units as u
from astropy.units import Quantity

class GigabyteType(TypeDecorator):
	''' Custom type to handle astropy.quantity objects stored as GB integers. '''
	
	impl = Numeric
	
	def __init__(self, *arg, **kwarg):
		TypeDecorator.__init__(self, *arg, **kwarg)
		self.quantity = arg[0]
	
	def process_bind_param(self, value, dialect):
		if isinstance(value, Quantity):
			return value.to(u.GB).value
		else:
			return value
	
	def process_result_value(self, value, dialect):
		if value is not None:
			value = value * u.GB
		return value
