from bs4 import BeautifulSoup
import urllib2

rootUrl = "https://www.etsy.com/search?q="
item = "5 panel hat"

def get_soup(url, header):
		return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)), 'html.parser')

#soup stuff
url = rootUrl + item
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

soup = get_soup(url,header)
prices = soup.findAll(attrs={"class":"element2"})

f = open('listName.txt', 'w') #creates a document and makes it writable

print()

for i in prices:
	f.write(i.string + '\n')

f.close()
#print(prices[0].string)