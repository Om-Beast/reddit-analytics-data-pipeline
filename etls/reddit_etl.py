import sys

import numpy as np
import pandas as pd
import praw
from praw import Reddit

from utils.constants import POST_FIELDS


def connect_reddit(
    client_id: str,
    client_secret: str,
    user_agent: str,
) -> Reddit:
    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            check_for_async=False,
        )
        print("Connected to Reddit successfully.")
        return reddit
    except Exception as exc:
        print(f"Failed to connect to Reddit: {exc}")
        sys.exit(1)


def extract_posts(
    reddit_instance: Reddit,
    subreddit: str,
    time_filter: str = "day",
    limit: int | None = None,
) -> list[dict]:
    subreddit_instance = reddit_instance.subreddit(subreddit)
    posts = subreddit_instance.top(time_filter=time_filter, limit=limit)

    post_list = []

    for post in posts:
        post_dict = vars(post)
        post_list.append(
            {
                field: post_dict.get(field)
                for field in POST_FIELDS
            }
        )

    return post_list


def transform_data(post_df: pd.DataFrame) -> pd.DataFrame:
    if post_df.empty:
        return post_df

    post_df = post_df.copy()

    post_df["created_utc"] = pd.to_datetime(
        post_df["created_utc"],
        unit="s",
        utc=True,
    )

    post_df["over_18"] = post_df["over_18"].fillna(False).astype(bool)
    post_df["author"] = post_df["author"].fillna("[deleted]").astype(str)

    post_df["edited"] = post_df["edited"].apply(
        lambda value: value if isinstance(value, bool) else False
    )

    post_df["num_comments"] = (
        pd.to_numeric(post_df["num_comments"], errors="coerce")
        .fillna(0)
        .astype(int)
    )

    post_df["score"] = (
        pd.to_numeric(post_df["score"], errors="coerce")
        .fillna(0)
        .astype(int)
    )

    post_df["title"] = post_df["title"].fillna("").astype(str)

    return post_df


def load_data_to_csv(data: pd.DataFrame, path: str) -> None:
    data.to_csv(path, index=False)