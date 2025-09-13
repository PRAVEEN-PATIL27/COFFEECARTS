menu = {
    "Espresso": 10,
    "Latte": 15,
    "Cappuccino": 12,
    "Mocha": 18
}

cart=[]


def showmenu():
    print("-----COFFEE SHOP MENU -----")
    for item,price in menu.items():
        print(f"{item}-${price}")


def addtocart(item):
    if item in menu:
        cart.append(item)
        print("ITEM ADDED TO CART")
    else:
        print("item not found in cart")
        
        
def checkout():
    if not cart:
        print("CART IS EMPTY")
        return
    total=sum(menu[item] for item in cart)
    print("BILL AMOUNT")
    for item in cart:
        print(f"{item}-${menu[item]}")
    print("TOTAL-$",total)
    print("THANK YOU FOR VISITING")


while True:
    showmenu()
    choice = input("\nEnter coffee name (or 'done' to checkout): ").title()
    if choice == "Done":
        checkout()
        break
    addtocart(choice)