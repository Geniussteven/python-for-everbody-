显示字母位置
print(ord('H'))#ordinal
72
unicode通用sets
ASCII
American Standard Code for I
UTF-8 1-4bytes The best way to encode data
UTF-16 2
UTF-32 4
在python3
x = 'hahaha'
type(x)->class str
x = u'hahaha'
type(x)->class str
在python2
x = u'hahaha'
type(x)->class unicode#strings stored internally in Python 3 as Unicode
prefixing前缀
 And so there's always been a thing like a byte string and they do this by prefixing the b.
x = b'abc'
type x ->class 'bytes'

将bytes decode-》Unicode
#web scraping网络抓取；retrieve检索
Question 4
In this Python code, which line is most like the open() call to read a file:

CS自学指南https://csdiy.wiki/
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

Answer:
mysock.connect()

#urllib
improt 一些库urllib
fhand = urllib.request.urlopen('http域名')#类似于open域名文件
for line in fhand:
print(line.decode().strip())#line 其实是byte array,需要解码成string

就像对待file一样对待
improt 一些库urllib
fhand = urllib.request.urlopen('http域名')
counts = dict()
for line in fhand:
 words = line.decode().split()
 for word in words:
  counts[emails] = counts.get(eamils, 0) + 1
print(counts)

用之前的代码逻辑

for line in name :
    line.decode().split()
    for emails in line[5] :
        counts[emails] = counts.get(eamils, 0) + 1
lst = list()
#scraping 
'''meaning：一段python程序伪装成一个浏览器，可以retrieve webpages，
可以提取信息，获取更多的链接。再去获得更多的网页，类似爬网。
爬网最大问题是对回来的HTML进行解析。当你的浏览器检索HTML时，它会经过一大堆事情，有效地原谅了HTML中的语法错误。
事实证明，网络上有很多HTML都有语法错误，但你甚至都没有注意到。'''
'''BeautifulSoup的库-HTML超级解析器,帮助纠正HTML语法错误'''
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags 
'''在HTML中标签<a></a> 或者大写字母A 。 其中的a（或者A） 是anchor 的缩写。
这些标签的作用是标明超连接的起始位置或目的位置。'''
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
