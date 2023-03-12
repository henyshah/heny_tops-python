# product manager
# product_menu={}  
# menu="""
#               press 1 for product manager
#               press 2 for customer
#               press 3 for exit 
              
#     """
# status=True
# p_status=True
# while status:
#     print(menu)
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         while p_status:
#             spec={}
#             print("WELCOME TO PRODUCT MANGER")
#             product_name=input("Enter product name: ")
#             qty=int(input("Enter qty: "))
#             amount=int(input("Enter amount: "))
#             if product_name in product_menu.keys():
#                 spec['qty']=product_menu[product_name]['qty']+qty
#                 spec['amount']=amount
#             else:
#                 spec['qty']=qty
#                 spec['amount']=amount
#             product_menu[product_name]=spec
#             print(product_menu)
#             p_choice=input("DO YOU WANT TO ADD MORE PRODUCT? (y/n) ")
#             if p_choice=='n':
#                 p_status=False
#     elif choice==2:
#         print("customer")
#     else:
#         print("THANK YOU FOR USING THIS APPICATION")
#         status=False


# customer panel
products = {
    'kiwi': {'qty': 20, 'price': 220},
    'apple': {'qty': 50, 'price': 150}
}
cart = {}
while True:
    print("Product List:")
    for product_name, details in products.items():
        print(f"{product_name.capitalize()}\t{details['qty']}\tRs. {details['price']} per box")

    print("-" * 50)
    product_name = input("Enter product name: ").lower()
    qty = int(input("Qty: "))
    price = products[product_name]['price']
    total_price = price * qty
    print(f"Total Price = Rs. {price} * {qty} = {total_price}\n")
    if product_name in cart:
        cart[product_name] += qty
    else:
        cart[product_name] = qty
    choice = input("Do you want to purchase more products? (y/n): ")
    if choice.lower() == "n":
        break

    print("-" * 50)
print("-" * 50)
print("Cart:")
total_cost = 0
for product_name, qty in cart.items():
    price = products[product_name]['price']
    cost = price * qty
    total_cost += cost
    print(f"{product_name.capitalize()}\t{qty}\tRs. {cost}")
print(f"Total = {total_cost} Rs.")

