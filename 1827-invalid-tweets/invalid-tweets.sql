SELECT tweets.tweet_id
FROM tweets
WHERE CHAR_LENGTH(tweets.content) > 15;