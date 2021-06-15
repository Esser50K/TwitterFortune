import os
import time
import tweepy
import random

COMMAND = "fortune"
if os.getenv("OFFENSIVE", None):
    COMMAND += " -o"

MIN_TIME_BETQEEN_TWEETS = 60 * 60 * 6 # 6 Hours
MAX_TIME_BETQEEN_TWEETS = 60 * 60 * 12 # 12 Hours

auth = tweepy.OAuthHandler(os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_SECRET_KEY"))
auth.set_access_token(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

while(True):
    fortune = ""
    while fortune == "" or len(fortune) > 280:

        fortune = os.popen(COMMAND).read()
        time.sleep(1)

    try:
        api.update_status(fortune)
        print("just tweeted: %s" % fortune)
    except Exception as e:
        print("failed to tweet fortune with len %d: %s" % (len(fortune), fortune))

    time.sleep(random.randint(MIN_TIME_BETQEEN_TWEETS, MAX_TIME_BETQEEN_TWEETS))

