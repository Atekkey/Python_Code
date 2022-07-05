"""from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

name = input("Enter - ")
search = name
for x in search:
    if(x==' '):
        search = search.replace(x, '_')
url = 'https://en.wikipedia.org/wiki/' + search
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print(soup.get_text())




tags = soup('p')
tagSum = ''
for tag in tags:
    tagSum += str(tag)
    tagSum += ' '
copies = re.findall(' *. copies', tagSum)
#print(copies, 'in', name)
print(tagSum)"""