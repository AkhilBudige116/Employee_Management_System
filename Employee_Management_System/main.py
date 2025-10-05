#  Employee Management System
Employees_Data = []

def add_employee(employees):
    pass
def view_employee(employees):
    pass
def search_employee(employees):
    pass
def update_employee(employees):
    pass
def delete_employee(employees):
    pass

# Add Employee
def add_employee():
    if len(Employees_Data) >= 8:
        print("Employee limit reached. Cannot add more employees.")
        return
    ID = input("Enter Employee ID: ")
    Name = input("Enter Name: ")
    Department = input("Enter Department: ")
    Role = input("Enter Role: ")
    Salary = input("Enter Salary: ")
    employee = {
        'ID': ID,
        'Name': Name,
        'Department': Department,
        'Role': Role,
        'Salary': Salary
    }
    Employees_Data.append(employee)
    print(f"Employee {Name} added successfully.")

# View Employees
def view_employee():
    if not Employees_Data:
        print("No employees found.")
        return
    for emp in Employees_Data:
        print(f"ID: {emp['ID']}, Name: {emp['Name']}, Department: {emp['Department']}, Role: {emp['Role']}, Salary: {emp['Salary']}")

# Search Employee
def search_employee():
    ID = input("Enter Employee ID to search : ")
    Name = input("Enter Employee Name to search : ")
    for emp in Employees_Data:
        if (ID and emp['ID'] == ID) or (Name and emp['Name'] == Name):
            print(f"Employee found: ID: {emp['ID']}, Name: {emp['Name']}, Department: {emp['Department']}, Role: {emp['Role']}, Salary: {emp['Salary']}")
            return
    print("Employee not found.")        

# Update Employee
def update_employee():
     ID = input("Enter Employee ID to update: ")
     for emp  in Employees_Data:
        if emp['ID'] == ID:
            print(f"Current details: ID: {emp['ID']}, Name: {emp['Name']}, Department: {emp['Department']}, Role: {emp['Role']}, Salary: {emp['Salary']}")
            emp['Name'] = input("Enter new name : ") or emp['Name']
            emp['Department'] = input("Enter new department : ") or emp['Department']
            emp['Role'] = input("Enter new role : ") or emp['Role']
            emp['Salary'] = input("Enter new salary : ") or emp['Salary']
            print("Employee details updated successfully.")
            return
        print("Employee not found.")

# Delete Employee
def delete_employee():  
    ID = input("Enter Employee ID to delete: ")      
    for i, emp in enumerate(Employees_Data):
        if emp['ID'] == ID:
            del Employees_Data[i]
            print(f"Employee with ID {ID} deleted successfully.")
            return
    print("Employee not found.")

# Menu
def menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employee()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
menu()    