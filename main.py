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

retweeted = set()

target_username = "Estuary_Tech"
query = f"from:{target_username}"

one_hour = 60*60

if __name__ == "__main__":
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret,
    )

    target_user = client.get_user(username=target_username)

    while True:
        try:
            latest_tweets = client.search_recent_tweets(query, max_results=20).data
            for tweet in latest_tweets:
                time.sleep(2)
                if tweet.id not in retweeted:
                    print(f"Retweeting {tweet.id} now: '{tweet.text}'")
                    client.retweet(tweet.id)
                    client.like(tweet.id)
                    retweeted.add(tweet.id)
                else:
                    print(f"Skipping tweet {tweet.id}. Already retweeted.")
        except:
            print("Twitter doesn't like me, waiting 5 minutes and retrying...")
            time.sleep(5*60)
        time.sleep(one_hour)


