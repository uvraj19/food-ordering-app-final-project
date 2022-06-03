import admin as ad
import user as ur
from user import User


uhh = User(str, str, str, str, str)

inp = int(input("Where You want to login select 1.Admin and 2.User and 3.Exit"))
if inp == 1:
    Username = input("Enter the username of admin: ")
    Password = input("Enter the password of admin: ")
    if ad.admin_keys[Username] == Password:
        print("*****You're successfully logged inn*****")
        admin_crawler = True
        while admin_crawler:
            adm_choice = int(input("Choose the options of admin panel 1.ADD NEW ITEM 2.EDIT ITEM 3.VIEW INVENTORY 4.REMOVE ITEM 5.EXIT"))
            if adm_choice == 1:
                ad.add_new_item()
            elif adm_choice == 2:
                ad.edit_from_item()
            elif adm_choice == 3:
                ad.show_inven()
            elif adm_choice == 4:
                ad.remove_item()
            elif adm_choice == 5:
                print(f"You're Exit to the admin panel{Username}")
                admin_crawler = False
            else:
                print("This is the wrong selection please select valid option")
    else:
        print("These are the wrong credentials! SORRY!!!")
elif inp == 2:
    print("Welcome to the user panel, resister your account")
    ur.account_register()
    username = input("Enter the username here: ")
    password = input("Enter the password here: ")
    if User.login(username, password):
        print(f"You are logged in successfully {username}")
    user_crawler = True
    while user_crawler:
            usr_choice = int(input(f"{username}, Enter the option 1.Place new order 2.Order history 3.Exit"))
            if usr_choice == 1:
                uhh.place_order()
            elif usr_choice == 2:
                print(f"Here is your order history, {username}")
                print(uhh.order_history)
            elif usr_choice == 3:
                user_crawler = False
                print("You're Successfully looged out")
            else:
                print("You choose the invalid option")
    else:
        print("These are the wrong credentials! SORRY!!!")
else:
    exit()


admin_keys = {"Yuvraj": "123456"}

inven = {1: {'ItemName': 'Tandoori Chicken','ItemID': 1,'Quantity': 4 ,'Price': 240,'Discount':5, 'Stock': 14},
        2: {'ItemName': 'Vegan Burger', 'ItemID': 2, 'Quantity': 1 ,'Price': 320,'Discount':5, 'Stock': 20},
        3: {'ItemName': 'Truffle Cake', 'ItemID': 3,'Quantity': 500, 'Price': 920,'Discount':5, 'Stock': 5}}
#nested dict

def add_new_item():
    itemname = input("Enter the Item name: ")
    itemid = int(input("Enter the item id: "))
    price = int(input("Enter the price of the item: "))
    stock = int(input("Enter the stock value of item: "))
    Quantity = int(input("enter value:"))
    Discount = int(input("enter value:"))
    inven[itemid] = {
        "ItemName": itemname,
        "ItemID": itemid,
        "Quantity": Quantity,
        "Price": price,
        "Discount": Discount,
        "Stock": stock
    }
    print("The Item"+itemname+ "is successfully added")
    return inven


def edit_from_item():
    item = int(input("Enter the itemid which you want to edit: "))
    a = input("Enter the item name")
    b = int(input("Enter the price of item"))
    c = int(input("Enter the stock of the item"))
    d = int(input("Enter the stock of the item"))
    e = int(input("Enter the stock of the item"))
    inven[item]["ItemName"] = a
    inven[item]["Quantity"] = b
    inven[item]["Price"] = c
    inven[item]["Discount"] = d
    inven[item]["Stock"] = e
    print("*****Edited item successfully*****")
    return inven


def show_inven():
    print("*****HERE IS THE INVENTORY OF RAKSHAK MART*****")
    def piece_item(i):
        print("Item Name: ",inven[i]["ItemName"])
        print("Price: ",inven[i]["Price"],"INR")
        print("Item ID: ",inven[i]["ItemID"])
        print("Stock: ",inven[i]["Stock"])
        print("Discount: ",inven[i]["Discount"],"%")
        print("Quantity: ",inven[i]["Quantity"],"pieces")
    piece_item(1)
    piece_item(2)
    def piece_item(i):
        print("Item Name: ",inven[i]["ItemName"])
        print("Price: ",inven[i]["Price"],"INR")
        print("Item ID: ",inven[i]["ItemID"])
        print("Stock: ",inven[i]["Stock"])
        print("Discount: ",inven[i]["Discount"],"%")
        print("Quantity: ",inven[i]["Quantity"],"gm")
    piece_item(3)
    
    return inven

def remove_item():
    d = int(input("Enter the Item id which you want to exit"))
    inven.pop(d)
    print("Remove item successfully ")
    return inven

import admin as ad

class User:
    username = " "
    password = " "
    login_info = {"username":username, "password": password}

    def __init__(self, name, number, email, address, password):
        self.name = name
        self.number = number
        self.email = email
        self.address = address
        self.password = password
        User.login_info["username"] = self.name
        User.login_info["password"] = self.password
        self.profile={"Name":name}
        self.order_history = {}

    @classmethod
    def login(cls,name,password):
          if cls.login_info["username"] == name and cls.login_info["password"] == password :
              print("You're are successfully logged in.....")
              return True
          else:
              print("SORRY! These are the Wrong Credentials")
              return False

    def place_order(self):
        print("What you want to order here in the Inventory")
        print(ad.show_inven())
        user_choice = int(input("If you want to order then select 1.YES 2.NO"))
        if user_choice == 1:
            n=int(input("Enter how many items do you want to Order"))
            x=0
            for i in range(n):
             itemid = int(input("Enter the Item id here: "))
             quan = int(input("Enter the quantity of the item: "))
             quantity =int(ad.inven[itemid]["Quantity"])
             price = ad.inven[itemid]["Price"]
             discount = ad.inven[itemid]["Discount"]
             x = x + ((price * quan)/quantity)
             print(x)
             thresvalue = int(input("thresvalue :"))
             if quan> thresvalue:
                x = x - ((x*discount)/100)
                print(x)
             elif quan <= thresvalue:
                print(x)
             again_ask = input("Are you still want to order this Enter YES or NO")
             if again_ask == "YES":
                print(f'''Your item name is {ad.inven[itemid]["ItemName"]}''')
                print(f'''Price of your Item is {ad.inven[itemid]["Price"]}''')
                print(f"This is your quantity {quan}")
                print(f"It costs you {x}INR in total")
                print("You're all set for this order")
                self.order_history[itemid] = {
                    "Item Name": ad.inven[itemid]["ItemName"],
                    "Price": ad.inven[itemid]["Price"],
                    "Quantity": quan
                }
                final_stock = ad.inven[itemid]["Stock"] - quan
                ad.inven[itemid]["Stock"] = final_stock
                print("You're order is successfully placed")

             elif again_ask == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")

    def display(self):
        print("name:",self.name)
        print("number:",self.number)
        print("email:",self.email)
        print("adress:",self.address)
        print("password:",self.password)
        print("login_info:",User.login_info)



def account_register():
    cs = User(input("name: "),int(input("enter number: ")),input("email_id: "),input("enter_ adress: "),input("enter password: "))
    return cs.display()


       


