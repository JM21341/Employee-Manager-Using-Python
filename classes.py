class Employee:
    num_of_emp = 0 # counts the number of employees

    def __init__(self, name, age, salary, tax, next):
        self.name = name
        self.age = age
        self.salary = salary
        self.tax = tax / 100
        self.next = None
        Employee.num_of_emp += 1
    
class Teacher(Employee):
    def __init__(self):
        pass