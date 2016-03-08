# Trillian Road Map

The following is a high-level road map describing the development path for Trillian. The shortest possible statement of the road map is:

 * Build only what is needed to reach the first publication.
 * Expand functionality after that.
 
Steps below link to further pages in the Trillian wiki that go into much more detail. These pages descibe the goal of each step and the details for impementation. Tasks are broken out down to the level of GitHub issues (which will then be linked from there).

---

## Road Map

Some of these steps depend on previous steps; others can be performed in parallel. The roadmap reflects these dependencies through milestones; each top level item within a milestone does not have prior dependencies.

###### Milestone 1: Create one data set

 * Design a database schema for the Trillian “command and control” server. It will need to manage the users, data available, and the jobs submitted to the server.
 * Add the first data source: imaging data from the [Sloan Digital Sky Survey](http://www.sdss.org/dr12/) (SDSS). Data added will be the subset of the SDSS covering [Stripe 82](http://www.physics.drexel.edu/~gtr/vla/stripe82/Deep_VLA_Observations_of_SDSS_Stripe_82.html), but Trillian will need to know what the entire footprint of the survey is.
 
 
 
 * Add a second data source.
 * Add further data sources as resources allow. Sources can be assigned each to interested individuals.
 * Design the basic Trillian data access API. This includes specifying the kind of data requested (catalog, imaging, etc.), wavelength range, magnitude range, location on sky, etc.
 * Design the unique properties of each data source into the API.
 * Create a new Docker module, identify the environment needed. Data will be accessed through the Docker container exclusively through the API.
 * Create a means to submit a Docker container to Trillian.
 * Define how the results of an analysis will be saved to the database (schema, API).
 * Run a very simple proof of concept analysis that spans multiple wavelengths and data sets.
 * Submit a simple, but scientifically interesting analysis via a Docker container.
 
Steps beyond here will be after publication (or at least the completion of all of the steps above).

 * Continue to add more data sets, striving for as wide a wavelength coverage as possible.
 * Perform more complex analyses.
 * Expand Trillian to a second node. This will involve the command and control server submitting and managing Docker containers on a remote server and managing remote data sets that expand sky coverage.
 
 
 