from farmerstest import Item, Register, printMenu, header
import json
'''
item_list = [Item('CH1','Chai',3.11),Item('AP1','Apples',6.00), Item('CF1','Coffee',11.23),Item('MK1','Milk',4.75),Item('OM1','Oatmeal',3.69)]
#print(item_list)
#for item in item_list:
    #print(item)

cart = [Item('CH1','Chai',3.11),Item('CH1','Chai',3.11),Item('OM1','Oatmeal',3.69)]
for item in cart:
    print(item)

cart[0][0]
'''

if __name__ == "__main__":
    printMenu()
    print("Hello! Welcome to the Farmer's Market.")
    new_checkout = Register()
    cart = new_checkout.addtoCart()
    new_checkout.bogo_discount()
    new_checkout.apple_discount()
    new_checkout.chai_milk_discount()
    new_checkout.oatmeal_apple_discount()
    new_checkout.double_discount()
    header()
    try:
        for items in cart:
            print(items)
    except NoneType:
        print("You didn't add anything to the basket! Please come back again.")
    new_checkout.calculateTotal()



