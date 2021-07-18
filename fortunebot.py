import os
import time
import tweepy
import random

COMMAND = "fortune"
if os.getenv("OFFENSIVE", None):
    COMMAND += " -o"

HASHTAGS = os.getenv("HASHTAGS", "").split(",")
MAX_TAGS = int(os.getenv("MAX_TAGS", 3))

MIN_TIME_BETWEEN_TWEETS = 60 * 60 * 6  # 6 Hours
MAX_TIME_BETWEEN_TWEETS = 60 * 60 * 12  # 12 Hours

try:
    MIN_TIME_BETWEEN_TWEETS = int(os.getenv("MIN_TIME_BETWEEN_TWEETS", None))
except: pass

try:
    MAX_TIME_BETWEEN_TWEETS = int(os.getenv("MAX_TIME_BETWEEN_TWEETS", None))
except: pass


auth = tweepy.OAuthHandler(os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_SECRET_KEY"))
auth.set_access_token(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)


while True:
    random.shuffle(HASHTAGS)
    hashtags = HASHTAGS
    if len(hashtags) > MAX_TAGS:
        hashtags = hashtags[:MAX_TAGS]

    hashtags = "\n" + " ".join(map(lambda x: "#"+x, hashtags))
    fortune = ""
    while fortune == "" or len(fortune) > 280:
        fortune = os.popen(COMMAND).read()+hashtags
        time.sleep(1)

    try:
        api.update_status(fortune)
        print("just tweeted: %s" % fortune)
    except Exception as e:
        print("failed to tweet fortune with len %d: %s" % (len(fortune), fortune))

    time.sleep(random.randint(MIN_TIME_BETWEEN_TWEETS, MAX_TIME_BETWEEN_TWEETS))

