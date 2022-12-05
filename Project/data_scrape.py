import json
import re

import matplotlib.pyplot as plt
import nltk
import pandas as pd
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud

TWITTER_API_KEY = "8r4bvIuCRsNzrbdPsCqaUoVv9"
TWITTER_API_SECRET = "JptZjnN991736aSssz4F8RUaOPtTHEOejNyDGb064KAjPJ2GMU"
TWITTER_ACCESS_TOKEN = "1297797286148399104-JTeBfDEIMD5xDmuzgtmiOcJMrurhFx"
TWITTER_ACCESS_SECRET = "FmJFEJjFiJEMMRAHenXe1dCNpPD6lz02mKuZVMzBP9b7c"

# Authentificate with Twitter
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)

total_tweets = 100000

# Create the API object
api = tweepy.API(auth, wait_on_rate_limit=True)

hashtag = "#RIPtwitter -filter:retweets"
results = tweepy.Cursor(
    api.search_tweets, q=hashtag, lang="en", tweet_mode="extended"
).items(total_tweets)

with open("Project/data.json", "w") as f:
    json.dump([tweet.full_text for tweet in results], f)
