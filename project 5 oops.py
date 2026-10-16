class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Person Details:")
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Salary: $" + str(float(self.salary)))


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def show_details(self):
        print("Manager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Salary: $" + str(float(self.salary)))
        print("Department:", self.department)


person = None
employee = None
manager = None

while True:

    print("\nChoose any of the givenoperation:")
    print("1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)

        print("Person created with name:", name,
              "and age:", age)

    elif choice == 2:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(name, age, emp_id, salary)

        print("Employee created with name:", name,
              ", age:", age,
              ", ID:", emp_id,
              ", and salary: $" + str(salary) + ".")

    elif choice == 3:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(name, age, emp_id, salary, department)

        print("Manager created with name:", name,
              ", age:", age,
              ", ID:", emp_id,
              ", salary: $" + str(salary),
              ", and department:", department + ".")

    elif choice == 4:
        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        detail_choice = int(input("please Enter your choice: "))

        if detail_choice == 1:
            if person:
                person.show_details()
            else:
                print("Person not created.")

        elif detail_choice == 2:
            if employee:
                employee.show_details()
            else:
                print("Employee not created.")

        elif detail_choice == 3:
            if manager:
                manager.show_details()
            else:
                print("Manager not created.")

        else:
            print("Invalid choice.")

    elif choice == 5:
        print("\nExiting the system. All resources have been freed.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice.Kindly try again.")