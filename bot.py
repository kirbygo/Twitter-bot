import tweepy
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

# Authenticate to Twitter
auth = tweepy.OAuthHandler("rCrxISeNNSzeAkZiTA4nrk1fX", "sppCdj4Txbwm7VisaFcXcyqADQaywi5X6FTTvvnRIT1W5ZHnzI")
auth.set_access_token("82220649-OGt1O8Jv0L6IwZmmUwcjc4Z3br7PqCwU0DtG3gzxO", "3gNQGaxN9QlC7x1poxqb8Uin6lSGcOBfAuIcJZHAHYUS5")

# Create API object
api = tweepy.API(auth,  wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["en base a"], languages=["es"])



# Crear un tweet
# api.update_status("Ando aprendiendo Tweepy, a ver si sí jala :P")

# Buscar tweets
# for tweet in api.search(q="Python", lang="en", rpp=10):
#    print(f"{tweet.user.name}:{tweet.text}")