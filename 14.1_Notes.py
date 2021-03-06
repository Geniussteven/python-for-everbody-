#面向对象编程
'''这节课更多教我们它是怎么实现的，更少提及我们应该怎么使用它。
obiects 例如list、dic可以看作更小单位的program，也有其逻辑和内置功能
程序外内就是使用者使用见到的和程序员写的代码'''

'''class类 -对象的形状，Python是一种面向对象的编程语言。
Python中几乎所有东西都是对象，包括它的属性和方法。
类类似于对象构造函数，或创建对象的“蓝图”。
例如很多string 有命名为x、y、z的，所有的string统称为class'''

'''method/MESSAGE-方法：类中定义的函数，方法是定义类的一部分，它也是对象的一部分。
这就是像string.upper、string.startwith、string.find这样的东西，这些都是字符串类中的方法。
但它们也是每个字符串对象的一部分。
MESSAGE意思是说，这里有这个对象，你要给它发送一个消息，使它做一些事情，
你会用这个消息来戳它一下。
但另一种说法是，它里面有代码，我们在对象里面调用一个函数，它们有点等同'''

'''Field/attribute-'''

'''instance-在运行时间内真实存在的对象'''
'''定义class就是先制造一个template,然后存储在一个变量里，然后call
an.party()类似于进入PartyAnimal。在其中调用party()函数，然后把这个变量作为第一个参数传给它
invoking唤起 the objects'''
'''回去试着用dir（）测试封装好的class'''
'''现在我们要讲的是物体是如何建造和丢弃的。这也是一直在发生的事情。
大多数时候，我们构建变量时，你说x = hello world，这就构成了一个对象。
当程序结束时，所有的变量都被丢弃了。有时候你可以更直白一点。
我们有专门的术语来描述它，我们称它为构造函数或构造，取模板，然后构建它。这是构建过程，然后把它扔掉，
让内存供程序的其他部分使用，这就是毁灭的时刻。如果你说x等于hello world，你就构造了一个字符串并把它放到x中。
如果你说x等于12，你构造了12并把它放到x中，但你也抛弃了之前在那里的hello world。
因此，析构函数是在我们重用变量或程序结束时发生的。
当对象变得更复杂时，构造函数的主要目的是设置初始值。'''

'''开始定义一个class
先定义这个class制作一个模板，然后将这个模板赋给变量an()an是举例
an.party()就是call it'''


案例 party5.py 再思考一下知道想明白为止。
class PartyAnimal:
   x = 0
   name = ''
   def __init__(self, nam):
     self.name = nam
     print(self.name,'constructed')

   def party(self) :
     self.x = self.x + 1
     print(self.name,'party count',self.x)

s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()'''注意这是两个x，两个名字，它们是独立存储在每个对象中的。
所以这是两个独立的instances实例，这里的关键是实例instances。
这是因为我们建造了两个PartyAnimals，然后把它们放在不同的变量中。
所以同时，它们中的每一个都有它们需要的所有内部结构'''

'''上面的这并不是一个非常有用的例子。
如果有一堆字符串，一个在x，一个在line，一个在z，一个在this，一个在name，一个在email，
它们都是字符串，里面有数据。
因此，这些变量名称是指向拥有所有数据的对象的。

#菜鸟编程例子 https://www.runoob.com/python3/python3-class.html
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'
 
# 实例化类
x = MyClass()
 
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())
#类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。

#self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# 实例化类
p = people('runoob',10,30)
p.speak()

'''静态方法: 用 @staticmethod 装饰的不带 self 参数的方法叫做静态方法，类的静态方法可以没有参数，可以直接使用类名调用。

普通方法: 默认有个self参数，且只能被对象调用。

类方法: 默认有个 cls 参数，可以被类和对象调用，需要加上 @classmethod 装饰器。'''
#一段程序作为主线运行程序时其内置名称就是 __main__.
#类的专有方法中，也是存在默认优先级的，多个方法都有返回值，但一般优先取 __str__() 的返回值.
#定义类时，若需要输入参数，则一般必须使用 __init__()方法；若不需要输入参数，是否使用 __init__() 方法都可以。
接下来，我们将讨论另一种定义对象能力的方法，即继承inheritance。'''
'''是对父class attribute和method的继承，再加上新的属性方法。
面向对象，因为它是一种将功能分组的方式'''
