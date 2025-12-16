class Person:
    def __init__(self):
        print("\t")
        self.name=input("Enter Name: ")
        self.age=int(input("Enter Age:"))
    def show_person(self):
        print(f"-Person Created With Name: {self.name} and Age: {self.age}.")
        print("\t")
    def p_detail(self):
        print("\t")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("\t")

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.id=int(input("Enter Employee ID:"))
        self.salary=float(input("Enter Salary:"))

    def show_employee(self):
        print(f"-Employee created with Name: {self.name} , Age: {self.age} , ID: {self.id} And Salary: {self.salary}")
        print("\t")

    def e_detail(self):
        print("\t")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.id}")
        print(f"Salary: {self.salary}")
        print("\t")


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department=input("Enter Department:")
        print("\t")
    def show_manager(self):
        print(f"-Manager created with Name: {self.name} , Age: {self.age} , ID: {self.id} , Salary: {self.salary} And Departemnt: {self.department}.")
        print("\t")

    def m_detail(self):
        print("\t")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.id}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")
        print("\t")
persons=[]
employees=[]
managers=[]
def menu():
    print("\t")
    print("---Employee Management System---")
    print("\t")
    while True:
        print("Choose an Operation:-")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")
        choice=int(input("Enter your Choice :"))
        print("\t")
        match choice:
            case 1:
                n=int(input("How many Persons you want to add :"))
                print("\t")
                for i in range(n):
                    print(f"-ADD Person {i+1} Details:-")
                    per=Person()
                    per.show_person()
                    persons.append(per)
            case 2:
                n=int(input("How many Employees you want to add :"))
                print("\t")
                for i in range(n):
                    print(f"-Add Employee {i+1} Details:-")
                    emp=Employee()
                    emp.show_employee()
                    employees.append(emp)
            case 3:
                n=int(input("How many Managers you want to add :"))
                print("\t")
                for i in range(n):
                    print(f"-Add Manager {i+1} Details:-")
                    man=Manager()
                    man.show_manager()
                    managers.append(man)
            
            case 4:
                while True:
                    print("---Show Details---")
                    print("1.Person")
                    print("2.Employee")
                    print("3.Manager")
                    print("4.Exit")
                    ch=int(input("Enter your Choice :"))
                    match ch:
                        case 1:
                            if not persons:
                                print("No Person Details stored yet ! please enter data first")
                            else:                          
                                for idx,p in enumerate(persons,start=1):
                                    print(f"Record {idx} :-")
                                    p.p_detail()
                        case 2:
                            if not employees:
                                print("No Employee Details stored yet ! please enter data first")
                            else:
                                for idx,e in enumerate(employees,start=1):
                                    print(f"Record {idx} :-")
                                    e.e_detail()
                        case 3:
                            if not managers:
                                print("No Manager Details stored yet ! please enter data first")
                            else:
                                for idx,m in enumerate(managers,start=1):
                                    print(f"Record {idx} :-")
                                    m.m_detail()
                        case 4:
                            print("Exiting from details Section.")
                            break
                        case _:
                            print("Invalid Choice !")
            case 5:
                print("\t")
                print("Exiting the system. All resources have been freed.")
                print("\t")
                print("Goodbye !")
                print("\t")
                break
            case _:
                print("Invalid Choice. try again !")
menu()



    