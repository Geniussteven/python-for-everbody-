#15.1 Relational Databases
#以连接为模型的概念是使数据库快速发展的基础数学
'''column列， row行
schema就是类似于表格有关标题那第一行，后面每一行必须要是整数，字符串不超过128个字符。
首先我们会建立一个database application（DB又称为API） ，它可以理解复杂的数据，
然后我们的code借用这个和复杂的database进行沟通。这个过程称之为abstraction抽象。
我们用SQL(Structured Query Language)和DB沟通。'''
SQL四个基础函数
CRUD-create a table、retrieve some data、insert data、delete data

#15.2 - Using Databases
首先
我们要建立表格放数据进去。做的是DBA的工作
在SQLite browser里输入内容
然后
我们要编写python程序和数据库沟通
input files 然后经过程序清理，存储到database
然后编写另一个程序读取数据，然后output（eg.R数据分析、D3.js）
总之，读取数据，清 理数据，并以合理和有组织的方式将其粘贴在数据库中。 然后编写其他应用程序来理解它并分析数据。

#databases model
'''数据模型不仅仅是查询它的 SQL，而是我们要在数据库中存储和检索内容的形状的合同。
SQLite 就是所谓的嵌入式数据库。MySQL 或 Oracle 是一整套独立的软件 ，我们通过网络连接讨论。 但 SQLite 实际上是软件的一部分，所以它是python内置的.
它的速度很快，并针对更少量的数据
导入语句：import statement'''

#建立table
CREATE TABLE users(
	name VARCHAR(128),
	email VARCHAR(128)
)
以上代码实际上就是一个有关最大字符数和名称的协议。
#insert 
INSERT INTO users (name, email) VALUES ('Kristin', 'kr@umich.edu') 
#DELETE
DELETE FROM users WHERE email='kr@umich.edu'
#update 更新允许我们进入表格中的特定单元格或单元格集，许多行或多列或多行/列组合。
UPDATE users SET name='Charles' WHERE email= 'kr@umich.edu'
#Retrieving
SELECT*FROM users'''SELECT接受一个列表，这是一个列表。
*意味着所有的列,名为 Users 的数据库中的所有行、列'''
'''SELECT*FROM users WHERE 某一行（或者每一个有这个语句的行）
SELECT COUNT(*) FROM Users
the user wants to know the total number of rows in the orders table. 
So the user calls the COUNT(*) function in a SELECT statement without a WHERE clause: 
SELECT COUNT(*) AS total_rows FROM orders'''
#sorting with order by
SELECT*FROM users ORDER BY email
'''排序是数据库做得非常好的事情之一。'''
DROP TABLE IF EXISTS Counts '''删除数据库中的表,如果表存在，则阻止一个全新的数据库'''

#emaildb.py example
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()'''这个cursor很像我们的handle 
它不像你只是open()read()那么简单 
但你打开它然后发送SQL命令。这个cursor，然后你拿到你的回答通过那同样的cursor 
因此这里的cur是我们感兴趣的这个变量 
首先我们要做的是，拿这个文件，这两行代码将帮助我们创建该文件，
目前该文件不存在，它将被创建在与emaildb.py相同的目录中'''

cur.execute('DROP TABLE IF EXISTS Counts')'''删除数据库中的表,如果表存在，则阻止一个全新的数据库'''

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')
'''我们在这里做的就是 我们可以把它(上一行括号内)看成是一个字典。 
如果你还记得我们介绍字典的时候， 字典就像是一个内存中的数据库。 
好吧，现在看起来我们是要用这个“数据库”来 创建另一个数据库'''

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))'''? is a placeholder.
    为了防止sql注入injection https://zh.wikipedia.org/zh-tw/SQL%E6%B3%A8%E5%85%A5
    这个cur.execute实际上没有真正检索这个数据 
    在某种程序上，它是在看着这个SQL并确保它或许验证那个表名是正确的或如果这里有任何语法错误，
    因此，这实际上没有真正读取这个数据
    '''
    row = cur.fetchone()'''抓取这个第一个然后把它放回在行里，然后行将成为这个我们从数据库里拿到的信息'''
    if row is None:#类似get语句
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))#使用update语句好过读取值然后增加value
    conn.commit()'''它的基本工作方式是 
    这个数据库是有效的保持了一些在内存中的信息，在某点上 必须写所有的资料出来到磁盘上 
    因此你可以选择提交地方的次数，现在 我们要通过这个循环每次提交，但你或许通过循环每10次提交，
    因为这个提交会花 一些时间，因为它命令所有都要写进磁盘'''

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()



The program can be speeded up greatly by moving the commit operation outside of the loop. 
In any database program, 
there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.
通过将提交操作移到循环之外，可以大大加快程序的速度。
在任何数据库程序中，你在提交之间执行的操作数量与不丢失尚未提交的操作结果的重要性之间存在着一种平衡。

Ai 是指自动增加，命名为文本域text field
