#5.1 notes
repeating steps 用while
So that was like a residual value of this little variable n after the last iteration（迭代） through the loop.
And that's because it was 1 and then we subtracted（减） 1 from it. And that got us to 0.
无限循环infinite loop

while True:
        line = input('> ')
        if line[0] == '#':
            continue
        if line =='done':
            break
        print(line)
print('Done!')
#definite loop定循环
#integer iteration variabies
#synax
for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')
#5.3 loop idioms
#Assignment 5.1
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "Done" :
        break
    try :
        newnum = int(num)
     if largest is None or largest < newnum : 
         largest = newnum 
     elif smallest is None or newnum < smallest :
         smallest = newnum 
    except :
        print('Invalid input')
        continue
print('Maximum is', largest)
print('Minimum is', smallest)
#两个错误，1. if largest is None，弄错赋值None对象。2.用or连结相同语句，两个if elif 也可以用。
#filtering过滤 in a loop
#Boolean is a kind of variable that either has the value True or False,
#is 比 = =更强烈表达两者完全相等 You shouldn't use is when you should be using double equals, 
#usually you're using them for a True, False, or None. So that we don't overuse is, because is,
#is a really, really strong equality. So it's a stronger equality than double equals to,
#so the double equals is mathematically equal to with potential conversion.
#smallest = None(flag value)
