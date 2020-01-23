from bs4 import BeautifulSoup
import urllib2

rootUrl = "https://www.etsy.com/search?q="
item = "world%20globes"

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

# soup settings    
url = rootUrl + item
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

soup = get_soup(url,header)

prices = soup.findAll(attrs={"class":"currency-value"})
names = soup.findAll(attrs={"class":"text-gray text-truncate mb-xs-0 text-body"})

f = open('globePrices.txt', 'w')

print(names[0].string.split('\n'))

for i in prices:
	f.write('$' + i.string + '\n')
	
f.close()
