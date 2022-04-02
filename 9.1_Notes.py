#“字典”是我们的第二个数据结构，我们的第二种数据集(collection)另一种是list
'''dictionary不像list那样有序。
Python lists are indexed using integers and dictionaries can use strings as indexes
你把数据放进去，并相应地贴上标签，再取出数据
数据不会保持原来的顺序， 顺序常常会变
但是 “字典”却非常强大 因为里面的数据存在形式都是关键字组
你为每个数据赋予一个关键字 使用关键字值存入数据 并且使用该关键字来提取相应数据'''

'''关键字是一个通用的概念 在其他编程语言中它也被称为辅助数列(associative array) java称之为Hashmap
你也可以去搜索了解一下关联数组(associative array)
在大多数语言中 比如Perl和PHP, 关联数组是 再说一次 大部分人最喜欢的数据结构
因为它可以协助人们完成很多事情 所以“字典”就是python最强大的集合
它就像一个小型的数据库 拥有关键字-数据组合，你通过关键字查询信息'''
#construct a dict()
purse = dict()
purse['a'] = 1#用 index operator append value。
#可以修改value
purse['a'] = purse['a'] + 1
print(purse)
{'a': 2}
#你也可以直接建立一个dict,不过打印后顺序会混乱。
'''可以用 in 询问某个key是否在dict中，会回答T/F.
如果试图去抓取不存在的key，就会Traceback Error'''

#The 'get' Mrthod for Dictionaries
x = counts.get(name, 0)
'''以name在counts这个字典里搜索，找到key对应的值并返回。
0是默认值，如果没有找到就会返回默认值给x。'''
#counting with get()
'''目标是遍历list找到dict里已有的计数加1，新的添加新的key，value设为1'''
第一种方法是用if-else
if name in names :
    count[name] = 1
else :
    count[name] = count[name] + 1
第二种用get()
counts[name] = counts.get(name, 0) + 1

'''looking through the dict()
for key in counts.是遍历key
print(key, counts[key]'''
maps to 映射到

'''retrieving lists of keys and values
aaa = {'a' : 3 , 'b' : 2 , 'c' : 1}
print(list(aaa))
['a', 'b', 'c']#不含value
print(aaa.key())
['a', 'b', 'c']
print(aaa.value())
[3, 2, 1]

print(aaa.items())
[('a' : 3) , ('b' : 2) , ('c' : 1)]#单个括号内的就是tuple

loop iteration variables 设为key-value格式

#ssignment 9.4
'''Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle :
    if not line.startswith('From ') :continue
    emails = line.split()
    for name in emails[2] :
        counts[name] = counts.get('name', 0) + 1

most_prolific_committer = None
frequency = None
for word,count in counts.items() :
    if frequency is None or count > frequency :
    	frequency = count
    	most_prolific_committer = word
print(most_prolific_committer, frequency)


几种正确解法
fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"
hand = open(fname)

lst = list()

for line in hand:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])

counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = {}
for line in handle:
    word = line.split()
    if len(word) < 3 or word[0] != "From" : continue #效果和  if not line.startswith("From:"): continue等同。
    email = word[1]
    if email in counts :
        counts[email] = 1 + counts[email]
    else :
        counts.update({email:1}) #Python 字典(Dictionary) update() 函数把字典 dict2 的键/值对更新到 dict 里。
max = 0
value = ""
for i in counts:
    if (counts[i]) > max :
        max = counts[i]
        value = i
print(value, max)

fname = input("Enter the file name: ")
fhandle = open(fname)
dic = dict()

for lines in fhandle:
    words = lines.rstrip().split()

    if 'From' in words and'From:' not in words:
        mails = words[1]
        dic[mails] = dic.get(mails, 0) + 1
    else:
        continue

frequency = 0
email = None
for k,v in dic.items():
    if v > frequency:
        frequency = v
        email = k
print(email, frequency)

name = "mbox-short.txt"
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lst = list()
mail_names = list()
counts = dict()
qew= ""

for line in handle:
    lst = line.rstrip().split()
    if 'From' in lst:
        mail_names.append(lst[1])


for name in mail_names:
    counts[name] = counts.get(name, 0) + 1

max_name_as_list = [key for key, value in counts.items() if value == max(counts.values())]
max_name = qew.join(max_name_as_list)#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
'''str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq );
consequence a-b-c'''

print(max_name ,max(counts.values()))
'''data mining 数据挖掘
Databases
Webpages with Django
PHP
