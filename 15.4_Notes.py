#Designing a Data Model
'''设计图涉及不同的表中列和不同表之间的联结。
相同字符串数据不要用两次，用关系来代替，可以建立新的表格。
应用程序的一个句子描述。应用程序要查找的数据 我们已经得到了所有这些列
第一步-找到不同元素之间的逻辑关系
第二步-映射到一个数据库map this into a database'''

15.5 - Representing a Data Model in Tables
'''建立物理模型，primary key 主键是一种方法 为我们指一个特定的行，因此它是个唯一的数字像1 2 3 4。
例如专辑从属于track，不同的专辑会有不同的数字代表。
And then we use that number in a column of a different table to sort of point to it.'''
箭头起点是新增加的列（例如album_id,它是Foreign key），终点是primary key。
logical key 从外界查找该行唯一的东西。
可以在where子句里用它。
简单可读性强的命名约定非常重要。
命名新的域及类型（TEXT or integer），然后定义非空，是主键。一旦连接到这张表就会大量使用它
'''现在的想法是我们趋向从外向里工作 
新建表里先是主键，后加上备注长语句 整数 不为空 主键 自动增量
然后是逻辑键
AI（自动递增）是自动指定，命名为文本域text field
'''
#15.6  Inserting Relational Data
插入
加；可以连续运行多次，执行相同命令。

#Inserting Relational Data
使用ON子句 以使我不混淆我的WHERE子句
目的是减少扫描才能获取信息的数据量
本节：如何插入数据，将事物连接到一起，建立关系和连接点的模型，而不是复制数字。

15.7 reconstructing Data with JOIN
JOIN - 从多个表里选取数据
重要部分是ON语句，用来连接一行和一个表与不同表中相应的行。
eg. select 两个不同表中的列 from 表一 JOIN 表二 on 箭头起点外键= 箭头终点外键
