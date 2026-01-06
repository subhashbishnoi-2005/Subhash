main_list=[]
def menu():
    print("\t")
    print("Welcome to the Data Analyzer and Transformer Program")
    print("\t")
    while True:
        print("Main Menu:")
        print("1. Input Data")
        print("2. Display Data Summery")
        print("3. Calculate Factorial ")
        print("4. Filter Data by threshold ")
        print("5. Sort Data ")
        print("6. Display DataSet Statistics ")
        print("7. Exit Program")
        choice=int(input("Please Enter your Choice :"))
        match choice:
            case 1:
                print("select input Type:")
                print("1. 1D list")
                print("2. 2D list")
                select=int(input("Select an Option :"))
                match select:
                    case 1:
                        Fun_1D()
                    case  2:
                        Fun_2D()
                    case _:
                        print("Please Select from 1 or 2.")
            case 2:
                display()
            case 3:
                print("\t")
                while True:
                    f=int(input("Enter a Number to Calculate it's Factorial: "))
                    if f < 0:
                        print("Please enter a number >=0 ")
                    else:
                     print(f"-Factorail of {f} is :",factorial(f))  
                     break  
            case 4:
                fun_filter()  
            case 5:
                sorting()
            case 6:
                 result = return_Multipe()
                 if result:  
                        min_val, max_val, total, avg = result
                        print("Dataset Statistics:")
                        print("- Minimum Value :", min_val)
                        print("- Maximum Value :", max_val)
                        print("- Sum of Values :", total)
                        print("- Average Value :", avg)
            case 7:
                print("Thankyou for using Data Analyzer and Transformer Program. Goodbye !")
                break
            case _:
                print("Invalid choice ! try again ")
def Fun_1D():
    global main_list
    Enter_1d=input("Enter Data for 1D array (seperated by space) :")
    main_list=[int(x) for x in Enter_1d.split()]
    print("1d data stored successfully !")
    print("your data :",main_list)
def Fun_2D():
    global main_list
    row=int(input("enter number of rows for 2d list:"))
    matrix=[]
    for i in range(row):
       row_input=input(f"Rows {i+1} (seperated by space):")
       row=[int(x) for x in row_input.split()]
       matrix.append(row)

    main_list=matrix
    print("2d data stored successfully !")
    print("Your 2D data:",main_list)


def display():
    global main_list
    if not main_list:
        print("No data stored yet ! Please enter data first.")
        return
    if isinstance(main_list[0],list):
        print("2D Data Summery:-")
        rows=len(main_list)
        cols=len(main_list[0])
        print("-Total Rows:",rows)
        print("-Total Columns:",cols)
        check=[x for row in main_list for x in row]
        print("-Total Element :",len(check))
        print("-Minimum Value :",min(check))
        print("-Maximum Value :",max(check))
        print("-Sum of Values :",sum(check))
        avg=sum(check)/len(check)
        print("-Average Value:",avg)
    else:
        print("1D Data Summery:-")
        print("-Total Elements :",len(main_list))
        print("-Minimum Value :",min(main_list))
        print("-Maximum Value :",max(main_list))
        print("-Sum of All Value :",sum(main_list))
        avg=sum(main_list)/len(main_list)
        print("-Average Value:",avg)  
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

def fun_filter():
    global main_list
    if not main_list:
        print("No Data stored yet ! please enter data first.")
        return
    threshold=int(input("Enter a threshold value :"))
    if isinstance(main_list[0],list):
        print("Filtering 2d list:-")
        flat=[x for row in main_list for x in row]
        filtering=list(filter(lambda x: x >=threshold,flat))
        print(f"Filtered Data (value >= {threshold}):{filtering}")
    else:
        print("Filtering 1D list :-")
        filtering=list(filter(lambda x: x >=threshold,main_list))
        print(f"Filtered Data (value >= {threshold}):{filtering}")

def sorting():
    global main_list
    if not main_list:
        print("No data stored yet! Please enter data first.")
        return
    print("Choose Sorting Option:")
    print("1. Ascending")
    print("2. Descending")
    ch = int(input("Enter your choice : "))

    match ch:
        case 1:   
            if isinstance(main_list[0], list):
                print("Sorting 2D list in Ascending order:-")
                flat = [x for row in main_list for x in row]
                sorted_list = sorted(flat)
                print("Sorted 2D Data:", sorted_list)
            else:
                print("Sorting 1D list in Ascending order:-")
                sorted_list = sorted(main_list)
                print("Sorted 1D Data:", sorted_list)
        case 2:  
            if isinstance(main_list[0], list):
                print("Sorting 2D list in Descending order:-")
                flat = [x for row in main_list for x in row]
                sorted_list = sorted(flat, reverse=True)
                print("Sorted 2D Data:", sorted_list)
            else:
                print("Sorting 1D list in Descending order:-")
                sorted_list = sorted(main_list, reverse=True)
                print("Sorted 1D Data:", sorted_list)
        case _:
            print("Invalid Sorting Choice!")
def return_Multipe():
    global main_list
    if not main_list:
        print("No data stored yet! Please enter data first.")
        return 
    if isinstance(main_list[0], list):
        flat = [x for row in main_list for x in row]
        min_val = min(flat)
        max_val = max(flat)
        total = sum(flat)
        avg = total / len(flat)
        return min_val, max_val, total, avg
    else:
        min_val = min(main_list)
        max_val = max(main_list)
        total = sum(main_list)
        avg = total / len(main_list)
        return min_val, max_val, total, avg
menu()            
