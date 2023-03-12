# string
s="Tops Technologies"
print(s)
# for i in s:
    # print(i)
print(s.capitalize())
print(s.casefold())
print(s.center(30,"*"))
print(s.startswith("y"))
print(s.endswith("es"))
print(s.find("log"))
print("tops123".isalpha())
print("tops".isalpha())
print("tops123".isalnum())
print("123".isnumeric())
print("tops".islower())
print("tops".isupper())
print("Tops Techno".istitle())
print("hello".replace("l","w"))


# string slicing
#  01234567890123456   +
s="Tops Technologies"
#  76543210987654321   -                 
print(s)
# +ve values
print(s[1:10])
print(s[:14])
print(s[6:])
print(s[1:13:2])
print(s[::4])
# -ve values
print(s[-17:-1])
print(s[:-6])
print(s[-5:])
print(s[-15:-2:2])
print(s[::-1])


# string slicing
#  012345678901234567   +
s="Python Programming"
#  876543210987654321   -                 
print(s)
# +ve values
print(s[1:10])
print(s[:14])
print(s[6:])
print(s[1:13:2])
print(s[::4])
# -ve values
print(s[-17:-1])
print(s[:-6])
print(s[-5:])
print(s[-15:-2:2])
print(s[::-1])
