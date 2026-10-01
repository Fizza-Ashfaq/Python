class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def display_info(self):
        print(f"ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")

    def update(self, name=None, age=None, salary=None):
        if name is not None:
            self.name = name

            if age is not None:
                self.age = age

                if salary is not None:
                    self.salary = salary


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, salary):
        employee_id = len(self.employees) + 1

        employee = Employee(
            employee_id,
            name,
            age,
            salary
        )

        self.employees.append(employee)

        return employee

    def view_employees(self):
        return self.employees

    def search_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee

            return None

    def delete_employee(self, employee_id):
        employee = self.search_employee(employee_id)

        if employee:
            self.employees.remove(employee)
            return True

        return False