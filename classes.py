class Employee:
    num_of_emp = 0 # counts the number of employees
    average_salary = 0

    def __init__(self, salary, tax, next):
        self.salary = salary
        self.tax = tax / 100
        self.next = next
        Employee.average_salary += salary 