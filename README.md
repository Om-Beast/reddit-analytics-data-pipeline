# Reddit Analytics Data Pipeline

A production-oriented batch data engineering pipeline for collecting Reddit data, transforming it with Python, orchestrating workflows with Apache Airflow, and preparing analytics data for AWS analytics services.

## Architecture

```text
Reddit API
    ↓
Apache Airflow
    ↓
Python ETL (Pandas)
    ↓
Data Quality Validation
    ↓
Local Staging
    ↓
Amazon S3
    ↓
AWS Glue + Athena
    ↓
Amazon Redshift