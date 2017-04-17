# -*- coding: utf-8 -*-

import MySQLdb as msql
#感悟：1.首先要连接，然后用query来执行表外操作，用execute来执行表内操作。
#2.fetchall能用来接收选到的文本，并且用python来操作。
#3.注意，由于建表操作会检验表是否存在，因此，程序只能运行一次。后续运行需要改动两处text(i)到text(i+1).

#登录数据库
cxn = msql.connect(user='root',passwd='password')

#建立数据库
cxn.query('CREATE DATABASE text6')
#授权所有人能用？
#cxn.query("GRANT ALL ON text4.* to ''@'localhost'")
#事务处理，只有提交后才能生效
cxn.commit()
cxn.close()

#重新登录
cxn=msql.connect(db='text6',user='root',passwd='password')

#建立表格users，并加入数据
#利用游标
cur=cxn.cursor()
cur.execute('CREATE TABLE users (login VARCHAR(8),userid INT)')
cur.execute("INSERT INTO users VALUES('john',7000)")
cur.execute("INSERT INTO users VALUES('jane',7001)")
cur.execute("INSERT INTO users VALUES('bob',7200)")
cur.execute("SELECT * FROM users WHERE login LIKE 'j%'")

#用python语言做更多操作
for data in cur.fetchall():
    print '%s\t%s' % data

#update操作
cur.execute("UPDATE users SET userid=7100 WHERE userid=7001")
cur.execute("SELECT * FROM users")
print"_____________________"

for data in cur.fetchall():
    print '%s\t%s' % data
	
cur.close()
cxn.commit()
cxn.close()

