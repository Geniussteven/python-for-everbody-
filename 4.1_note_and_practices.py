#函数是储存和调用的载体
#函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()，thing（）-调用函数
def thing():#def后接上定义函数eg:print_balbal
    Print('hello')#这两个print像是变量被存储在thing（）
    Print('fun')
#以上是代码块，取消缩进后一个函数被定义，截止这什么都不执行。
thing()#call/invoking调用函数
Print('zip')
thing()
#output-hello.fun.zip.hello.fun

# lang这个变量最好把它当做一个别名 它是这个函数被调用时 任何第一个参数的别名
#现在我们3次调用这个函数 我们分别在括号中放入3个不同的值 这是一种通过传递不同的参数让代码在很大部分看起来相同 但是让他们有一点点不一样的方式 因为我们放进了不同的参数，所以代码的行为略有不同
#所以实际上这只是一个告知第一个参数是什么的占位符
#我们作为函数的编写者 可以通过return语句 (return statement)决定返回值 (residual value)
#所以基本上，尽管这是一个 连参数都没有的简单函数，return语句做了两件事： 第一，它终止了这个函数 并且它跳转到下一行代码 第二，它也决定了返回值 (residual value)
# you can have more than one parameter as you might well expect
def addtwo(a, b):
    add = a + b
    return add

x = addtwo(3, 5)
print(x)
#parameter是函数定义中括号内列出的变量。argument是在调用函数时发送到函数的值。
#some functions do not return values. We call them non-fruitful functions
#and if they return values then we call them fruitful functions.
#4.6 Assignment
def computepay(h, r):
    if h < 40 :
    	return h*r
    elif h >40 :
    	return 40*r+(h-40)*r*1.5

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rates:")
r = float(rate)
p = computepay(h, r)
print("Pay", p)
