import json
import os


def printMenu():
    print('+'+'--------------- '+'|'+' --------------- '+'|'+ ' ---------'+ '+')
    print('|  '+'Product Code  '+'|'+'\tName \t'+'   |'+'   Price  '+'|')
    print('+'+'--------------- '+'|'+' --------------- '+'|'+ ' ---------'+ '+')
    print('|'+'\tCH1\t'+' |'+'\tChai\t'+'   |'+'  $3.11  '+' |')
    print('|'+'\tAP1\t'+' |'+'\tApples\t'+'   |'+'  $6.00  '+' |')
    print('|'+'\tCF1\t'+' |'+'\tCoffee\t'+'   |'+'  $11.23  '+'|')
    print('|'+'\tMK1\t'+' |'+'\tMilk\t'+'   |'+'  $4.75  '+' |')
    print('|'+'\tOM1\t'+' |'+'\tOatmeal\t'+'   |'+'  $3.69  '+' |')
    print('+'+'--------------- '+'|'+' --------------- '+'|'+ ' ---------'+ '+')

def header():
        print("|\tItem\t\t\tPrice\t|")
        print("-----------------------------------------")

class Item:

    def __init__(self,code,name,discount,price):
        self.code = code
        self.name = name
        self.discount = discount
        self.price = price
    
    def __str__(self):
        string = "|\t"+str(self.code)
        string+= f"\t{self.name}"
        string+= f"\t{self.discount}"
        string+= "\t{0:.2f}\t|".format(self.price)
        return string


class Register():
    
    def __init__(self):
        self.cart = []
        self.total = 0

    def loadMenu(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__,'menu.json')) as f:
            self.data = json.load(f)

    def createItem(self,code):
        item_value = self.data[code]
        name = item_value[0]
        discount = item_value[1]
        price = item_value[2]
        return Item(code,name,discount,price)

    def addtoCart(self):
    #function to ask user for product codes and create the cart
        self.loadMenu()
        add = ''
        while add == '':
            self.answer = input("Please enter the product code. (Press N at any time to finish): ").upper()
            if self.answer != 'N' and self.answer in self.data.keys():
                new_item = self.createItem(self.answer)
                self.cart.append(new_item)
                print('Product added to cart!')
            elif self.answer not in self.data.keys() and self.answer != 'N':
                print("We currently do not have that for sale! Please try again.")
                add = ''
            else:
                add = 'N'
        return self.cart
          
    def bogo_discount(self):
        i = 0
        f = 0 
        coffee_count = 0
        while i < len(self.cart): #parse the cart for existing coffee
            if self.cart[i].code == 'CF1' and self.cart[i].discount != "BOGO": #if coffee exists, parse cart for a second coffee to apply bogo
                coffee_count += 1
                if coffee_count == 1:
                    self.cart.insert(i+1,Item('CF1','','BOGO',-11.23))
                    self.cart.insert(i+1,Item('CF1','Coffee','BOGO',11.23))
                elif coffee_count > 1:
                    self.cart.insert(i+1, Item('CF1','','BOGO',-11.23))
            i+=1
    
    def apple_discount(self):
        apple_count = 0
        i = 0
        f = 0
        while i < len(self.cart):
            if self.cart[i].code == 'AP1' and self.cart[i].discount != "APPL":
                apple_count += 1
            i+=1
        if apple_count >= 3:     
            while f < len(self.cart):
                if self.cart[f].code == 'AP1' and self.cart[f].discount != "APPL":
                    self.cart.insert(f+1,Item('AP1','','APPL',-1.50))
                f+=1
    
    def chai_milk_discount(self):
        chmk_count = 0
        i = 0
        f = 0
        z = 0
        while i < len(self.cart):
            if self.cart[i].code == 'CH1': #check for chai milk
                while f < len(self.cart): #parse the cart for existing Milk, if existing, add the discount under it
                    if self.cart[f].code == 'MK1' and self.cart[f].discount != "CHMK" and chmk_count < 1:
                        self.cart.insert(f+1, Item('MK1','','CHMK',-4.75))
                        chmk_count +=1
                    f+=1
                    
                if chmk_count < 1: #if no existing milk
                    self.cart.append(Item('MK1','','',4.75))
                    self.cart.append(Item('','','CHMK',-4.75))
                    chmk_count += 1
                    z+=1                    
            i+=1
    
    def oatmeal_apple_discount(self):
        i = 0
        apom = 0
        f = 0
        while i < len(self.cart) and apom < 1:
            if self.cart[i].code == 'OM1':
                while f < len(self.cart):
                    if self.cart[f].code == 'AP1' and self.cart[f].discount != "APPL" and self.cart[f].discount != "APOM" and apom < 1:
                        self.cart.insert(f+1,Item('AP1','','APOM',-3.00))
                        apom += 1
                    f += 1        
            i+=1
    
    def double_discount(self):
        # check to see if more than one discount was applied on a single grocery item.
        # if so, only apply the higher discount

        i = 0 
        while i < len(self.cart):
            if self.cart[i].name == '' and self.cart[i+1].name == '': #if there are two discounts in a row (indicating two discounts on one item)
                #check to see which discount is greater
                if self.cart[i].discount < self.cart[i+1].discount: 
                    self.cart.remove(self.cart[i+1])
                elif self.cart[i].discount > self.cart[i+1].discount:
                    self.cart.remove(self.cart[i])
            i+=1


        # directly checking for apom and appl discount method:
        # count_apom = 0
        # count_appl = 0
        # for item in self.cart:
        #     if item.discount == "APOM":
        #         count_apom += 1
        #     elif item.discount == "APPL":
        #         count_appl += 1
        
        # while count_apom >= 1 and count_appl >= 1: #if there's an apom discount 
        #     for item in self.cart:
        #         if item.discount == "APPL":
        #             self.cart.remove(item)
        #             count_apom -= 1
        #             break

    def calculateTotal(self):
        for item in self.cart:
            self.total += item.price
        print("-----------------------------------------")
        print("| Total:\t\t\t${:.2f}\t|".format(self.total))


        

                

