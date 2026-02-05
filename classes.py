class PersonalData():
    def __init__(self, name, age, gender, birthdate, fb, ig, twt, linkedin):
        self.name = name
        self.age = age 
        self.gender = gender
        self.birthdate = birthdate 
        self.fb = fb
        self.ig = ig
        self.twt = twt
        self.linkedin = linkedin
        

class LoginData():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class EmployeeData():
    def __init__(self, salary, tax, occupation, title, company):
        self.monthly_salary = salary - (salary * (tax / 100))
        self.occupation = occupation
        self.title = title
        self.company = company

class Node:
    def __init__(self, login_data, personal_data, emp_data):
        self.login_data = login_data
        self.personal_data = personal_data
        self.employee_data = emp_data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, login_data, personal_data, emp_data):
        new_node = Node(login_data, personal_data, emp_data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node 