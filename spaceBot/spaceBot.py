from bs4 import BeautifulSoup
from io import BytesIO

from PIL import Image
from PIL import ImageFile

import urllib2
import os
import json
import random
import tweepy
import requests

#from pixelsort import *

from secrets import *

#twitter setup
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

#creates a class inheriting from the tweepy StreamListener
#class BotStreamer(tweepy.StreamListener):
#	#called when a new status arrives which is passed down from the on_data method of streamlistener
#	def on_status(self, status):
#		username = status.user.screen_name
#		status_id = status.id 
#		#
#		if 'media' in status.entities:
#			for image in status.entities['media']:
#				tweet_image(image['media_url'], username, status_id)

#myStreamListener = BotStreamer()

#stream = tweepy.Stream(auth, myStreamListener)
#stream.filter(track=["@databoy87954009"])
#Scraper
searchTerm = "space"
save_directory = "images/"

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

# soup settings    
url="https://www.google.co.in/search?q="+searchTerm+"&source=lnms&tbm=isch"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
soup = get_soup(url,header)

ActualImages=[]
for a in soup.find_all("div",{"class":"rg_meta"}):
    link =json.loads(a.text)["ou"]
    ActualImages.append(link)
    
imgNum = random.randrange(len(ActualImages))
thisImg = ActualImages[imgNum]
req = urllib2.Request(thisImg, headers={'User-Agent' : header})
raw_img = urllib2.urlopen(req).read()
imageName = "img_" + str(imgNum) + ".jpeg"
f = open(os.path.join(save_directory , imageName), 'wb')
f.write(raw_img)
f.close()

a = random.randrange(90)
angle = str(a)

b = random.uniform(.6,1.8)
bigB = str(b)

r = random.randrange(99)
randomness = str(r)

os.system('python pixelsort.py images/' + imageName + ' -o file.png -i threshold -s intensity -a ' + angle + ' -u ' + bigB + ' -r ' + randomness)



img = 'file.png'
im = Image.open(img)
rgb_im = im.convert('RGB')
rgb_im.save('new.jpeg')

height = 500
width = 500

im2 = Image.open('new.jpeg')
im3 = im2.resize((width,height), Image.ANTIALIAS)
im3.save("final.jpeg")


#tweet = ""

api.update_with_media('final.jpeg', searchTerm)