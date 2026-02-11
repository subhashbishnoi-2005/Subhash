import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""Dataset Overview
1: passengerId = Unique ID given to each passenger.
2: Survived = Target variable
    0 = Did not survive
    1 = Survived
3: Pclass = Passenger class
    1 = First class
    2 = Second class
    3 = Third clas
4: Name = Name of the passenger.
5: Sex = Gender of the passenger (male / female).
6: Age = Age of the passenger (some values are missing).
7: SibSp = Number of siblings or spouses aboard the Titanic.
8: Parch = Number of parents or children aboard the Titanic.
9: Ticket = Ticket number.
10: Fare = Amount paid for the ticket.
11: Cabin = Cabin number (many missing values).
12: Embarked = Port of embarkation
    C = Cherbourg
    Q = Queenstown
    S = Southampton"""
class Titanic:
    def __init__(self):
        self.container=None
    def load_csv(self):
        self.container=pd.read_csv("train.csv")
        print("\t")
        print("-DataSet Loaded SuccessFully !")
        print("\t")
    def Explore(self):
        if self.container is None:
            print("\t")
            print("-Please Load Datset First !")
            print("\t")
        else:
            print("--Explore DataSet--")
            while True:
                    print("Choose An Operation:")
                    print("1. First 5 Rows from DataSet")
                    print("2. Display Column Name")
                    print("3. Display Data Types ")
                    print("4. Display Basic Info")
                    print("5. Exit")
                    try:
                        e_choice=int(input("Enter Your Choice:-"))

                        match e_choice:
                            case 1:
                                print("First 5 Rows from Data :-\n",self.container.head())
                            case 2:
                                print("Coulmns Name:\n",self.container.columns)
                            case 3:
                                print("Data Types of Coulmns:\n",self.container.dtypes)
                            case 4:
                                print("Basic Information :-\n",self.container.info())
                            case 5:
                                print("\t")
                                print("- Exit From Explore Dataset ")
                                print("\t")
                                break
                    except ValueError:
                        print("\t")
                        print("-Error: Value is not Interger !")
                        print("\t")
    def HandleMissingValue(self):
        if self.container is None:
            print("\t")
            print("-Please Load Datset First !")
            print("\t")
        else:
            while True:
                print("Choose an Option:")
                print("1. Find Missing Value")
                print("2. Find Missing value in Percentage")
                print("3. Drop Null Value")
                print("4. Filling Missing Value ")
                print("5. Exit")
                try:
                    h_choice=int(input("Enter your Choice:"))
                    match h_choice:
                        case 1:
                            print("Misssing value :\n",self.container.isnull().sum())
                        case 2:
                            print("Missing value in Percentage:\n",self.container.isnull().sum()/len(self.container)*100)
                        case 3:
                            print("Rows Before Drop:-",self.container.shape)
                            print("Rows After Drop Null Values:-",self.container.dropna().shape)
                            confirm=input("Are You Sure You want To Drop Null Value (yes):").lower()
                            if confirm == "yes":
                                print("Rows With Null Value droped",self.container.dropna())
                                self.container.dropna(inplace=True)
                                print("Null Values Row Dropped !")
                                print("Rows After Drop Null Value:-",self.container.shape)
                        case 4:
                            print("--Filling Missing Value--")
                            self.container["Age"].fillna(self.container["Age"].mean(),inplace=True)
                            self.container["Cabin"].fillna("Unknown",inplace=True)
                            self.container["Embarked"].fillna(self.container["Embarked"].mode()[0],inplace=True)
                            print("\t")
                            print("Missing Value Filled Successfully !")
                            print("\t")
                        case 5:
                            print("\t")
                            print("- Exit From Handle Missing Value ")
                            print("\t")
                            break
                except ValueError:
                        print("\t")
                        print("-Error: Value is not Interger !")
                        print("\t")
    def Descriptive(self):
        print(self.container.describe())
    
    def Visualization(self):
        print("Choose an Option:-")
        print("1. Survival Count")
        print("2. Survival Vs Gender")
        print("3. Age Distribution")
        print("4. Passanger Class Vs Survival")
        V_choice=int(input("Enter your Choice:"))
        match V_choice:
            case 1:
                print("----Survival Count----")
                sns.countplot(x="Survived", data=self.container)
                plt.title("Survival Count")
                plt.show()
            case 2:
                sns.countplot(x="Sex", hue="Survived", data=self.container)
                plt.title("Survival vs Gender")
                plt.show()
            case 3:
                sns.histplot(self.container["Age"])
                plt.title("Age Distribution")
                plt.show()
            case 4:
                sns.countplot(x="Pclass", hue="Survived", data=self.container)
                plt.title("Passenger Class vs Survival")
                plt.show()


def menu():
    t=Titanic()
    print("Explore Titanic DataSet")
    while True:
        print("Choose an Option:-")
        print("1. Load DataSet")
        print("2. Explore DataSet")
        print("3. Handle Missing Data")
        print("4. Generate Descriptive Statistics")
        print("5. Data Visualization")
        print("6. Exit")
        try:
            choose=int(input("Enter Your Choice:"))
            match choose:
                case 1:
                    t.load_csv()
                case 2:
                    t.Explore()
                case 3:
                    t.HandleMissingValue()
                case 4:
                    t.Descriptive()
                case 5:
                    t.Visualization()
                case 6:
                    print("Exiting the program. GoodBye !")
                    break

        except ValueError:
            print("\t")
            print("-Error: Value is not Interger !")
            print("\t")

menu()
