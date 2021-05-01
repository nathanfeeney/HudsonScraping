import json
import urllib
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup


url = 'https://dev-test.hudsonstaging.co.uk/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
productNameArr = []
productInfoArr = []
for tweet in content.findAll('div', attrs={"class": "product-tile"}):
    productObject = {
        "product": tweet.find('p', attrs={"class": "product-name"}).text,
         "meta data": tweet.findAll('p')[1].text,
         "": tweet.findAll('p')[2].text
    }
    productNameArr.append(productObject)
#for tweet in content.findAll('div', attrs={"class": "details"}):
   # infoObject = {   
       
        #"metadataTest": tweet.findAll(text='Quantity:', items=2)
    #}
    
   # productInfoArr.append(infoObject)
with open('productNEW.json', 'w') as outfile:
    json.dump(productNameArr, outfile)
  #  json.dump(productInfoArr, outfile)
    print("file created")