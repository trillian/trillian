## PostgreSQL + Polygon Indexing Notes

Creating an index on a `polygon` field:

    CREATE INDEX polygon_idx ON table_name USING gist(polygon_field);
Ref: https://wiki.postgresql.org/wiki/Indexable_Operators

Geometry operators: https://www.postgresql.org/docs/9.5/static/functions-geometry.html




