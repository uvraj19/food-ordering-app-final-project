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