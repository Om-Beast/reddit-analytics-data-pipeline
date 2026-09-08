import pandas as pd
from quality.data_quality import validate_data

from etls.reddit_etl import (
    connect_reddit,
    extract_posts,
    load_data_to_csv,
    transform_data,
)
from utils.constants import (
    POST_LIMIT,
    REDDIT_CLIENT_ID,
    REDDIT_CLIENT_SECRET,
    REDDIT_USER_AGENT,
    SUBREDDIT,
)


def reddit_pipeline(
    file_path: str,
    subreddit: str = SUBREDDIT,
    time_filter: str = "day",
    limit: int = POST_LIMIT,
) -> str:
    if not REDDIT_CLIENT_ID or not REDDIT_CLIENT_SECRET:
        raise ValueError(
            "Reddit API credentials are missing. "
            "Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET."
        )

    reddit = connect_reddit(
        REDDIT_CLIENT_ID,
        REDDIT_CLIENT_SECRET,
        REDDIT_USER_AGENT,
    )

    posts = extract_posts(
        reddit,
        subreddit,
        time_filter,
        limit,
    )

    post_df = pd.DataFrame(posts)
    post_df = transform_data(post_df)
    validate_data(post_df)
    load_data_to_csv(post_df, file_path)

    return file_path