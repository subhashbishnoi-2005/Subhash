print("Welcome to the Student Data Organizer!")
MyList=[]
while True:
    print("Select an option:")
    print("1.Add Student")
    print("2.Display All Students")
    print("3.Update Student Information")
    print("4.Delete Student")
    print("5.Display Subjects Offered")
    print("6.Exit")
    first_choice=int(input("Enter Your Choice:"))
    match first_choice:
        case 1:
            print("---Add Student---")
            NoOfStudent=int(input("How many Student want to Add:"))
            for i in range(NoOfStudent):
                print(f"Enter Student Details {i+1}:")

                ID=int(input("Enter Student ID:"))
                NAME=input("Enter Student Name:")
                AGE=int(input("Enter Student Age:"))
                GRADE=input("Enter Grade:")
                DATE_OF_BIRTH=input("Enter Date of Birth(YYYY-MM-DD):")

                SUBJECTS=[]
                SUB=int(input("How Many Subjects You Want To Enter:"))
                for s in range(SUB):
                    s+=1
                    SUB=input(f"Enter Subject {s} (comma-seperated):")
                    SUBJECTS.append(SUB)

                MyDict={
                    "ID":ID,
                    "NAME":NAME,
                    "AGE":AGE,
                    "GRADE":GRADE,
                    "DATE OF BIRTH":DATE_OF_BIRTH,
                    "SUBJECTS":SUBJECTS
                }

                MyList.append(MyDict)

                print(f"Student {NAME} Added Successfully")
        case 2:
            print("---Display Student---")
            print("Enter Your Choice")
            print("1.Display All Record")
            print("2.Display Record By ID")
            CHOICE=int(input("Enter Your Choice:"))
            match CHOICE:
                case 1:
                    if not MyList:
                        print("NO Record ")
                    else:
                        for i in MyList:
                            if not MyList:
                                print("No Record Found")
                            else:
                                print(f"Student ID: {i.get("ID")} | Name: {i.get("NAME")} | Age: {i.get("AGE")} | Grade: {i.get("GRADE")} | Date Of Birth: {i.get("DATE OF BIRTH")} | Subjects: {" , ".join(i.get("SUBJECTS"))}")
                case 2:
                    if not MyList:
                        print("No Record Found")
                    else:
                        ENTER_ID=int(input("Enter Student ID:"))
                        for i in MyList:
                            if i.get("ID")==ENTER_ID:
                             print(f"Student ID: {i.get("ID")} | Name: {i.get("NAME")} | Age: {i.get("AGE")} | Grade: {i.get("GRADE")} | Date Of Birth: {i.get("DATE OF BIRTH")} | Subjects: {" , ".join(i.get("SUBJECTS"))}")
        case 3:
            if not MyList:
                print("No Record ")
            else:

                print("---Update Student Information---")
                E=int(input("Enter Student ID:"))
                for i in MyList:
                    if i.get("ID")==E:
                        print(f"Record Found Name:{i.get("NAME")}")
                        print("Select Option:-")
                        print("1.Update Name")
                        print("2.Update Age")
                        print("3.Update Grade")
                        print("4.Update Subjects")
                        option=int(input("Enter Your Choice:"))
                        match option:
                            case 1:
                                print("---Update Name---")
                                i["NAME"]=input("Enter New Name:")
                                print("NAME UPDATED SUCCESSFULLY")
                            case 2:
                                print("---Update Age---")
                                i["AGE"]=int(input("Enter AGE:"))
                                print("AGE UPDATED SUCCESFUULY")
                            case 3:
                                print("---Update Grade---")
                                i["GRADE"]=input("Enter Grade:")
                                print("GRADE UPDATED SUCCESSFULLY ")
                            case 4:
                                print("---Update Subjects---")
                                for j in MyList:
                                    if j.get("ID")==E:
                                      j["SUBJECTS"]=input("Enter Subjects(with comma):").split(",")
                                print("SUBJECT UPDATED SUCCESFULLY")
        case 4:
            if not MyList:
                print("No Record")
            else:
                print("---Delete Record---")
                ent_id=int(input("Enter Student ID:"))
                for idx,d in enumerate(MyList):
                    if d.get("ID")==ent_id:
                        print(f"Record Found Name: {d.get("NAME")}")
                        confirm=input("Are You Sure You Want To Delete Record(yes,no): ").lower()

                        if confirm=='yes':
                            del MyList[idx]
                            print(f"Record id:{ID} With Name:{NAME} Deleted Successfully")
                        else:
                            print("No Data Deleted ")
        case 5:
            if not MyList:
                print("No Record")
            else:
                print("---Display Subjects Offered---")
                for s in MyList:
                 print(f"Student Name :{s.get("NAME")} ||  Subjects:{" , ".join(s.get("SUBJECTS"))}")
        case 6:
            print("Exiting ! ")
            break
        case _:
            print("invalid choice! please try again")

                
                                


            

 
            

