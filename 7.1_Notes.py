7.1
#之前我们一直讨论存在main memory里的变量和CPU之间的联系（主存储存储，CPU反馈），还有从用户那读取，回到主存储，然后输出。
#现在我们要讨论二级存储（又称permanent memory），files一般存在二级存储里，针对由语句行组成的纯文本文件flat txt filesd（eg.邮箱文件导出的平面文件，方便检索等操作)
#print语句自带一个\n, 实际换行都会又产生一个\n(例如提取邮件某段文字需要考虑用rstrip消除间隔)
xfile = open('mbox.txt')
#用open函数建立一个方便读取平面文本文件的handle，而并非数据本身。文件名和处理方式（r/w）用，隔开。
for cheese in xfile:
    print(cheese)
#len(\n) = 1、
#用read()函数从别处读取所有文件
最重要的三行代码
fhand = open('mailbox.txt')
for line in fhand:
    line = line.rstrip()

if not line.startwith('From:')
    continue
priny(line)
'''Assignment 7.1
Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt'''
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
try:
    fh = fh.read()
except:
    print('Invalid file name: ')
    quit()
fh = fh.rstrip()
print(fh.upper())

'''Assignment 7.2
rite a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt'''

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    number= float(line[line.find("0"):])
    count = count + 1
    total = total + number
print("Average spam confidence:",total/count)

'''kipping with continue
如果代码量非常大，最好是跳过不好的语句，专注于好的。用 if not 来“判定'''
fhand = open('words.txt')
for line in fhand:
    line  = line.rs()
    if not line.startwith('From:') :continue
    print(line)

















1txt = open('1.txt')
count = 0
for line in 1txt ：
    count  = count + 1
print（‘The numbles of the lines are’, count）
