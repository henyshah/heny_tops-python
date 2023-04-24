# importing connecting file 
import connection
import pymysql

# connection with database
mydb=pymysql.connect(host="localhost",user="root",password="",database="mydb_tops")
mycursor=mydb.cursor()

status=True
while status:
    data="""
                  MENU
                1) store data
                2) view data
                3) update data
                4) search data
                5) delete data
    """
    print(data)
    choice=int(input("enter your choice: "))
    if choice==1:

        # to insert data
        id=int(input("enter id: "))
        name=input("enter your name: ")
        subject=input("enter your subject: ")
        
        # query
        query="insert into student (name,subject) values ('%s','%s')"

        args=(name,subject)

        mycursor.execute(query % args)

        # to save changes
        mydb.commit()
        print("succesfully data inserted")

    elif choice==2:
        # to fetch all data from table
        query="select * from sudent"

        # execute query
        mycursor.execute(query)

        # to fetch all data from query
        data=mycursor.fetchall()

        print(data)

    elif choice==3:
        # update data
        id=int(input("enter id: "))
        name=input("enter name: ")
        subject=input("enter subject: ")

        # query
        query="update student set name='%s',subject='%s' where id=%s"
        args=(name,subject,id)

        # execute query
        mycursor.execute(query%args)
        mydb.commit()

        print("updated successfully")

    elif choice==4:
        # search data
        id=int(input("enter id: "))

        # query
        query="select*from students where id=%s"

        # args
        args=(id)

        mycursor.execute(query%args)

        # retrieve all data in row variable
        row=mycursor.fetchone()

        # id=0 name=1 subject=2
        displayname=row[1]
        displaysubject=row[2]

        print("name= ",displayname)
        print("subject= ",displaysubject)

    elif choice==5:
        # delete data
        id=int(input("enter id: "))

        # query
        query="delete from student where id= %s"

        # args
        args(id)

        mycursor.execute(query%args)
        mydb.commit()
        print("deleted successfully")

    loop_choice=input("do you want to perform more operations press 'y' for yes and press 'n' for no: ")
    if loop_choice=='n' or loop_choice=='no':
        status=False


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
#         name=input("enter book name: ")
#         publisher=input("enter your publisher name: ")
#         pages=int(input("enter pages: "))
#         price=int(input("enter price: "))
#         available=input("is it availbale?: ")

#         # query
#         query="insert into book (name, publisher, pages, price, available) values ('%s', '%s', '%s', %s, '%s')"

#         values=(name,publisher,pages,price,available)

#         mycursor.execute(query,values)

#         # to save changes
#         mydb.commit()
#         print("succesfully data inserted")

#     elif choice==2:
#         # to fetch all data from table
#         query="select * from book"

#         # execute query
#         mycursor.execute(query)

#         # to fetch all data from query
#         data=mycursor.fetchall()

#         print(data)
     
#     loop_choice=input("do you want to perform more operations press 'y' for yes and press 'n' for no: ")
#     if loop_choice=='n' or loop_choice=='no':
#         status=False