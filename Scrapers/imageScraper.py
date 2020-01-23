from bs4 import BeautifulSoup
import urllib
from urllib import request
import os
import json
import random

# image settings    
searchTerm = input("What would you like to search for? \n")

save_directory = "images/"

print("Okay, searching for " + searchTerm + "...")

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

# soup settings    
url="https://www.google.co.in/search?q="+searchTerm+"&source=lnms&tbm=isch"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
soup = get_soup(url,header)

ActualImages=[]
for a in soup.find_all("div",{"class":"rg_meta"}):
    link =json.loads(a.text)["ou"]
    ActualImages.append(link)
    
print(len(ActualImages))
imgNum = random.randrange(len(ActualImages))#gets the number of the image, from the list of available images

thisImg = ActualImages[imgNum]#assignes the url of the image to thisImg

imgName = searchTerm + str(imgNum) + ".jpg" #what we call the saved file from image download
urllib.request.urlretrieve(thisImg, save_directory + imgName) #saves the image at the url thisImg, and then saves it in the save directory, with the name imgName
