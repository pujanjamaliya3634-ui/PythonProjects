# Data Analyzer and Transformer Program

data = []

while True:

    print("\n===== CHOOSE ANOTHER OPTION =====")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    # 1. Create a Person
    if choice == "1":

        name = input("Enter the name:")
        age = input("Enter the age:")
        print("Person  created with name:",name,"and age:",age)
    # 2. Create a Employee
    elif choice == "2":
        name = input("Enter the name:")
        age = input("Enter the age:")
        employee = input("Enter the Employee ID:")
        salary = input("Enter the Salary:")
        print("Employee created with name:",name,"age:",age,"ID:",employee,"Salary:",salary)
        

    # 3. Create a Manager
    elif choice == "3":
        name = input("Enter the name:")
        age = input("Enter the age:")
        employee = input("Enter the Employee ID:")
        salary = input("Enter the Salary:")
        department=input("Enter the Department")
        print("Employee created with name:",name,",age:",age,",ID:",employee,",Salary:",salary,",and Department:",department)            
       
    # 4. Filter Data by Threshold
    elif choice == "4":
        while True:
            print("Choose details to show:")
            print("1. Create a Person")
            print("2. Create an Employee")
            print("3. Create a Manager")
            print("4. Exit")
            choice1 = input("Enter your choice: ")

            if choice1 == "1":
                print("Name:",name)
                print("Age:",age)
            elif choice1 == "2":
                print("Name:",name)
                print("Age:",age)
                print("Employee ID:",employee)
                print("Salary:",salary)
            elif choice1 == "3":
                print("Name:",name)
                print("Age:",age)
                print("Employee ID:",employee)
                print("Salary:",salary)
                print("Department:",department)
            elif choice1 == "4":
                break
            else:
                print("Invalid Choice")
    
     # 5. Sort Data
    elif choice == "5":        
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
