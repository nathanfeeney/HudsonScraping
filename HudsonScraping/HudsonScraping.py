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
         "meta data": {
          "Quantity": tweet.findAll('p')[1].text.strip("Quantity: "),
          "Price": tweet.findAll('p')[2].text.strip("Price: $"),
          "img-url": tweet.find("img").get('src')
    }}
    productNameArr.append(productObject)

with open('katrina.json', 'w') as outfile:
    json.dump(productNameArr, outfile, indent=1)
    print("file created")
