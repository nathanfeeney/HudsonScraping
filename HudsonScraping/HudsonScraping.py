from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://dev-test.hudsonstaging.co.uk/")
bsObj = BeautifulSoup(html.read(), 'lxml')
nameList = bsObj.findAll("p",{"class": "product-name"})
for name in nameList:
        print(name.get_text())

