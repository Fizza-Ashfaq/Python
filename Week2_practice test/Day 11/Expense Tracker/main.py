from expense_tracker import add_expense,delete_expense,total_expense,total_avg,highest

cont=True
while cont:
    print(f"\n\n----Expense Tracker System----")
    print("1. Add expense")
    print("2. Total expense")
    print("3. Average of expenses")
    print("4. Highest expense:")
    print("5. Delete expense")
    print("6. Exit")
    op=input("Choose an option(1-6): ")

    match op:
        case "1":
            add_expense()
        case "2":
            total_expense()
        case "3":
            total_avg()
        case "4":
            highest()
        case "5":
            delete_expense()
        case "6":
            cont=False
        case _:
            print("Please enter a valid record ")

