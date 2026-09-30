from pathlib import Path
import json

filepath=Path("data")/"inventory.json"

def get_inventory():
    try:
        with open(filepath, "r") as file: 
            inventory = json.load(file)
    except FileNotFoundError:
        print("File not found")
    else:
        return inventory


def add():
    inventory=get_inventory()
    try:
        name=input("Enter product name: ")
        price=int(input("Enter product price: "))
        quantity=int(input("Enter product quantity:"))
    except ValueError:
        print("Please enter valid values")

    product={
        "id":len(inventory)+1,
        "name":name,
        "price":price,
        "quantity":quantity
    }

    inventory.append(product)
    with open(filepath,"w") as file:
        json.dump(inventory,file,indent=4)

def view():
    with open(filepath,"r") as file:
        inventory=json.load(file)

        print(f"Inventory: {inventory}")

def update():

    to_update=int(input("Enter a product id to update: "))
    inventory=get_inventory()

    found=False
    for product in inventory:
        if product["id"]==to_update:
            product["name"]=input("Enter product name: ")
            product["price"]=int(input("Enter product price: "))
            product["quantity"]=int(input("Enter product quantity:"))


            found=True
            break

    if found==False:
        print("Product not found!")
    else:
        with open(filepath,"w") as file:
            json.dump(inventory,file,indent=4)


def delete():

    to_delete=int(input("Enter a product id to delete: "))
    inventory=get_inventory()

    found=False
    for product in inventory:
        if product["id"]==to_delete:
            inventory.remove(product)
            found=True

            if found==False:
                print("Product not found!")
            else:
                with open(filepath,"w") as file:
                    json.dump(inventory,file,indent=4)