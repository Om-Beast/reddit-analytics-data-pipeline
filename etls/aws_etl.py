import boto3

from utils.constants import AWS_REGION, S3_BUCKET_NAME


def create_s3_client():
    return boto3.client(
        "s3",
        region_name=AWS_REGION,
    )


def upload_to_s3(file_path: str, object_key: str) -> None:
    if not S3_BUCKET_NAME:
        raise ValueError("S3_BUCKET_NAME is not configured.")

    s3_client = create_s3_client()

    s3_client.upload_file(
        file_path,
        S3_BUCKET_NAME,
        object_key,
    )