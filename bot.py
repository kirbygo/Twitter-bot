import tweepy
import os
import json

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, status):
        if status.retweeted_status:
            return
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error, putito...")

# Config vars
token = os.environ['API_KEY']
tokensec = os.environ['API_KEY_SECRET']
tokenacc = os.environ['ACCESS_TOKEN']
tokenaccsec = os.environ['ACCESS_TOKEN_SECRET']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(token,tokensec)
auth.set_access_token(tokenacc,tokenaccsec)

# Create API object
api = tweepy.API(auth,  wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#tweets_listener = MyStreamListener(api)
#stream = tweepy.Stream(api.auth, tweets_listener)
#stream.filter(track=["en base a"], languages=["es"])






# Crear un tweet
api.update_status("Desde Heroku")

# Buscar tweets
# for tweet in api.search(q="Python", lang="en", rpp=10):
#    print(f"{tweet.user.name}:{tweet.text}")