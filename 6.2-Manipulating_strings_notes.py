fruit = 'banana'
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1
    #colon operater

#string concatenation
a = 'Hello'
b = 'There'
c = a + ' ' + 'There'
print(c)

'''大写字母Z小于小写字母a的
假如一个字符串是Chuck
以大写字母C开头 另一个字符串是Glenn 以大写字母G开头 其他地方都是小写
那么它俩就会被正确的排序 因为所有的大写字母都被和大写字母比较 而小写字母被和小写字母比较
但如果字符串变为chuck和Gleen 这两个字符串就会被用错误的方式排序 因为G将会被放在c前面(G比c小)
这没啥问题 或许也说得通 这些规则是前后一致的 虽然你确实可以这么做 不过毫无疑问==操作符给出的结果是最合理的
这些就是我们可以进行的一些基本运算
'''

'''字符串操作的其中之一是
 你可以用greet.lower() 这就像是 像是调用了一个叫做lower()的函数 然后把greet传递给它
 但这是一种略有不同的语法
 这的意思是 调用属于字符串对象的一个函数lower() 这是字符串类的一部分 它会返回一个小写的该字符串 从功能上解释这一行代码
 它会创建一个greet的复制 将其转化为小写并返回 然后我们将这个值赋给变量zap
 假如我们将其打印出 你会发现字母都是小写的
 然后如果我们查看一下greet的值是什么 你会发现greet的值并没有变
 因为这个函数做的是创建一个小写的复制 所以它不会改变原来的字符串
 其实甚至常量也是一个合法的对象 因此它也包含了lower这个方法 所以这会输出"Hi There"的小写版 对我们展示出所有字母的小写
 即使是常量也有这种内置的功能 当我们讲到这的时候 你可以自己查阅一下 看一下对象的方法 这个东西就是一个方法'''
print('HI THERE', lower())

#what methods are python
#https://www.analyticsvidhya.com/blog/2020/11/basic-concepts-object-oriented-programming-types-methods-python/

#用dir查string能干什么
string = 'hello'
dir(string)
#balbal.find('balball')如果没有就输出-1
很多内置函数都只会返回复制信息
#lstrip()把左边空格取消rsreip()同理
text = "X-DSPAM-Confidence:    0.8475"
step1 = text.find(':')
step2 = text[step1+1 : ]

'''用 Python 中 list 的相关函数求解
方法一：
解题关键主要是想找到 num2 = target - num1，是否也在 list 中，那么就需要运用以下两个方法：

num2 in nums，返回 True 说明有戏
nums.index(num2)，查找 num2 的索引

作者：lao-la-rou-yue-jiao-yue-xiang
链接：https://leetcode-cn.com/problems/two-sum/solution/xiao-bai-pythonji-chong-jie-fa-by-lao-la-rou-yue-j/
'''
def twoSum(nums, target):
    lens = len(nums)
    j=-1
    for i in range(lens):
        if (target - nums[i]) in nums:
            if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                continue
            else:
                j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2
                break
    if j>0:
        return [i,j]
    else:
        return []
