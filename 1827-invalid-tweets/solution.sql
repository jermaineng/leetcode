# Write your MySQL query statement below
SELECT tweet_id from Tweets
WHERE CHAR_LENGTH(content) > 15;

# LENGTH() returns the length of the string measured in bytes
# CHAR_LENGTH() returns the length of the string measured in characters
# LENGTH works here because the characters are only english characters and not special characters
