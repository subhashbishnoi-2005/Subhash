import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:
    def __init__(self):
        self.data=None
        print("==== Data Analysis & Visualization Program ====")
    def __del__(self):
        print("Program Closed")
    def loadDataSet(self):
        print("== Load Dataset ==")
        try:
            L=input("Enter the path of Dataset (MySalesRecord.csv) :").strip()
            self.data=pd.read_csv(L)
            print("Dataset Loaded Successfully !")
        except FileNotFoundError:
            print("Error : File not Found.")
    def exploreData(self):
        if self.data is None:
            print("\t")
            print("Please Load Dataset First")
            print("\t")
            return
        try:
            print("== Explore Data ==")
            print("1. Display the First 5 Rows")
            print("2. Display the Last 5 Rows")
            print("3. Display Column Name")
            print("4. Display Data Types ")
            print("5. Display Basic Info")
            print("6. Exit")
            while True:
                e_Choice=int(input("Enter your Choice:"))
                match e_Choice:
                    case 1:
                        record=self.data
                        r=pd.DataFrame(record).head(5)
                        print("First 5 Record :\n",r)
                    case 2:
                        record=self.data
                        r=pd.DataFrame(record).tail(5)
                        print("Last 5 Record :\n",r)
                    case 3:
                        record=self.data
                        r=pd.DataFrame(record).columns
                        print("Columns :-\n",r)
                    case 4:
                        record=self.data
                        r=pd.DataFrame(record).dtypes
                        print("Data Types:-\n",r)
                    case 5:
                        self.data.info()
                    case 6:
                        print("\t")
                        print("Exiting the Explore Data")
                        print("\t")
                        break
        except FileNotFoundError:
            print("Error: File Not Found.")
    def performOp(self):
        if self.data is None:
            print("Please load dataset first!")
            return
        print("=== Perform DataFrame Operations ===")
        print("Please select option:")
        print("1. Sort Data by Sales")
        print("2. Filter Sales Greater Than Value")
        ch = int(input("Enter your choice: "))
        match ch:
            case 1:
                print(f"Sorting data by sales:\n{self.data.sort_values("Sales",ascending=False)}")
            case 2:
                ent_val=int(input("Enter value to get Greater than :"))
                print(self.data[self.data["Sales"]>ent_val])
    def HandleMissing(self):
        if self.data is None:
            print("\t")
            print("Please Load dataset first !")
            print("\t")
            return
        print("=== Handle Missing Data ===")
        print("1. Display Row with Missing Values")
        print("2. Fill Missing Value with Mean")
        print("3. Drop rows with missing values")
        print("4. Replace Missing value with a Specific Value")
        print("5. back ")
        while True:
            Ent_H=int(input("Enter your Choice:"))
            match Ent_H:
                case 1:
                    
                    print(f"Rows with Missing Value:\n {self.data[self.data.isnull().any(axis=1)]}")
                    
                case 2:
                    self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
                    print("Missing values filled with mean !")
                case 3:
                    self.data.dropna(inplace=True)
                    print("Null Values Row Dropped !")
                case 4:
                    valuee=input("Enter a value to replace with Null value:")
                    self.data.fillna(valuee,inplace=True)
                    print("\t")
                    print(f"Missing Value Replaced With {valuee}.")
                    print("\t")
                case 5:
                    print("Back from the Missing data Handle ")
                    break
    def Descriptive(self):
        print(self.data.describe())
    def Data_V(self):
        if self.data is None:
            print("Please load dataset first!")
            return
        print("==== Data Visualization ====")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Plot")
        print("5. Histogram Plot")
        Ent_v=int(input("Enter Your Choice: "))
        match Ent_v:
            case 1:
                sns.barplot(data=self.data, x="Region", y="Sales")
                plt.title("Total Sales by Region")
                plt.xlabel("<------------Region------------>")
                plt.ylabel("<------------Sales------------>")
                plt.show()
            case 2:                
                sns.lineplot(data=self.data, x="Year", y="Sales", marker="o")
                plt.title("Sales Trend by Year")
                plt.xlabel("<------------Year------------>")
                plt.ylabel("<------------Sales------------>")
                plt.show()
            case 3:
                sns.scatterplot(data=self.data, x="Year", y="Sales")
                plt.title("Year vs Sales")
                plt.xlabel("<------------Year------------>")
                plt.ylabel("<------------Sales------------>")
                plt.show()
            case 4:
                pie_data = self.data.groupby("Product")["Sales"].sum()
                plt.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%")
                plt.title("Sales Distribution by Product")
                plt.show()
            case 5:
                plt.hist(self.data["Sales"], bins=10, edgecolor="Black")
                plt.title("Sales Distribution")
                plt.xlabel("<------------Sales------------>")
                plt.ylabel("<------------Frequency------------>")
                plt.show() 
    def saveV(self):
        if self.data is None:
            print("Please load dataset first!")
            return

        print("== Save Visualization ==")
        file_name=input("Enter file name to save the plot (ex:- scatter_plot.png ): ")
        try:
            plt.savefig(file_name)
            print(f"Visualization saved as {file_name} successfully!")
        except Exception as e:
            print("Error while saving visualization:", e)
def mainM():
    obj=SalesDataAnalyzer()
    while True:
        print("Please Select an Option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")

        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                obj.loadDataSet()
            case 2:
                obj.exploreData()
            case 3:
                obj.performOp()
            case 4:
                obj.HandleMissing()
            case 5:
                obj.Descriptive()
            case 6:
                obj.Data_V()
            case 7:
                obj.saveV()

            case 8:
                print("Exiting the program. GoodBye !")
                break
            case _:
                print("Invalid choice")
mainM()