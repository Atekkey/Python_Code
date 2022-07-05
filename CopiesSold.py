from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

gameA = input("Enter - ")
game = gameA
for x in game:
    if(x==' '):
        game = game.replace(x, '_')
url = 'https://en.wikipedia.org/wiki/' + game
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('p')
tagSum = ''
for tag in tags:
    tagSum += str(tag)
    tagSum += ' '
copies = re.findall('[a-z0-9]+ [a-z]+ copies', tagSum)[0]
print(copies, 'of', gameA, 'were sold')
print(tagSum)