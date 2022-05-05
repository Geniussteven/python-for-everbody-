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
