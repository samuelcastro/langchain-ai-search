import os
from dotenv import load_dotenv
import tweepy
import requests

load_dotenv()

twitter_client = tweepy.Client(
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
    consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
    consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
)


def scrape_user_tweets(username: str, num_tweets=5, mock: bool = False):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    """

    tweet_list = []

    if mock:
        TWITTER_GIST = "https://gist.githubusercontent.com/samuelcastro/1fb4e0e33ecd7d8bbd8bca2ad7e0bcd1/raw/83423729b49b392dce33fcadb431b55d49eb286d/twitter.json"
        tweets = requests.get(TWITTER_GIST, timeout=5).json()

    else:
        user_id = twitter_client.get_user(username=username).data.id
        tweets = twitter_client.get_user_tweets(
            id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
        )
        tweets = tweets.data

    for tweet in tweets:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://x.com/{username}/status/{tweet['id']}"
        tweet_list.append(tweet_dict)

    return tweet_list


if __name__ == "__main__":
    tweets = scrape_user_tweets(username="samuelcasilva", mock=True)
    print(tweets)
