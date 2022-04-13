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


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
Answer:
mysock.connect()
