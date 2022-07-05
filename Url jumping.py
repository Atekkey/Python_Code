from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def urlTags(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup("a")
    tagList = []
    for tag in tags:
        tag = str(tag.get('href', None))
        tag = re.findall('^/wiki.*', tag)
        if(tag != []):
            tagList.append(tag)
    return tagList

urlList1 = urlTags("https://en.wikipedia.org/wiki/orange")
urlList2 = urlTags("https://en.wikipedia.org/wiki/pear")
urlListRemove = urlTags("https://en.wikipedia.org/wiki/Apple")

for url in urlList1:
    if(url in urlListRemove):
        urlList1.remove(url)
for url in urlList2:
    if(url in urlListRemove):
        urlList2.remove(url)
for url in urlList1:
    if(url in urlList2):
        print(url)
