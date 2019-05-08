import pymysql
db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')

# 创建数据库
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# cursor.execute("CREATE DATABASE spiders CHARACTER SET utf8")
# print('Database version:', data)

# 创建表
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL , PRIMARY KEY(id))'

id = '20120001'
user = 'Bob'
age = 20

cursor = db.cursor()
sql = 'INSERT INTO students(id,name,age) values(%s, %s, %s)'
try:
	cursor.execute(sql,(id,user,age))
	db.commit()
except:
	db.rollback()
db.close()