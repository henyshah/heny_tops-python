# TASK 1 : accept two numbers from user and check which number is greater 
# n1 = float(input("Enter the first number: "))
# n2 = float(input("Enter the second number: "))

# if n1 > n2:
#     print(n1, "is greater than", n2)
# elif n1 < n2:
#     print(n2, "is greater than", n1)
# else:
#     print(n1, "and", n2, "are equal")


# TASK 2 : accept two numbers and check entered number is positive or negative 
# n = int(input("Enter number : "))
# if n>0:
#     print("\nIt is +ve")

# else: 
#     print("\nIt is -ve")
    

# accept two numbers and check entered number is even and odd
# n = int(input("Enter number : "))
# if (n%2)==0:
#     print("\nIt is even")
# else: 
#     print("\nIt is odd")


# TASK 3 : mini project : 
# KALYAN JWELLERS : 

# M 
# >  65
# purchase > 2lk - 3lk    20% 
# purchase > 3lk - 5lk 	30% 
# purchase > 5lk  	35% 


# <65
# purchase > 2lk - 3lk    10% 
# purchase > 3lk - 5lk 	20% 
# purchase > 5lk  	25% 



# F
# >  65
# purchase > 2lk - 3lk    25% 
# purchase > 3lk - 5lk 	35% 
# purchase > 5lk  	40% 


# <65
# purchase > 2lk - 3lk    15% 
# purchase > 3lk - 5lk 	25% 
# purchase > 5lk  	30% 


# ------------------------------------------------------------
# Enter your name : 
# Enter gender : 
# Enter age : 

# Enter product : Ring 
# Enter product gram : 20  
# current gold price (1 grm) : 5752

# -------------------------------------
# TOTAL GOLD RATE :  XXXXX 


# Making charges (1 gram)  : 845
# Total Making CHarges :    TOTAL GOLD  X  MAKING CHARGES 

# ---------------------------------------
# TOTAL AMOUNT : GOLD PRICE + TOTAL MAKING CHARGES



# DISCOUNT :   25 (AUTOMATIC) 
# DIS- AMOUNT : except (making charges) 
# -----------------------------------------
# total net amount : 

# --------------------------------------------
# HINT : variables , input , conditional statements 


GOLD_PRICE_PER_GRAM = 5752
MAKING_CHARGES_PER_GRAM = 845

def calculate_gold_rate(gram):
    return GOLD_PRICE_PER_GRAM * gram

def calculate_making_charges(gold_rate):
    return MAKING_CHARGES_PER_GRAM * gold_rate

def calculate_discount(age, gender, purchase_amount):
    discount = 0
    if gender == 'M':
        if age >= 65:
            if purchase_amount > 500000:
                discount = 0.35
            elif purchase_amount > 300000:
                discount = 0.3
            elif purchase_amount > 200000:
                discount = 0.2
        else:
            if purchase_amount > 500000:
                discount = 0.25
            elif purchase_amount > 300000:
                discount = 0.2
            elif purchase_amount > 200000:
                discount = 0.1
    elif gender == 'F':
        if age >= 65:
            if purchase_amount > 500000:
                discount = 0.4
            elif purchase_amount > 300000:
                discount = 0.35
            elif purchase_amount > 200000:
                discount = 0.25
        else:
            if purchase_amount > 500000:
                discount = 0.3
            elif purchase_amount > 300000:
                discount = 0.25
            elif purchase_amount > 200000:
                discount = 0.15
    return discount


name = input("Enter your name: ")
gender = input("Enter your gender (M/F): ")
age = int(input("Enter your age: "))
product = input("Enter product: ")
gram = float(input("Enter product gram: "))
gold_rate = calculate_gold_rate(gram)
print("-------------------------------------------")
print("TOTAL GOLD RATE : ", gold_rate)
making_charges = calculate_making_charges(gold_rate)
print("Making charges (1 gram)  : ", MAKING_CHARGES_PER_GRAM)
print("Total Making Charges :   ", making_charges)
total_amount = gold_rate + making_charges
print("-------------------------------------------")
print("TOTAL AMOUNT : ", total_amount)
discount = calculate_discount(age, gender, total_amount)
discount_amount = total_amount * discount
print("DISCOUNT : ", discount * 100, "%")
print("DIS- AMOUNT : ", discount_amount)
net_amount = total_amount - discount_amount
print("--------------------------------------------")
print("total net amount : ", net_amount)
print("--------------------------------------------")
