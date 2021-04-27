from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://dev-test.hudsonstaging.co.uk/")
bsObj = BeautifulSoup(html.read(), 'lxml')
print(bsObj.p)
