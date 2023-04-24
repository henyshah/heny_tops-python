# database:database means collection of tables.
# which contains multiple items


# need to install xampp server mysql
# after the installation of xampp server need to start apache and mysql
# to install pymsql: pip install pymysql

import pymysql

# connection with the server
mydb=pymysql.connect(host="localhost",user="root",password="",database="mydb_tops")
mycursor=mydb.cursor()

# need to create database
mycursor.execute("create database IF NOT EXISTS mydb_tops")
mydb.commit()

# cnnection with database
mydb=pymysql.connect(host="localhost",user="root",password="",database="mydb_tops")

# table creation
mycursor.execute("create table if not exists student (id int primary key auto_increment,name varchar(20),subject varchar(20))")

mydb.commit()

# import pymysql

# # connection with the server
# mydb=pymysql.connect(host="localhost",user="root",password="",database="mydb_tops")
# mycursor=mydb.cursor()

# # need to create database
# mycursor.execute("create database IF NOT EXISTS mydb_tops")
# mydb.commit()

# # cnnection with database
# mydb=pymysql.connect(host="localhost",user="root",password="",database="mydb_tops")

# # table creation
# mycursor.execute("create table if not exists book (id int primary key auto_increment,name varchar(20),publisher varchar(20),pages varchar(20),price varchar(20),available varchar(20))")

# mydb.commit()