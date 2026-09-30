from operations import add,view,update,delete

cont=True
while cont:
    print("----Inventory System----")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update product")
    print("4. Delete Product")
    print("5. Exit")
    op=input("Choose an option(1-5): ")

    match op:
        case "1":
            add()
        case "2":
            view()
        case "3":
            update()
        case "4":
            delete()
        case "5":
            print("Exiting")
            cont=False
            break
        case _:
            print("Please enter a valid option")