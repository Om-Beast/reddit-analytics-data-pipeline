CREATE TABLE IF NOT EXISTS reddit_posts (
    id VARCHAR(50) NOT NULL,
    title VARCHAR(500),
    score INTEGER,
    num_comments INTEGER,
    author VARCHAR(255),
    created_utc TIMESTAMP,
    url VARCHAR(1000),
    over_18 BOOLEAN,
    edited BOOLEAN,
    spoiler BOOLEAN,
    stickied BOOLEAN
);