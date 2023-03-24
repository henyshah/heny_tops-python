# keywords: a word which have predefined meaning.
    # a reserved word  
    # you can't take it keyword as a variable

"""
for,
while,
continue,
break,
......are the keywords
"""

import keyword 
keyword_list=keyword.kwlist
print(keyword_list)
name=input("enter name: ")
if name in keyword_list:
    print("yes it is a keyword")
else:
    print("no it is not a keyword")    
 