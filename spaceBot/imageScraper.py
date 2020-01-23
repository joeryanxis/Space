from bs4 import BeautifulSoup
import urllib2
import os
import json
import random

# image settings    
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
f = open(os.path.join(save_directory , "img" + "_"+ str(imgNum)+".jpg"), 'wb')
f.write(raw_img)
f.close()