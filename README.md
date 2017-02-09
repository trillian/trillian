Trillian
========
#### An All-Sky, Multi-wavelength Astronomy Computational Engine

Trillian is a project whose aim is to bridge the gap between astrophysical models and the vast amount of publicly available astronomical data. 

Its principle features include:

* a distributed data scheme
* distributed computation
* integrated API access to disparate data

A more detailed descripton of the project can be found here: [http://trillianverse.org](http://trillianverse.org).

An arXiv paper by Demitri Muna and Eric Huff that describes Trillian in more detail can be found here: [arXiv:1402.5932](http://arxiv.org/abs/1402.5932), and more details are available on the wiki (above).



Links
-----
Project home page: [http://trillianverse.org](http://trillianverse.org)  
Mozilla ScienceLab Collaborate page: [https://mozillascience.org/projects/trillian](https://mozillascience.org/projects/trillian)  
Mailing list: [https://groups.google.com/forum/#!forum/trillianverse](https://groups.google.com/forum/#!forum/trillianverse)  



## What Is Trillian?

Trillian is a project to create a next-generation astronomical archive, allowing astronomers to analyze hundreds of terabytes of data (or more!) as easily as they would dozens of files on their own hard drive.

#### The Problem.

Astronomy has generated *a lot* of freely available, public data. The recent [Pan-STARRS data release](http://panstarrs.stsci.edu) alone is 2PB in size, and that's just one telescope. The data is available through a number of archives around the world such as the [Space Telescope Science Institute](http://archive.stsci.edu),  [IPAC](http://ipac.caltech.edu), or [SDSS](https://dr13.sdss.org). There is no single, central repository of data. These archives are organized by the funding bodies for the telescopes or satellites, e.g. NASA or hosted by the individual surveys. Typically, this means that optical data will be in one archive, radio in another, infrared yet another, etc. This makes sense from an organizational of funding point of view, but it makes life difficult for the individual astronomer.

When an astronomer wants to study a particular set of objects, ideally she wants to get all of the observations that have been made of those objects. First, she must identify the archives that might contain data for those objects. Next, she will go to each of those archives and, most frequently, enter the positions in the sky she wants manually into a web form (where each web form is different) and download the files herself. Extracting the data from the files is another task – while all of the files will likely be in the [FITS format](https://github.com/trillian/trillian/wiki/What-is-a-FITS-file%3F), the data from each telescope or satellite will be organized differently. Finally, she will be able to use her code to analyze the data.

This manual process doesn’t scale to large data sets. The individual astronomer has limited time to visit all of the archives (assuming she is aware of all of them) so she uses the ones she's most familiar with, potentially leaving data on the table. She may be able to download data for hundreds or even thousands of objects, but not millions from several archives. She has limited disk space to download data (so, for that matter, does her department or whole university!). It's impossible to perform an analysis across many different observed wavelengths across the whole sky.

#### The Solution.

Trillian is a framework that aims to solve these problems. First, it is an archive that will organize astronomical data by position on the sky, not by wavelength. Even if you can programatically access all of the data needed remotely, you will spend more of your time waiting to download it.

If we can't bring the data to the astronomer’s code, let's bring the code to the data. By customizing a provided Python module template, the user can write their own, custom module to analzye data. Is radio data available? Let's use it. Are distance measurements available? Use them. The Trillian framework will supply the data available from any data set that has been indexed. The custom code is then placed into a Docker container and send to a server where the data is on disk. The data is analyzed, where the results stored in a database and made available to the user.

This is the only model of data analysis that can currently enable individuals with limited resources to analyze hundreds of terabytes (or even petabytes) of data. It will allow us to ask scientific questions of data – that is currently sitting on disk! – that we lack the tools to ask.



## Resources

The Trillian project is being developed at the [Center for Cosmology and Astroparticle Physics](http://ccapp.osu.edu) (CCAPP) at Ohio State University. CCAPP awarded the project a $10K startup fund which was used to purchase a ~30TB server to develop a proof of concept. While certainly not enough for all-sky coverage while trying to include even the most popular data sets, it’s more than enough for a both a proof of concept and scientific inquiry. Two regions on the sky have been chosen initially: SDSS’s Stripe 82 and the Kepler field, selected as they have been heavily studied and are good representative regions for both extragalactic and Galactic science. Data covering as many wavelengths as possible will be collected for these areas.



## Current Development Goals

The first milestone is to provide an arbitrarily simple model to Trillian, have the framework apply that model to all objects available, and return a likelihood value for each one. Current tasks include:

- Gather and index the metadata from as many astronomical data sets as possible (50TB indexed and counting!).
- Initialize the server with the coarsest resolution of HEALPix regions/trixels.
- Define the structure of each trixel (the storage on disk representation of each HEALPix region). This will include a schema for each data set (e.g. SDSS, WISE, etc.) in a shared database on each node, indexing of image data, etc.
- Define an API for accessing data between nodes.
- Implement a Docker VM that can accept a user-supplied Python program to be run on nodes.
- Define the API for the user-supplied Python code. This code will accept data in a defined format (limited on the first pass to magnitudes, spectra, and raw pixel data), and return a likelihood value that the provided data fits the model represented by the code.
- Define a job queue system (built on Redis?) for communication between the central server and the nodes.

## Support

*  Trillian is gratefully supported by the [Center for Cosmology and Astroparticle Physics (CCAPP)](http://ccapp.osu.edu) at Ohio State University.

*  The [Trillian project](https://science.mozilla.org/projects/trillian) was selected for Mozilla Science Lab’s [Collaborate on Software for Science](http://collaborate.mozillascience.org).

   ​

## Contact

The Trillian project is currently seeking collborators. If you are interested in contributing to this project, please contact [Demitri Muna](http://github.com/demitri).

