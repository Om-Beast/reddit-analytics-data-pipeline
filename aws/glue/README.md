\# AWS Glue



This directory contains the AWS Glue layer for cataloging the Reddit dataset stored in Amazon S3.



\## Planned flow



S3 raw data

→ Glue Crawler

→ Glue Data Catalog

→ Athena



The crawler should discover the date-partitioned Reddit dataset and maintain table metadata for downstream SQL analytics.

