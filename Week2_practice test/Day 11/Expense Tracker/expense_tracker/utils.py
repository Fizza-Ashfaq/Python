from .expenses import expenses

def view_expense():
    print("Expenses:")
    for expense in expenses:
        for key,value in expense.items():
            print(f"{key}: {value}")

def calculate_expense():
    total=0
    for expense in expenses:
        total+=expense["amount"]
    return total