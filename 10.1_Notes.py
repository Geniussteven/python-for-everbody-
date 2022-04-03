10.1 Tuples
'''limited版本的list,不可修改（immutable）使它比列表更密集的存储。
元组的输出是列表的子集。list可变需要分配更多的内存，tuples不可变使更高效
Given that Python lists and Python tuples are quite similar - when might you prefer to use a tuple over a list?
For a temporary variable that you will use and discard without modifying
eg.A = (1, 2, 3)'''

'''两个内置函数
count（）计算某一特定值的元素数量
index（）'''

#元组特性
'''将左边的元组里的值、返回元组的函数、expression表达式双重赋值给右边。左右必须同时是元组
convert from dict to tuples用items()'''
d = dict()
d['a'] = 1
d['b'] = 2
for (k, v) in d.items() :
    print(k, v)

#Tuples are comparable
从左往右比较，直到比出结果（T/F）

'''Sort by key
d = 一个{}
d.items()得到一个tuple
sorted(d.items())得到按key排序的list'''
'''Sort by value instead of key
Key-value tuple ->Value-Key tuples'''




'''Assignment 10.2
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in name :
    line.statswith('From ').split()
    for emails in line[5] :
        counts[emails] = counts.get(eamils, 0) + 1
lst = list()
for key, val in count.items() :
    newtup = (val, key)
    1st
