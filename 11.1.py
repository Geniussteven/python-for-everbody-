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
  
