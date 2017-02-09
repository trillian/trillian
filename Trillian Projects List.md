# Trillian Projects List

Although Trillian is a large project in scope, it can be broken down into several parts that can be assigned to independent teams. This page is a list of projects that are ready to be started (and is by no means exhaustive!).

### Metadata Scraping

A key feature of Trillian is that it contains the metadata of numerous astronomical data sets. For each data set we want to include in Trillian, we need to gather the metadata for every file available. This has already been done for several data sets (see [this part of the repo](https://github.com/trillian/trillian/tree/master/datasets)), but will need to be expanded to others. This might mean extracting the data from a database we have, to writing a Python script to extract the metadata from the archives themselves. I've been extracting the full FITS headers from each file, and we need a script to be able to do this remotely without downloading the full file. This will be repeated for multiple data sets.

**Programming challenge:** Write a Python script that reads and parses the first FITS header of this file without downloading the full file: http://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band_p1bm_frm/3a/01253a/124/01253a124-w1-int-1b.fits.

### API Development

The Trillian project has indexed the metadata of over 50TB (and counting!) of astronomical data. When a user's custom code requests or is provided data (either from the database or the data files themselves), it will do so through a RESTful API. APIs need to be designed and written for numerous data sets, which new ones being added. The API framework will be written as a [Flask](http://flask.pocoo.org) application written in Python, utilizing the [SQLAlchemy](http://sqlalchemy.org) object relational mapper. The API will access the the PostgreSQL database for its data.

Beyond the data API, an Trillian API will also need to be developed. This will report on the current status of the framework – what data sets are being indexed, the percent completed, the total size, number of jobs running, etc.

**Programming challenge:** Create a small SQLite database (to keep things simple) that contains a table with a list of filenames. Write a simple API that will query the database, returning the filenames that contain a string specified by the user in the API call. The returned format must be JSON. Bonus points for using SQLAlchemy!

### Web Interfaces

Trillian needs a web interface for both developers and users. On the developer side it will need to present what data sets are available, what percentage they have been indexed, data set size, etc. You will work with the person developing the Trillian framework API above. Ideally, this information will be displayed graphically using whatever JavaScript library you prefer. This task will require knowledge of HTML, JavaScript, CSS, and basic web design.

**Programming challenge:** Write a web page that accesses some live API (your choice) and presents the results on the page. This can be a pure HTML+JavaScript page or else a basic Python+Flask application. Note that we are only interested in these technologies (e.g. no PHP), but if you have suggestions for something else, please contact us via the [mailing list](https://groups.google.com/forum/#!forum/trillianverse). Things that we are particularly looking for: a modern, clean design; easy to read code; a graphical display of data (it doesn't have to be super fancy, but more than just text on a page), use of JavaScript for visualization.

### Documentation

Trillian will require several APIs for data access. These will need to be documented on the web site. This will require developing HTML templates. Should they be generated from the code, will they need to be hand-made, or some combination of the two? Documentation should also include examples on how to use the API, including code, sample queries and outputs.

### Docker Development Environment

We need Docker expertise! Docker will be used in two contexts - user development and server deployment. A person who uses Trillian will need a sandbox/development environment. They will start with a Docker container that has the Python environment we want to set up, plus the latest version of the Trillian Python module. They will then add their own code there. The container will have the ability to download data into it.

**Programming challenge:** Create a Docker instance that has the Anaconda Python 3 environemnt installed into it. Write a script/pipeline/process that will take that template and load the latest Trillian Python module from GitHub.

### Your Project Here!

Have an idea for your own project proposal? Join the [Trillian mailing list](https://groups.google.com/forum/#!forum/trillianvers) and pitch your idea there. We will discuss it with you and provide feedback and guidance. Based on the idea, we will devise a short programming challenge that is appropriate to the task.

**Programming challenge:** TBD.

