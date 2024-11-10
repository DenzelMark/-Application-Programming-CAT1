class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee: {self.name}, ID: {self.employee_id}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"{self.name}'s new salary: {self.salary}")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name} department")

    def total_salary_expenditure(self):
        total = sum(emp.salary for emp in self.employees)
        print(f"Total Salary Expenditure for {self.department_name}: {total}")
        return total

    def display_all_employees(self):
        print(f"Employees in {self.department_name}:")
        for emp in self.employees:
            emp.display_details()

if __name__ == "__main__":
    
    finance_department = Department("Finance")
    emp1 = Employee("Mwangi", "E001", 80000)
    emp2 = Employee("Achieng", "E002", 70000)

    finance_department.add_employee(emp1)
    finance_department.add_employee(emp2)
    
    finance_department.display_all_employees()
    finance_department.total_salary_expenditure()