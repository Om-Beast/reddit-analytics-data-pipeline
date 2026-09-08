import pandas as pd
import pytest

from quality.data_quality import (
    validate_data,
    validate_unique_ids,
)


def valid_dataframe():
    return pd.DataFrame(
        {
            "id": ["a1", "a2"],
            "title": ["Post 1", "Post 2"],
            "score": [10, 20],
            "num_comments": [2, 5],
            "author": ["user1", "user2"],
            "created_utc": pd.to_datetime(
                ["2026-01-01", "2026-01-02"]
            ),
        }
    )


def test_valid_dataset():
    validate_data(valid_dataframe())


def test_duplicate_ids_fail():
    df = valid_dataframe()
    df.loc[1, "id"] = "a1"

    with pytest.raises(ValueError):
        validate_unique_ids(df)


def test_empty_dataset_fails():
    df = valid_dataframe().iloc[0:0]

    with pytest.raises(ValueError):
        validate_data(df)