from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("URL - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
key = str(input("Search - "))
#Returns a list of all tags
tags = soup('a')
for tag in tags:
    tag = str(tag.get('href', None))
    found = re.findall(key, tag)
    if(key in found):
        print(tag)
print("done")