#网络体系结构network architecture
transport control protocol (TCP)
IP Internet protocol
transport to transport 端对端
socket套接字（两台电脑间接受传输的接口）
listen ports侦听端口
TCPIP接口
80是web网页（HTTP）常用接口；443端口

想要实现互联基础代码如下
import socket#引入库
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))#前面是域名host，后面是端口port
#这里的语法, 我不想解释。 只要按照我告诉你的方式输入这个。
作用大体是在你的计算机内部 创建了一个准备好去连接外界的端口
不过目前还未链接 就像是一个还没连接上的 连接点，
stream数据流指的是一连串不停地出现的字符

12.2Hypertext Transfer Protocol (HTTP)超文本传输协议protocol
是互联网上的dominant application layer主要应用层
为了browser 浏览器retrieve webpage检索网页诞生inception
eg. https://www.coursera.org/learn/python-network-data/

点击-识别当前页面的HTML-识别要到哪个服务器的哪个端口-要检索哪个文档
浏览器建立到端口的套接字连接，并发送名为get的请求到端口
然后进入web服务器解析请求找出正在寻找的文档
以HTML（HyperText Markup Language）的形式发回响应
Metadata元数据 然后text
序列控制檯Console
接着11-13行的代码
输入cmd（一些get请求）然后send
然后while循环直到没有数据，然后解码decode，最后关闭建立的socket


encode and decode
encode将Unicode string转化为bytes utf-8 第31行的cmd实际上就是bytes（编码后）
发送给sockets然后，它接收，并decode
一些有意思的python网址
https://dash.gallery/Portal/
https://plotly.com/python/
https://www.panda3d.org/
https://www.opengl.org/
https://unity.com/
https://threejs.org/
https://www.kaggle.com/
  
  Using URL lib in python
  将我们之前request get等操作存在lib里
  send into a library
  整体操作 import library
  通过几个函数（request,open）返回一个object例如视频里的fhand
