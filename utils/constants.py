import os

from dotenv import load_dotenv

load_dotenv()

# Reddit
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv(
    "REDDIT_USER_AGENT",
    "reddit-analytics-pipeline/1.0",
)

# AWS
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# Pipeline
SUBREDDIT = os.getenv("SUBREDDIT", "dataengineering")
POST_LIMIT = int(os.getenv("POST_LIMIT", "100"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

POST_FIELDS = (
    "id",
    "title",
    "score",
    "num_comments",
    "author",
    "created_utc",
    "url",
    "over_18",
    "edited",
    "spoiler",
    "stickied",
)