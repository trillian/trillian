# Trillian Projects List

Although Trillian is a large project in scope, it can be broken down into several parts that can be assigned to independent teams. This page is a list of projects that are ready to be started (and is by no means exhaustive!).



### API Development

The Trillian project has indexed the metadata of over 50TB of astornomical data. When a user's custom code requests or is provided data (either from the database or the data files themselves), it will do so through a RESTful API. APIs need to be designed and written for numerous data sets, which new ones being added. The API framework will be written as a [Flask](http://flask.pocoo.org) application written in Python, utilizing the [SQLAlchemy](http://sqlalchemy.org) object relational mapper.



### Web Interfaces

Interacting ith 