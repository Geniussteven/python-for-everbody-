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
9 in some
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
这段代码不管我们要计算多少数字的平均数 仅仅会使用两个变量
而这段代码计算多少数字 就需要多少额外的内存空间'''
选校工具
https://offer.1point3acres.com/db/programs/CS-MS-
https://docs.python.org/3/library/stdtypes.html#range
