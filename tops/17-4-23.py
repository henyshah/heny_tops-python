# python crud database
# # database:database means collection of tables.
# # which contains multiple items


# # need to install xampp server mysql
# # after the installation of xampp server need to start apache and mysql
# # to install pymsql: pip install pymysql

# import pymysql

# # connection with the server
# mydb=pymysql.connect(host="localhost",user="root",password="")
# mycursor=mydb.cursor()

# # need to create database
# mycursor.execute("create database IF NOT EXISTS mydb_tops")
# mydb.commit()

# # cnnection with database
# mydb=pymysql.connect(host="localhost",user="root",password="",database="mydb_tops")

# # table creation
# mycursor.execute("create table if not exists sudent (id int primary key auto_increment,name varchar(20),subject varchar(20))")

# mydb.commit()




# # importing connecting file 
# import connection
# import pymysql

# # connection with database
# mydb=pymysql.connect(host="localhost",user="root",password="",database="mydb_tops")
# mycursor=mydb.cursor()

# status=True
# while status:
#     data="""
#                   MENU
#                 1) store data
#                 2) view data
#                 3) update data
#                 4) search data
#                 5) delete data
#     """
#     print(data)
#     choice=int(input("enter your choice: "))
#     if choice==1:

#         # to insert data
#         name="enter your name"
#         subject="enter your subject"
        
#         # query
#         query="insert into student (name,subject) values('%s,%s)"

#         args=(subject % query)

#         mycursor.execute(query % args)

#         # to save changes
#         mydb.commit()
#         print("succesfully data inserted")
     
#     loop_choice=input("do you want to perform more operations press 'y' for yes and press 'n' for no: ")
#     if loop_choice=='n' or loop_choice=='no':
#         status=False
