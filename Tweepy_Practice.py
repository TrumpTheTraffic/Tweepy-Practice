#!/usr/bin/env python

import tweepy

##[Insert keys here]

auth = tweepy.OAuthHandler(c_key, c_secret)
auth.set_access_token(a_token, a_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

##for tweet in public_tweets:
##	if tweet.user.screen_name == 'TrumpTheTraffic':
##		print tweet.mentions

mentions = api.mentions_timeline()

for mention in mentions:
	print '@' + mention.user.screen_name + ': ' + mention.text

