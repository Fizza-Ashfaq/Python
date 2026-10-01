from employee import EmployeeManager
import logging
manager=EmployeeManager()
def add_employee():
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = int(input("Enter salary: "))
        employee = manager.add_employee(name, age, salary)
    except ValueError:
        logging.error("Value error")
    else:
        print("\nEmployee added successfully!")
        employee.display_info()


def view_employees():
    employees = manager.view_employees()

    if not employees:
        print("No employees found.")
    else:
        for employee in employees:
            print("\n----------------")
            employee.display_info()

def search_employee():
    employee_id = int(input("Enter employee ID to search: "))

    employee = manager.search_employee(employee_id)

    if employee:
        employee.display_info()
    else:
        print("Employee not found.")


def update_employee():
    employee_id=int(input("Enter employee id to update: "))
    employee = manager.search_employee(employee_id)

    if employee:
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        salary = int(input("Enter new salary: "))
        employee.update(name, age, salary)
        print("Employee updated successfully!")
    else:
        print("Employee not found.")

def delete_employee():
    
    employee_id = int(input("Enter employee ID to delete: "))
    if manager.delete_employee(employee_id):
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")