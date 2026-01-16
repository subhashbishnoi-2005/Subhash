import numpy as np
class NumpyAnalyzer:
    def __init__(self):
        self.arr=None
        print("Welcome to the NumPy Analyzer !")
        print("===============================")
        while True:
            print("Choose An Option:")
            print("1. Create A NumPy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine and Split Arrays")
            print("4. Search,Sort And Filter Arrays")
            print("5. Compute Aggregate and Statistics")
            print("6. Exit !")
            Choice=int(input("Enter your choice:"))
            match Choice:
                case 1:
                    print("Select The Type of Array to Create:")
                    print("1D Array")
                    print("2D Array")
                    print("3D Array")
                    Select=int(input("Enter Your Choice:"))
                    match Select:
                        case 1:
                            try:
                                Enter1d=input("Enter Value Seperated By Space:")
                                self.arr=np.array(Enter1d.split(),dtype=int)
                                print(f"Array Created Successfully:\n {self.arr}")
                            except ValueError:
                                print("Please enter interger value only !")
                            
                            
                        case 2:
                            try:
                                row=int(input("Enter the Number of Rows :"))
                                cols=int(input("Enter the Number of columns :"))
                                m=row*cols
                                Enter=input(f"Enter {m} elements for the array seperated by Space:").split()
                                Enter=[int(x) for x in Enter]
                                self.arr=np.array(Enter).reshape(row,cols)
                                print(f"Array Created Successfilly:\n {self.arr}")
                            except ValueError:
                                print("please enter number how much it ask for !")
                        case 3:
                            try:
                                block=int(input("Enter Blocks:"))
                                rows=int(input("Enter the Number of Rows :"))
                                colss=int(input("Enter the Number of columns :"))
                                multi=block*rows*colss
                                value=input(f"Enter {multi} elements for the array seperated by space:").split()
                                value=[int(y) for y in value]
                                self.arr=np.array(value).reshape(block,rows,colss)
                                print(f"Array Created Successfully:\n {self.arr}")
                            except ValueError:
                                print("please enter number how much it ask for")
                
                case 2:
                    if self.arr is None:
                        print("Create Array First !")

                    print("Choose a Mathematical Opeartion:")
                    print("1. Addition")
                    print("2. Substraction")
                    print("3. Multiplication")
                    print("4. Division")
                    select_M=int(input("Enter your Choice:"))
                    match select_M:
                        case 1:
                            s=self.arr.size
                            enterValueO=input(f"Enter {s} Elements for Operations:").split()
                            enterValueO=[int(s) for s in enterValueO]
                            arrOp=np.array(enterValueO).reshape(self.arr.shape)
                            print("Original Array:\n",self.arr)
                            print("Second Array:\n",arrOp)
                            print("Result of Addition :\n",self.arr + arrOp)
                        case 2:
                            s=self.arr.size
                            enterValueO=input(f"Enter {s} Elements for Operations:").split()
                            enterValueO=[int(s) for s in enterValueO]
                            arrOp=np.array(enterValueO).reshape(self.arr.shape)
                            print("Original Array:\n",self.arr)
                            print("Second Array:\n",arrOp)
                            print("Result of Substraction :\n",self.arr - arrOp)
                        case 3:
                            s=self.arr.size
                            enterValueO=input(f"Enter {s} Elements for Operations:").split()
                            enterValueO=[int(s) for s in enterValueO]
                            arrOp=np.array(enterValueO).reshape(self.arr.shape)
                            print("Original Array:\n",self.arr)
                            print("Second Array:\n",arrOp)
                            print("Result of Multiplication :\n",self.arr * arrOp)
                        case 4:
                            s=self.arr.size
                            enterValueO=input(f"Enter {s} Elements for Operations:").split()
                            enterValueO=[int(s) for s in enterValueO]
                            arrOp=np.array(enterValueO).reshape(self.arr.shape)
                            print("Original Array:\n",self.arr)
                            print("Second Array:\n",arrOp)
                            print("Result of Division :\n",self.arr / arrOp)
                        case _:
                            print("Invalid operation choice!")

                case 3:
                    print("Choose as Option:")
                    print("1. Combine Arrray")
                    print("2. Split Arrray")
                    option=int(input("Enter your choice:"))
                    match option:
                        case 1:
                            if self.arr is None:
                                print("Please enter Array first !")
                            c=self.arr.size
                            newarr=input(f"Enter the elements of Another array to combine ({c} elements seperated by space):").split()
                            newarr=[int(r) for r in newarr]
                            nrr=np.array(newarr).reshape(self.arr.shape)
                            print("Original Array:\n",self.arr)
                            print("Second Array\n",nrr)
                            print("Combined Array(Vertical stack):\n",np.vstack((self.arr,nrr)))

                        case 2:
                            if self.arr is None:
                                print("Please enter Array first !")
                            print("Original array:\n",self.arr)
                            parts=int(input("In how many parts you want to split array:"))
                            split_array=np.split(self.arr,parts)
                            print("Splited Array:\n",split_array)
                case 4:
                    print("Choose an Option:")
                    print("1. Search a Value")
                    print("2. sort the array")
                    print("3. filter values")
                    search=int(input("Enter your choice:"))
                    match search:
                        case 1:
                            print("Original Array:\n", self.arr)
                            searchV = int(input("Enter value to search index of it:"))

                            idx = np.where(self.arr == searchV)

                            if idx[0].size == 0:
                                print(f"{searchV} not found in array")
                            else:
                                if self.arr.ndim == 1:
                                    print(f"Index of {searchV} :", idx[0][0])

                                elif self.arr.ndim == 2: 
                                    print(f"Row index of {searchV} :", idx[0][0])
                                    print(f"Column index of {searchV} :", idx[1][0])

                                elif self.arr.ndim == 3:
                                    print(f"Block index of {searchV} :", idx[0][0])
                                    print(f"Row index of {searchV}   :", idx[1][0])
                                    print(f"Column index of {searchV}:", idx[2][0])
                        case 2:
                            print("Choose an Option:")
                            print("1. Ascending Order ")
                            print("2. Descending Order ")
                            AD=int(input("Enter your Cboice:"))
                            match AD:
                                case 1:
                                    print("Original Array:\n",self.arr)
                                    ascendingO=np.sort(self.arr)
                                    print("Ascending Order:\n",ascendingO)
                                case 2:
                                    print("Original Array:\n",self.arr)
                                    descending = np.sort(self.arr)[::-1]
                                    print("Descending Order:\n",descending)
                        case 3:
                            print("Choose Option:")
                            print("1. Greater than Value")
                            print("2. Less than Value")
                            print("3. Get Even Numbers")
                            print("4. Get Odd Numbers")
                            filt = int(input("Enter your choice:"))
                            print("Original Array:\n", self.arr)
                            match filt:
                                case 1:
                                    val = int(input("Enter value (greater than): "))
                                    print("Filtered Array:\n", self.arr[self.arr > val])

                                case 2:
                                    val = int(input("Enter value (less than): "))
                                    print("Filtered Array:\n", self.arr[self.arr < val])

                                case 3:
                                    print("Even Numbers:\n", self.arr[self.arr % 2 == 0])

                                case 4:
                                    print("Odd Numbers:\n", self.arr[self.arr % 2 != 0])

                                case _:
                                    print("Invalid choice!")
                case 5:
                    print("Choose Option:")
                    print("1. Aggregate")
                    print("2. Statistical")
                    AS=int(input("Enter your choice:"))
                    match AS:
                        case 1:
                            print("Original Array:\n",self.arr)
                            print("Sum Of Array:",np.sum(self.arr))
                            print("Mean Of Array:",np.mean(self.arr))
                            print("Median Of Array:",np.median(self.arr))
                            print("S.D. Of Array:",np.std(self.arr))
                            print("Variance Of Array:",np.var(self.arr))
                        case 2:
                            print("Original Array:\n",self.arr)
                            print("Minimum Value:",np.min(self.arr))
                            print("Maximum Value",np.max(self.arr))
                            print("Correlation of Coefficient:",np.corrcoef(self.arr))
                case 6:
                    print("\t")
                    print("Thank You For using NumPy Analyzer! GoodBye!")
                    print("\t")
                    break
N=NumpyAnalyzer()
print(N)