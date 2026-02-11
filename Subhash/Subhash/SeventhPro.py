from My_Packages import My_DateTime,My_Uuid,My_FileOperation
from My_Packages import My_Maths,My_RandomDataGen,my_Mattribute
class MultyUtilityKit:
    def __init__(self):
        print("===========================")
        print("Welcome to Multi-Utility Toolkit")
        print("===========================")
        while True:
            print("Choose an Option :")
            print("1. Datetime And Time Operations")
            print("2. Mathematical Operations")
            print("3. Random Data Generation")
            print("4. Generate Unique Identifiers (UUID)")
            print("5. File Operations (Custom Module)")
            print("6. Explore Module Attributes (dir())")
            print("7. Exit")
            print("===========================")
            try:
                choice=int(input("Enter Your Choice :"))
                match choice:
                    case 1:
                         print("Date and Time Operations:")                       
                         print("1. Display current Date and Time ")
                         print("2. Calculate difference between Two Dates/Times")
                         print("3. Format Date into Custom format")
                         print("4. Stopwatch")
                         print("5. Countdown Timer")
                         print("6. Back to Main Menu")
                         while True:
                          try:
                            choiceD=int(input("Enter Your Choice:"))
                            match choiceD:
                                case 1:
                                    print("\t")
                                    My_DateTime.currentDateTime()
                                    print("==================================")
                                
                                case 2:
                                    print("\t")
                                    My_DateTime.differenceTwoDates()
                                    print("==================================")
                                case 3:
                                    print("\t")
                                    My_DateTime.formatDate()
                                    print("======================================")
                                case 4:
                                    print("\t")
                                    My_DateTime.stop_watch()
                                    print("==================================")
                                case 5:
                                    print("\t")
                                    My_DateTime.count_down()
                                    print("==================================")
                                case 6:
                                    print("Exiting Date and Time Operations !")
                                    break
                          except ValueError:
                            print("Please enter Valid Number")

                    case 2:
                      print("Mathematical Operations:")
                      print("1. Calculate Factorial")
                      print("2. Solve Compound Interest")
                      print("3. Trigonometirc Calculations")
                      print("4. Area Of Geomatric Shapes")
                      print("5. Back to the Main Menu")
                      while True:
                          try:
                            choiceM=int(input("Enter Your Choice:"))
                            match choiceM:
                                case 1:
                                    print("\t")
                                    My_Maths.my_factorial()
                                    print("==================================")
                                
                                case 2:
                                    print("\t")
                                    My_Maths.CompoundInt()
                                    print("==================================")
                                case 3:
                                    print("\t")
                                    My_Maths.trigno()
                                    print("==================================")
                                case 4:
                                    print("\t")
                                    My_Maths.areaofshape()
                                    print("==================================")

                                case 5:
                                    print("Exiting Mathematical Operations !")
                                    break
                          except ValueError:
                            print("Please enter Valid Number")
                    case 3:
                      print("Random Data Generation:")
                      print("1. Generate Random Number")
                      print("2. Generate Random List")
                      print("3. Create Random Password")
                      print("4. Generate Random OTP")
                      print("5. Back to the Main Menu")
                      while True:
                          try:
                            choiceM=int(input("Enter Your Choice:"))
                            match choiceM:
                                case 1:
                                    print("\t")
                                    My_RandomDataGen.RandomNum()
                                    print("==================================")
                                
                                case 2:
                                    print("\t")
                                    My_RandomDataGen.RandomList()
                                    print("==================================")

                                case 3:
                                    print("\t")
                                    My_RandomDataGen.RandomPass()
                                    print("==================================")
                                
                                case 4:
                                    print("\t")
                                    My_RandomDataGen.RandomOTP()
                                    print("==================================")
                                  
                                case 5:
                                    print("Exiting Random Data Generation !")
                                    break
                          except ValueError:
                            print("Please enter Valid Number")
                    case 4:
                      print("\t")
                      print("Generate Unique Identifiers:")
                      print("\t")
                      My_Uuid.UniqueID()
                      print("\t")
                    
                    case 5:
                      print("File Operations")
                      print("1. Create a New File")
                      print("2. Write to a File")
                      print("3. Read From a File")
                      print("4. Append to a File")
                      print("5. Back to Main Menu")
                      while True:
                          try:
                            choiceM=int(input("Enter Your Choice:"))
                            match choiceM:
                                case 1:
                                    print("\t")
                                    My_FileOperation.CreateFile()
                                    print("==================================")
                                
                                case 2:
                                    print("\t")
                                    My_FileOperation.WriteInFile()
                                    print("==================================")

                                case 3:
                                    print("\t")
                                    My_FileOperation.ReadFile()
                                    print("==================================")
                                
                                case 4:
                                    print("\t")
                                    My_FileOperation.AppendFile()
                                    print("==================================")
                                  
                                case 5:
                                    print("Exiting File Operation !")
                                    break
                          except ValueError:
                            print("Please enter Valid Number")

                    case 6:
                      print("Explore Module Attributes:") 
                      pass
                      
                    case 7:
                        print("Thank You For Using the Multi-Utility Toolkit !")
                        break
            except ValueError:
             print("Please Enter a Valid Number ")
m=MultyUtilityKit()
print(m)
