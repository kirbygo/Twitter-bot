import tweepy
import os
import time
#import json

# Config vars
token = os.environ['API_KEY']
tokensec = os.environ['API_KEY_SECRET']
tokenacc = os.environ['ACCESS_TOKEN']
tokenaccsec = os.environ['ACCESS_TOKEN_SECRET']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(token,tokensec)
auth.set_access_token(tokenacc,tokenaccsec)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def bot(tweet_text, screen_name):
    reply = 'Hola, @' + screen_name + ': ' + 'Solo pasaba para informarte que no se dice "en base a", se dice "con base en". Saludos! -> ' + tweet_text
    return reply

class BotStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        # Ignorar los propios, RT y que diga "en base a" literal haha
        if tweet.user.id_str == self.me.id_str:
            print('ignoramos los propios')
            return
        
        if (not tweet.retweeted) and ('RT @' not in tweet.text) and ('en base a' in tweet.text) and ('bot' not in tweet.text) and ('@en_base_a_bot' not in tweet.text):
            reply = None
            try:
                reply = bot(tweet.text, tweet.user.screen_name)
            except Exception as exc:
                print(f'el pedo: {exc}')

            if reply:
                print(f'RESPONDEMOS: {reply}')
                api.update_status(f"@{tweet.user.screen_name} {reply}", tweet.id_str)
                time.sleep(61)

# Listener
bot_listener = BotStreamListener(api)

# llamamos el streaming
my_bot = tweepy.Stream(auth=api.auth, listener=bot_listener)
me = api.me()

# filtrín
my_bot.filter(track=['en base a'], languages=["es"])
