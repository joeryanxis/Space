from bs4 import BeautifulSoup
from io import BytesIO

from PIL import Image
from PIL import ImageFile
 
import urllib
from urllib import request 
import os
import json
import random
import tweepy
import requests
import csv

#from pixelsort import *

from secrets import *

#twitter setup
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

my_mentions = api.mentions_timeline() #see if I have any new mentions

user = "@"+my_mentions[0].author.screen_name #find out who tweeted @ me
statusID = my_mentions[0].id 


tweetInitial = my_mentions[0].text #see what they tweeted

checkFile = open(r'C:\Users\Joe\Dropbox\Space\spaceBot\Tweet.txt', 'r')#a check to make sure i'm not doubling up on old mentions
check = checkFile.read()

equal = "equal"
f = open(r'C:\Users\Joe\Dropbox\Space\spaceBot\Tweet.txt', 'w')

set1 = set(check.split(' '))
set2 = set(tweetInitial.split(' '))

#print tweetInitial
f.write(tweetInitial)

f.close()


tweet = tweetInitial.replace("@databoy87954009 ", '')
tweetNoSpaces = tweet.replace(" ", '')
tweetList = tweetNoSpaces.splitlines()
tweetFinal = ''.join(tweetList)
print(tweet)
print(tweetFinal)
output = user + " " + tweet + "!" #what my final tweet in response is going to say
#print(output)

#This is for when I don't have any new mentions, so I can search for something cool from a list of topics I already have
mySearch = open(r'C:\Users\Joe\Dropbox\Space\spaceBot\searches.txt')
mySearchList = mySearch.read().splitlines()
mySearchNum = random.randrange(len(mySearchList))
SearchTerm = mySearchList[mySearchNum]

#Scraper

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

def tweet_image(searchTerm):
	#searchTerm = "space"
	save_directory = r"C:\Users\Joe\Dropbox\Space\spaceBot\images/"
	# soup settings    
	url=r"https://www.google.co.in/search?q="+searchTerm+"&source=lnms&tbm=isch"
	header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
	soup = get_soup(url,header)

	ActualImages=[]
	for a in soup.find_all("div",{"class":"rg_meta"}):
	    link =json.loads(a.text)["ou"]
	    ActualImages.append(link)
	    
	imgNum = random.randrange(len(ActualImages))
	thisImg = ActualImages[imgNum]
	
	imageName = searchTerm + str(imgNum) + ".jpeg"
	urllib.request.urlretrieve(thisImg,"download.jpeg")

	a = random.randrange(90)
	angle = str(a)

	b = random.uniform(.6,1.8)
	bigB = str(1.8)

	r = random.randrange(99)
	randomness = str(r)

	#os.system(r'python C:\Users\Joe\Dropbox\Space\spaceBot\pixelsort.py C:\Users\Joe\Dropbox\Space\spaceBot\images\ ' + imageName + r' -o C:\Users\Joe\Dropbox\Space\spaceBot\File.png -i threshold -s intensity -a' + angle + ' -u ' + bigB + ' -t .1')
	os.system(r'python pixelsort.py -o sortedImage.png -a ' + angle +  ' -r ' + randomness + ' download.jpeg')

	print(imageName)

	img = r'C:\Users\Joe\Dropbox\Space\spaceBot\sortedImage.png'
	im = Image.open(img)
	rgb_im = im.convert('RGB')
	rgb_im.save(r'C:\Users\Joe\Dropbox\Space\spaceBot\New.jpeg')

	height = 500
	width = 500

	im2 = Image.open(r'C:\Users\Joe\Dropbox\Space\spaceBot\New.jpeg')
	im3 = im2.resize((width,height), Image.ANTIALIAS)
	im3.save(r"C:\Users\Joe\Dropbox\Space\spaceBot\Final.jpeg")


	#tweet = ""

	api.update_with_media(r'C:\Users\Joe\Dropbox\Space\spaceBot\Final.jpeg', output)

if set1 != set2:
	#when it tweets in reponse to someone
	counter = 0;
	count = open(r'C:\Users\Joe\Dropbox\Space\spaceBot\count.txt','w')
	count.write(str(counter))
	count.close()
	print ("Not equal")
	tweet_image(tweetFinal)

if set1 == set2:
	count = open(r'C:\Users\Joe\Dropbox\Space\spaceBot\count.txt', 'r')
	counter = int(count.read())
	count.close()
	if counter == 6:
		print (SearchTerm)
		SearchTerm2 = SearchTerm.replace('/n','')
		output = SearchTerm + '!'
		tweet_image(SearchTerm2)
		counter = 0;
	counter = counter + 1
	count = open(r'C:\Users\Joe\Dropbox\Space\spaceBot\count.txt','w')
	count.write(str(counter))
	count.close()
	print ("Equal")

#tweet_image(tweetFinal) #final call used to test















