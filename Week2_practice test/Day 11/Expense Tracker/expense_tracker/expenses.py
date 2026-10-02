expenses=[]

def add_expense():
    expense={}
    expense["id"]=len(expenses)+1
    expense["name"]=input("Enter description: ")
    expense["amount"]=int(input("Enter amount: "))
    expense["category"]=input("Enter category: ")
    expenses.append(expense)

def delete_expense():
    to_delete=int(input("Enter id of expense you want to delete: "))
    for expense in expenses:
        if to_delete==expense["id"]:
            expenses.remove(expense)
            print("Expense deleted successfully!")