import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class RetailAnalyzer:
    def __init__(self):
        self.data = None
        print("\t")
        print("==== Retail Sales Data Analyzer ====")

    def loadDataSet(self):
        print("== Load Dataset ==")
        try:
            Ent_F= input("Enter CSV file path (Retail_sales.csv): ").strip()
            self.data = pd.read_csv(Ent_F)
            print("Data Loaded Successfully !")

        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print("Error:", e)

    def exploreData(self):
        if self.data is None:
            print("Please load dataset first")
            return
        print("== Explore Data ==")
        print("1. First 5 Rows")
        print("2. Last 5 Rows")
        print("3. Column Names")
        print("4. Data Types")
        print("5. Dataset Info")
        print("6. Exit")
        while True:
            ch = int(input("Enter your choice: "))
            match ch:
                case 1:
                    print(self.data.head())
                case 2:
                    print(self.data.tail())
                case 3:
                    print(self.data.columns)
                case 4:
                    print(self.data.dtypes)
                case 5:
                    self.data.info()
                case 6:
                    break

    def HandleMissing(self):
        if self.data is None:
            print("Please load dataset first!")
            return
        print("=== Handle Missing Data ===")
        print("1. Show rows with missing values")
        print("2. Fill NUMERIC missing values with mean")
        print("3. Fill CATEGORICAL missing values with mode")
        print("4. Drop rows with missing values")
        print("5. Back")
        while True:
            ch = int(input("Enter choice: "))
            match ch:
                case 1:
                    print(self.data[self.data.isnull().any(axis=1)])
                case 2:
                    self.data["Price"].fillna(self.data["Price"].mean(), inplace=True)
                    self.data["Quantity Sold"].fillna(
                        self.data["Quantity Sold"].mean(), inplace=True
                    )
                    self.data["Total Sales"] = (
                        self.data["Price"] * self.data["Quantity Sold"]
                    )
                    print("Numeric missing values filled with Successfully !")

                case 3:
                    self.data["Product"].fillna(
                        self.data["Product"].mode()[0], inplace=True
                    )
                    self.data["Category"].fillna(
                        self.data["Category"].mode()[0], inplace=True
                    )
                    print("Categorical missing values filled with mode.")
                case 4:
                    self.data.dropna(inplace=True)
                    print("Rows with missing values dropped.")
                case 5:
                    break

    def Descriptive(self):
        if self.data is not None:
            print(self.data.describe())
    def Data_V(self):
        if self.data is None:
            print("Please load dataset first!")
            return
        print("==== Data Visualization ====")
        print("1. Bar Chart")
        print("2. Line Chart")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        ch = int(input("Enter choice: "))
        match ch:
            case 1:
                sns.barplot(data=self.data, x="Category", y="Total Sales")
                plt.title("Total Sales by Category")
                plt.show()
            case 2:
                trend = self.data.groupby("Date")["Total Sales"].sum()
                plt.plot(trend.index, trend.values, marker="o")
                plt.title("Sales Trend Over Time")
                plt.show()
            case 3:
                sns.scatterplot(data=self.data,x="Price",y="Quantity Sold")
                plt.title("Price vs Quantity Sold")
                plt.show()
            case 4:
                pie_data = self.data.groupby("Category")["Total Sales"].sum()
                plt.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%")
                plt.title("Sales Distribution by Category")
                plt.show()
            case 5:
                plt.hist(self.data["Total Sales"], bins=20, edgecolor="black")
                plt.title("Total Sales Distribution")
                plt.show()
def mainM():
    obj = RetailAnalyzer()
    while True:
        print("\n1. Load Dataset")
        print("2. Explore Data")
        print("3. Handle Missing Data")
        print("4. Descriptive Statistics")
        print("5. Data Visualization")
        print("6. Exit")
        choice = int(input("Enter choice: "))
        match choice:
            case 1:
                obj.loadDataSet()
            case 2:
                obj.exploreData()
            case 3:
                obj.HandleMissing()
            case 4:
                obj.Descriptive()
            case 5:
                obj.Data_V()
            case 6:
                print("Goodbye!")
                break
            case _:
                print("Invalid choice")
mainM()
