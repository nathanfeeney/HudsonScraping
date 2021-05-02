import json
import urllib
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup


url = 'https://dev-test.hudsonstaging.co.uk/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
productInfoArr = []
contentArr = []


for info in content.findAll('div', attrs={"class": "product-tile"}):
    productObject = {
        "product": info.find('p', attrs={"class": "product-name"}).text,
        "meta data": {
         #this finds all <p> tags at the 2rd index and strips the text
        "Quantity": info.findAll('p')[1].text.strip("Quantity: "),
          #this finds all <p> tags at the 3rd index and strips the text and currency
         "Price": info.findAll('p')[2].text.strip("Price: $"),
          #this finds all <img> tags at gets the src value
         "img-url": info.find("img").get('src')
    }}
    productInfoArr.append(productObject)
with open('productInfo.json', 'w') as outfile:
    json.dump(productInfoArr, outfile, indent=1)
    print("file created")
