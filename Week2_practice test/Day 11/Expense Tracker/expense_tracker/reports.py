from .expenses import expenses
from .utils import calculate_expense

def total_expense():
    total=calculate_expense()
    print(f"Total amount of all expenses: {total}")

def total_avg():
    total=calculate_expense()
    avg=total/len(expenses)
    print(f"Total average: {avg}")

def highest():
    highest=expenses[0]["amount"]
    for expense in expenses:
        if expense["amount"]>highest:
            highest=expense["amount"]
    print(f"Highest expense: {highest}")

