print("Welcome to the Pattern Generator and Number Analyzer!")
while True:
    print("Select an Option:")
    print("1. Generate a Pattern(Right Angled Triangle)")
    print("2. Analyze a Range of Numbers ")
    print("3. Exit ")
    select=int(input("Enter Your Choice: "))
    match select:
        case 1:
            rows=int(input("Enter the number of rows for the pattern:"))
            if rows>0:
                for i in range(1,rows):
                    for j in range(1,i+1):
                        print("*",end=" ")
                    print()
            else:
                print("Invalid number !")
                break
        case 2:
            start=int(input("Enter the Start of the Range: "))
            end=int(input("Enter the end of the Range: "))
            sum=0
            for i in range(start,end):
                sum+=i
                if i%2==0:
                    print(f"Number {i} is Even")
                elif i < 0:
                     pass
                else:
                    print(f"Number {i} is Odd")
            print(f"Sum of all numbers from {start} to {end-1} is:",sum)
        case 3:
            print("Exiting the program. Goodbye !")
            break
