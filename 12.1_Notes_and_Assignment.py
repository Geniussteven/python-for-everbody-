#网络体系结构network architecture
transport control protocol (TCP)
IP Internet protocol
transport to transport 端对端
socket套接字（两台电脑间接受传输的接口）
listen ports侦听端口
TCPIP接口
Client客户端
80是web网页（HTTP）常用接口；443端口
what is an important aspect of an Application Layer protocol like HTTP?
Which Application talks first? The client or server?
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
  
  P69 b站视频 https://www.bilibili.com/video/BV16b411n7U4?p=49
  URL(Uniform Resource Locator) 
  Using URL lib in python
  将我们之前request get等操作存在lib里
  send into a library
  整体操作 import library
  通过几个函数（request,open）返回一个object例如视频里的fhand
如果你上了这个课的时间足够长， 
你知道这个数字是什么，这将是正确的答案， 
因为它总是正确的答案。 所以，我想告诉你在 URL 上放置参数的想法。 
所以，我可以把一个参数，猜测等于 12。 所以，我放了一个问号 ，你会看到 URL。 
如果您使用的是 Google 地图或其他任何东西，您将看到这些问号。 
这些参数除了 URL 之外还会继续进行。 所以，这里我们有 URL 是这样的， 
然后有外围被发送到 服务器上的这个交互式应用程序。 所以，如果我们看看发生了什么，
我 们做一个 get 请求， 如果我查看标题， 它发送到整个 URL， 文档要检索。 
问号猜测等于 1， 问号后面的 Web 应用程序， 请参阅这些参数的键值对。 
它来像一个小字典。 所以，如果我们看看这里， 那就是 URL， 
我们做了一个获取请求， 这是我们连接到的 IP 地址，有一个 200， 响应标头，我们看到它是内容类型的文本 HTML。 
请求标头再次， 这些是我们发送的。 
有一个路径和方案以及所有其他东西， 然后有查询字符串参数。
cache-control 缓存控制
302表示我给你的是一个location header
header中的metadata告诉浏览器如何在响应文档返回时解释它的正文
text/plain文本平面 text/html
