import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#url = input('Enter the url - ')
url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')


#Retrieve all the anchor tag
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))