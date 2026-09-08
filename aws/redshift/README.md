\# Amazon Redshift



Redshift is the warehouse target for curated Reddit data.



The initial warehouse schema is defined in:



`sql/redshift/schema.sql`



The production implementation will load validated datasets from the S3-based data lake into Redshift for analytical workloads.

