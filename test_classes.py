# Test script to check if classes work technically

import classes as cls 

# Test PersonalData
try:
    pd = cls.PersonalData("John Doe", 30, "Male", "1993-01-01", "fb.com/johndoe", "ig.com/johndoe", "twt.com/johndoe", "linkedin.com/johndoe")
    print("PersonalData: OK")
except Exception as e:
    print(f"PersonalData: ERROR - {e}")

# Test LoginData
try:
    ld = cls.LoginData("johndoe", "password123", "john@example.com")
    print("LoginData: OK")
except Exception as e:
    print(f"LoginData: ERROR - {e}")

# Test EmployeeData
try:
    ed = cls.EmployeeData(50000, 10, "Engineer", "Senior Engineer", "TechCorp")
    print(f"EmployeeData: OK - Monthly Salary: {ed.monthly_salary}")
except Exception as e:
    print(f"EmployeeData: ERROR - {e}")

# Test Node
try:
    node = cls.Node(ld, pd, ed)
    print("Node: OK")
except Exception as e:
    print(f"Node: ERROR - {e}")

# Test LinkedList insert
try:
    ll = cls.LinkedList()
    # Assuming insert expects a tuple of (login_data, personal_data, emp_data)
    data = (ld, pd, ed)
    ll.insert(*data)
    print("LinkedList insert: OK")
except Exception as e:
    print(f"LinkedList insert: ERROR - {e}")
