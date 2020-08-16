import pymysql

password = 'pcy2674467254'

# db = pymysql.connect(host = 'localhost', user = 'root', password = password, port = 3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

# db = pymysql.connect(host = 'localhost', user = 'root', password = password, port = 3306, db = 'spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()

db = pymysql.connect(host = 'localhost', user = 'root', password = password, port = 3306, db = 'spiders')
cursor = db.cursor()
db.close()
