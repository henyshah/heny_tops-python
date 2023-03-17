"""
there are 4 type sof function categories
(1)function without parameter and function without return type.
          syntax:   def<funname>()
          //block of code

          <funname>

(2)function with parameter and function without return type.
           syntax:   def add(n1,n2):
           //operation

            syntax:   def mul(n1,n2):
           //operation

"""


# db={}
# def registration(firstname,email,password):
#     db['name']=firstname
#     db['email']=email
#     db['password']=password
#     print("Registration is done succesfully!!!")

# def login(email,password):
#     if email==db['email']:
#         if password==db['password']:
#             return db['name']
#         else:
#             return "Invalid email or password"
#     else:
#         return"Invalid email or password"
    
# status=True
# while status:
#     menu="""
#     (1)press 1 for registration
#     (2)press 2 for login
#     (3)press 3 for exit
#     """
#     print(menu)

#     choice = int(input("enter your choice: "))
#     if choice==1:
#         name=input("enter name: ")
#         email=input("enter email: ")
#         password=input("enter password: ")
#         registration(name,email,password)

#     elif choice==2:
#         email=input("enter email: ")
#         password=input("enter password: ")
#         login(email,password)

#     elif choice==3:
#         status=False    



"""
*args: arguments  (tuple as parameter)

**kwargs: key with arguments   (dictionary as parameter)

"""

# normal function with normal parameter
def sum(n1,n2):
    ans=n1+n2
    print(ans)
sum(10,20) 


# *args function
def addition(*n):
    ans=0
    for i in n:ans+=i
    print(ans)
addition(1,2,3,4,5,6,7,8,9,10)


# **kwargs function
def myfun(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}={v}")
myfun(name="heny",subject="python")