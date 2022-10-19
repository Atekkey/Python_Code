from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re
import requests


result = requests.get('https://en.wikipedia.org/wiki/Super_Mario_World')
src = result.content
soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
for link in links:
    if(re.search("world", link)==True):
        print(link)