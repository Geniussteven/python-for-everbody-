'''Regular Expressions
caret character‘^’
if line.find('From: ') >= 0 :
等同于
import re 引入这个功能
然后if re.rearch('From: ', line) : '''
更多笔记：
https://www.notion.so/f3f75ef747934f1da4f9b36771fc0f49
re.search()返回对与错根据字符串时候match正则表达式
re.findall() 让matched string to be extracted print出字符串组
Greedy Matching
import re
x = '一串含数字的字符串'
y = re.findall('[0-9]+', x)
greedy matching prefer longest eg ^A.+:
Non-greedy Matching 倾向于shortest  ^A.+?:
  Assignment 11.1
  import re
fname = input("Enter file:")
handle = open(fname)
list = ()
y = re.findall('[0-9]+', handle)
#此时的y是lists of strings
for line in handle ：
  i = float(y[0])
  y = y[0:  ]
  x  = sum(i)
other method
1st:
import re#use the 推导式comprehensions
print(sum([int(i) for i in (re.findall('[0-9]+',(open('filename.txt','r').read())))]))
2nd
import re 
hand = open("regex_sum_24962.txt")
x=list()
for line in hand :
    y = re.findall('[0-9]+', line)
    x = x + y
sum = 0
for z in x :
    sum = sum + int(z)
print(sum)

3rd
import re 
hand = open("regex_sum_24962.txt")
x = []
for line in hand :
    num = line.rstrip()
    numbers  = re.findall('[0-9]+', line)
for number in numbers
    if number != ''：
    lst.append(int(number))
print(sum(x))

'''for num in x:
    num_list.append(int(num))'''也可以
