'''Lists
#算法就像是代码的GPS导航 而数据结构是结构化的变量 。
strings are immmutable, Lists are mutable.'''
len()、range()、append()
#counting loop
a = ['1', '2', '3']
for i in range(len(a))
    friend = a[i]
    print()

#building a list
stuff = list()#list()是预设定义类型，这一步类似于建立一个空list然后assign给stuff
stuff.append('apple')#如果x = x.append会返回值破坏x
print(stuff)
#Is something in a list.
some  = ('a', 'b', 'c')
a in some
#True(会返回这个值)

#sort（）按字母顺序排列
#1st way.
num = 0
count = 0
    while True :
        inp = input('')
        if inp =='done' : break
        value = float(inp)
        num = value + num
        count = count + 1
average = num / count
#2rd way. Using a data structure rather than just a logic
numlist = list()
    while True :
        inp = input('')
        if inp =='done' : break
        value = float(inp)
        numlist.append(value)

average = sum(numlist) / len(numlist)
print()
'''这两者之间只有一个微小的差异
那就是在上面这种方法sum(),实际做计算之前 这一个会把所有的数字都存在内存中
而另外一个只在内存中保存了一个数字
这也许并不重要 如果只有十万或者更小数字的话 但是假设有一亿个数字 那么这一个不会用到 内存中的一亿个空间 而这一个确实会用到一亿个空间
所以如果数据够大的话 这个区别就很重要了
这两段程序占用的内存区别很大 因为这段代码只需要用到两个变量<br />(占用两个float类型的空间，其实二者都是2个变量)
1st代码不管我们要计算多少数字的平均数 仅仅会使用两个变量
而2rd代码计算多少数字 就需要多少额外的内存空间'''
选校工具
https://offer.1point3acres.com/db/programs/CS-MS-
https://docs.python.org/3/library/stdtypes.html#range
'''函数splict() 默认按空格分割，多个空格亦可，分割出[]'''
line = ('1;2;3')
i = line.splict()
print(len(i))
#也可以根据符号分割
thing = line.splict(';')
print(len(thing))

#The double splict pattern
#Assignment 1
'''Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method. 
The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt'''
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
   words = line.rstrip().split()
   for word in words:
        if word in lst:#也可以这样写 if word not in lst
            continue#1st.append(word)
        else :
            lst.append(word)
lst.sort()
print(lst)

#Assignment 2
'''Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. 
Also look at the last line of the sample output to see how to print the count.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt'''
fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh :
    line = line.rstrip()
    if not line.startswith('From ') :continue
    a = line.split()
    print(a[1])
    count = count + 1  
print("There were", count, "lines in the file with From as the first word")
