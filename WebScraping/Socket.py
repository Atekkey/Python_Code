import re
"""x = "the quick brown fox jumped over the lazy dog"
y = re.findall('(t[^ ]*) l', x)
print(y)"""

"""import socket
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mySock.send(cmd)

while True:
    data = mySock.recv(600)
    if (len(data) < 1):
        break
    print(data.decode())
mySock.close()"""
"""
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
"""
from bs4 import BeautifulSoup