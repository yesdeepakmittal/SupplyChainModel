import requests
import csv
import sys
import time


def request_until_succeed(url):
    while True:
        try:
            res = requests.get(url, timeout=10)
        except Exception as e:
            print("ERROR: {0}".format(e))
            print("Retrying in 5s.")
            time.sleep(5)
            continue

        if res.status_code == 200:
            return res.text
        else:
            print("STATUS CODE {0} @ {1}\n".format(
                res.status_code,
                url,
            ))
            print("Retrying in 5s.")
            time.sleep(5)

def open_csv_w(filename):
    """Open a csv file in proper mode depending on Python verion."""
    import io
    return(io.open(filename, mode='w',encoding="utf-8") if sys.version_info[0] == 2 else
           io.open(filename, mode='w', newline='',encoding="utf-8"))

import tweepy #https://github.com/tweepy/tweepy
import csv
# from utils import open_csv_w
# import authentication credentials
TWITTER_C_KEY  = '🎯enter your C_key here'
TWITTER_C_SECRET = '🎯enter your c_secret here'
TWITTER_A_KEY= '🎯enter your a_key here'
TWITTER_A_SECRET= '🎯enter your a_secret here'


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method

	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(TWITTER_C_KEY, TWITTER_C_SECRET)
	auth.set_access_token(TWITTER_A_KEY, TWITTER_A_SECRET)
	api = tweepy.API(auth)

	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print("getting tweets before %s" % (oldest))

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print("...%s tweets downloaded so far" % (len(alltweets)))


	#transform the tweepy tweets into a 2D array that will populate the csv	| you can comment out data you don't need
	outtweets = [[tweet.id_str,
				tweet.created_at,
				tweet.favorite_count,
				tweet.retweet_count,
				tweet.retweeted,
				tweet.source,
				tweet.text,
				tweet.geo,
				tweet.lang,
				tweet.is_quote_status,
				tweet.user.name,
				tweet.user.screen_name,
				tweet.user.location,
				tweet.user.description,
				tweet.user.protected,
				tweet.user.followers_count,
				tweet.user.friends_count,
				tweet.user.listed_count,
				tweet.user.created_at,
				tweet.user.favourites_count,
				tweet.user.utc_offset,
				tweet.user.time_zone,
				tweet.user.geo_enabled,
				tweet.user.verified,
				tweet.user.statuses_count,
				tweet.user.lang
				]

				for tweet in alltweets]


	#write the csv
	with open_csv_w('%s_tweets.csv' % screen_name) as f:
		writer = csv.writer(f)
		writer.writerow(["id",
				"created_at",
				"favorites",
				"retweets",
				"retweeted",
				"source",
				"text",
				"geolocation",
				"language",
				"is_quote_status",
				"username",
				"user_screen_name",
				"user_location",
				"user_description",
				"user_protected",
				"user_followers_count",
				"user_friends_count",
				"user_listed_count",
				"user_created_at",
				"user_favourites_count",
				"user_utc_offset",
				"user_time_zone",
				"user_geo_enabled",
				"user_verified",
				"user_statuses_count",
				"user_lang"])
		writer.writerows(outtweets)

	pass



if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("yesdeepakmittal")

from sentiment import sentiment
import pandas as pd
import numpy as np
temp = []
df = pd.read_csv('yesdeepakmittal_tweets.csv')
for i in df['text']:
    temp.append(sentiment(i))

df = pd.DataFrame(temp,columns=['sentiment','confidence']).join(df['created_at'])
df['sent_value'] = np.where(df['sentiment'] == 'pos',1,-1)
df.rename(columns={'created_at':'time'},inplace=True)
df.to_csv('yesdeepakmittal_tweets.csv')
del df
