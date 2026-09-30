from Expense_tracker import add_expense,delete_expense,view_expense,calculate_expense,calculate_expense_by_category

cont=True
while cont:
    print("----Expense Tracker System----")
    print("1. Add expense")
    print("2. View expense")
    print("3. Calculate expense")
    print("4. Calculate expense by category")
    print("5. Delete expense")
    print("6. Exit")
    op=input(f"Choose an option(1-6): \n\n")

    match op:
        case "1":
            add_expense()
        case "2":
            view_expense()
        case "3":
            calculate_expense()
        case "4":
            calculate_expense_by_category()
        case "5":
            delete_expense()
        case "6":
            cont=False
        case _:
            print("Please enter a valid record ")

