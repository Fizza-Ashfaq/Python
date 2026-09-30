expenses=[]

def add_expense():
    expense={}
    expense["id"]=len(expenses)+1
    expense["name"]=input("Enter description: ")
    expense["amount"]=int(input("Enter amount: "))
    expense["category"]=input("Enter category: ")
    expenses.append(expense)

def view_expense():
    print("Expenses:")
    for expense in expenses:
        for key,value in expense.items():
            print(f"{key}: {value}")

def calculate_expense():
    total=0
    for expense in expenses:
        total+=expense["amount"]
        print(f"Total amount of all expenses: {total}")

def calculate_expense_by_category():
    total=0
    category=input("Which category's expense you want to calculate")
    for expense in expenses:
        if category==expense["category"]:
            total+=expense["amount"]
            print(f"Total amount of {category} expenses: {total}")

def delete_expense():
    to_delete=int(input("Enter id of expense you want to delete: "))
    for expense in expenses:
        if to_delete==expense["id"]:
            expenses.remove(expense)
            print("Expense deleted successfully!")