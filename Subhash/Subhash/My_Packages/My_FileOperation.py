import os
def CreateFile():
    filename = input("Enter File Name with (.txt): ").strip()
    if filename == "":
        print("Please Enter File Name!")
        return
    with open(filename, "w") as file:
        pass  
    print("File created successfully!")
0
def WriteInFile():
    filename = input("Enter existing file name: ").strip()
    if not os.path.exists(filename):
        print("File does not exist! Please create it first.")
        return
    data = input("Enter data to write: ")
    with open(filename, "w") as f:
        f.write(data)
    print("Data written successfully!")

def ReadFile():
    filename = input("Enter existing file name: ").strip()
    if not os.path.exists(filename):
        print("File does not exist!")
        return
    with open(filename, "r") as f:
        print("File Content:")
        print(f.read())

def AppendFile():
    filename = input("Enter existing file name: ").strip()
    if not os.path.exists(filename):
        print("File does not exist!")
        return
    data = input("Enter data to append: ")
    with open(filename, "a") as f:
        f.write("\n" + data)
    print("Data appended successfully!")

