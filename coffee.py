# print("Program started")
menu = {"Espresoo":150,
        "latte": 200,
        "Cappacino": 180,
        }
def show_menu ():
    print("Show menu")
    for Coffee, price in menu.items():
        print(Coffee,price)
def take_order():
    order = {}
    while True:
     choice = input("Coffee Name or done")
     if choice == "done":
        break
    #  else:
     quantity = int(input("Quantity: "))
     order[choice] = quantity
     return order
def calculate_bill(order):
    total = 0
    for coffee, quantity in order.items():
       total += menu[coffee] * quantity
       print("Total bill:", total)
show_menu()
order = take_order()
calculate_bill(order)

    