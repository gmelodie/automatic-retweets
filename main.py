import tweepy
import time
import os
from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env.
consumer_key=os.environ.get("CONSUMER_KEY")
consumer_secret=os.environ.get("CONSUMER_SECRET")
access_token=os.environ.get("ACCESS_TOKEN_KEY")
access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET")
bearer_token=os.environ.get("BEARER_TOKEN")

latest_retweeted = None

target_username = "Estuary_Tech"
query = f"from:{target_username}"


if __name__ == "__main__":
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret,
    )

    target_user = client.get_user(username=target_username)
    print(f"Retweeting from {target_username}")

    while True:
        latest_tweet = client.search_recent_tweets(query, max_results=10).data[0]
        if latest_tweet != latest_retweeted or latest_retweeted is None:
            print(f"Retweeting {latest_tweet.id} now: '{latest_tweet.text}'")
            client.retweet(latest_tweet.id)
            latest_retweeted = latest_tweet
        time.sleep(60)

