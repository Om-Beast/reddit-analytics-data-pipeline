import pandas as pd


REQUIRED_COLUMNS = {
    "id",
    "title",
    "score",
    "num_comments",
    "author",
    "created_utc",
}


def validate_schema(df: pd.DataFrame) -> None:
    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )


def validate_not_empty(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("Dataset is empty.")


def validate_unique_ids(df: pd.DataFrame) -> None:
    if df["id"].duplicated().any():
        raise ValueError("Duplicate Reddit post IDs detected.")


def validate_numeric_fields(df: pd.DataFrame) -> None:
    for column in ("score", "num_comments"):
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise ValueError(f"{column} must be numeric.")


def validate_data(df: pd.DataFrame) -> None:
    validate_not_empty(df)
    validate_schema(df)
    validate_unique_ids(df)
    validate_numeric_fields(df)