#!/usr/bin/python

from secrets import *

import random
import tweepy

# twitter setup

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

firstText = open('C:\Users\Joe\Dropbox\Space\Bots\Adjectives.txt')
firstList = firstText.readlines()
firstNum = random.randrange(len(firstList))
first = firstList[firstNum]


#get intro text
introText = open('C:\Users\Joe\Dropbox\Space\Bots\Nouns.txt')
introList = introText.readlines()
introNum = random.randrange(len(introList))
intro = introList[introNum]

middleText = open('C:\Users\Joe\Dropbox\Space\Bots\Verbs.txt')
middleList = middleText.readlines()
middleNum = random.randrange(len(middleList))
middle = middleList[middleNum]


#get outro text

outroText = open('C:\Users\Joe\Dropbox\Space\Bots\NounsOut.txt')
outroList = outroText.readlines()
outroNum = random.randrange(len(outroList))
outro = outroList[outroNum]


tweet = first + intro + middle + outro
print tweet
tweet = tweet.replace('\n',' ')



user = api.get_user('GdSpdBotEmperor')
for friend in user.friends():
   print(friend.screen_name)



#tweet = "I am a TWITTER BOT"

api.update_status(tweet)