from etls.aws_etl import upload_to_s3


def upload_s3_pipeline(
    file_path: str,
    object_key: str,
) -> str:
    upload_to_s3(file_path, object_key)
    return object_key