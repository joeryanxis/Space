#!/usr/bin/python

from secrets import *

import random
import tweepy

# twitter setup

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

firstText = open('adjectives.txt')
firstList = firstText.readlines()
firstNum = random.randrange(len(firstList))
first = firstList[firstNum]


#get intro text
introText = open('nouns.txt')
introList = introText.readlines()
introNum = random.randrange(len(introList))
intro = introList[introNum]

middleText = open('verbs.txt')
middleList = middleText.readlines()
middleNum = random.randrange(len(middleList))
middle = middleList[middleNum]


#get outro text

outroText = open('nounsOut.txt')
outroList = outroText.readlines()
outroNum = random.randrange(len(outroList))
outro = outroList[outroNum]


tweet = first + intro + middle + outro
print (tweet)
tweet = tweet.replace('\n',' ')







#tweet = "I am a TWITTER BOT"

api.update_status(tweet)