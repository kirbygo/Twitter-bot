import tweepy

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

# Create a tweet
api.update_status("Ando aprendiendo Tweepy, a ver si sí jala :P")