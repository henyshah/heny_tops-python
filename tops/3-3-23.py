# Dictionary 
# dictionary is a collection data type which contains key and values in pair .
# list []
# tuple ()
# set{}
# dictionary{}

# dictionary contains  only unique keys 
# dict={
#     key1 : "value",
#     key2 : "value",
# }


# dict example
# student={
#     "name":"Heny",
#     "subject":"python",
#     "marks":99
# }
# print(student)

# print(student["subject"])

# for k, v in student.items():
#     print(f"{k}={v}")
  
# for k in student.keys():
#     print(k)

# for v in student.values():
#     print(v)


# eg2 
quiz={
    1:{
    "que":"most popular programming language",
    "ans":"python"
    },
    2:{
    "que":"prime minister of india",
    "ans":"narendra modi"
    }
}
for i in range(1,len(quiz)+1):
    print(quiz[i]['que'])
    ans=input("enter ans: ")
    if ans == quiz[i]['ans']:
        print("right answer")
    else:
        print("wrong answer")

    



# eg3
# jay_bhavani={
#     "vadapav":30,
#     "dabeli":20,
#     "bhel":70,
# }
# print("menu")
# for k,v in jay_bhavani.items():
#     print(f"{k} Rs. {v}")
# cart={}
# status=True
# while status:
#     product_name=input("Enter product: ")
#     qty=int(input("Enter no. of qty: "))
#     price=qty*jay_bhavani[product_name]
#     cart[product_name]=price
#     choice=input("do you want to purchase more product: press y for yes and n for no")
#     if choice=='n' or choice=='N':
#         status=False
#         print(cart)