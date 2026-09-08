-- Top posts by engagement
SELECT
    id,
    title,
    score,
    num_comments,
    author,
    created_utc
FROM reddit_posts
ORDER BY
    (score + num_comments) DESC
LIMIT 20;


-- Daily engagement summary
SELECT
    DATE(created_utc) AS post_date,
    COUNT(*) AS total_posts,
    SUM(score) AS total_score,
    SUM(num_comments) AS total_comments,
    AVG(score) AS avg_score
FROM reddit_posts
GROUP BY DATE(created_utc)
ORDER BY post_date DESC;


-- Most active authors
SELECT
    author,
    COUNT(*) AS post_count,
    SUM(score) AS total_score,
    SUM(num_comments) AS total_comments
FROM reddit_posts
WHERE author IS NOT NULL
GROUP BY author
ORDER BY post_count DESC
LIMIT 20;