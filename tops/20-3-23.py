# lambda function:function without any name is called lambda.
# it is anonymous function. 
# function 
    # syntax:
        #   var=lambda args:expression



# normal function
# def sum(n1,n2):
#     ans=n1+n2
#     return ans
# print(sum(10,10))


# lambda function
# ans=lambda n1,n2:n1+n2
# print(ans(10,10))


"""
filter():filter is a method which is filter given sequence with the help of function that test each element of the sequence.
     syntax:
            filter(function,sequence)
"""

# l1=['a','e','v','j','a']
# vowels_list=['a','e','i','o','u']
# l2=[]
# def checkVowel():
#     for c in l1:
#         if c in vowels_list:
#             l2.append(c)
# checkVowel()
# print(l2)

# for i in l2:
#     print(i)


# using filter
# l1=['a','e','v','j','a']
# vowels_list=['a','e','i','o','u']
# def myfun(seq):
#     if(seq in vowels_list):
#         return True
#     else:
#         return False
# filtered_data=filter(myfun,l1)
# for i in filtered_data:
#     print(i)


# print even nos. using filter
# data_set=[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
# def my_fun(data):
#     if data %2==0:
#         return True
#     else:
#         return False
# filtered_data=filter(my_fun,data_set)
# for i in filtered_data:
#     print(i)


# filterd subjects available in list or not 
# subjects=["english","maths","java","android","SS"]
# tops_subject=["C","C++","java","android","flutter"]

subjects=["english","maths","java","android","SS"]
tops_subject=["C","C++","java","android","flutter"]
def myfun(seq):
    if(seq in tops_subject):
        return True
    else:
        return False
filtered_data=filter(myfun,subjects)
for i in filtered_data:
    print(i)