#define the menu of the restrarnat
menu = {
    'pizza':50,
    'pasta':30,
    'burger':25,
    'salad':60,
    'coffee':20
    }
print(menu)
# greet the customer
print("Welcome to the Akshu&ganu Restrarant")
print("pizza:Rs50\npasta:Rs30\nburger:Rs25\nsalad:Rs60\ncoffee:20")

order_total=0

item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total += menu[item_1] #0+50
    print(f"your item{item_1}has been added to your order")

else:
    print(f"ordered item{item_1}is not available yet sorry!")


another_order =input("do you want to add another item ?(yes/no)")
if another_order=="yes": 
    item_2 = input("Enter the name of the second item :")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item{item_2}has been added to your order")
    else:
        print(f"order item{item_2}is not available")

print(f"the total amount of item is {order_total} thank you for visiting !")
