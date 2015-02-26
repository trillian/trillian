#### Populating a Node

These steps assume that a node exists and has been configured with a running database.

 1. Identify node
 2. Check that schema exists in node's database
    * If not, create schema
 3. Populate data
 

#### Dividing a Node
 
  1. Identify the node to split
  2. Split the HEALPix pixels in the database, keeping the node location on the current node
  3. For each data set, identify the data in the database that falls within the healpixel to be moved. "Bookmark" the data.
  4. Copy the data to the new node’s database (dump/restore).
  5. Sanity check the data.
  6. Delete the set identified in the bookmark.
  7. Repeat with files.