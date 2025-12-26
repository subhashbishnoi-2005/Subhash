import datetime
import os
def menu():
    j = JournalManager()
    while True:
        print("\t")
        print("\n--- Welcome to Personal Journal Manager ! ---")
        print("\t")
        print("Please Select an Option:-")
        print("\t")
        print("1. Add Journal Entry")
        print("2. View All Entries")
        print("3. Search Entry by Date")
        print("4. Delete All Entries")
        print("5. Exit")

        try:
            choice = int(input("User Input: "))
            match choice:
                case 1:
                    j.takeinput()
                case 2:
                    j.showEnt()
                case 3:
                    j.searchBY_date_Key()
                case 4:
                    j.deleteJournal()
                case 5:
                    j.exit_program()
                    break
                case _:
                    print("Invalid option. Please Select a Valid option from the menu.")

        except ValueError:
            print("Please enter a valid number.")


class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def takeinput(self):
        try:
            entry = input("Enter your journal entry:\n")
            print("\t")

            if entry.strip() == "":
                print("Error: Journal entry cannot be empty.")
                return

            now = datetime.datetime.now()

            currentDate = now.strftime("%d-%m-%Y %I:%M:%S %p")

            with open(self.filename, "a") as file:
                file.write(f"[{currentDate}]\n")
                file.write(entry + "\n\n")
            print("\t")

            print("Entry added successfully!")

        except Exception as e:
            print("Error while adding entry:", e)

    def showEnt(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()

                if content.strip() == "":
                    print("No journal entries found.")
                else:
                    print("\n--- All Journal Entries ---")
                    print(content)

        except FileNotFoundError:
            print("Journal file not found. No entries yet.")
        except Exception as e:
            print("Error while reading entries:", e)

    def searchBY_date_Key(self):
        try:
            search = input("Enter a keyword or date to search: ")

            with open(self.filename, "r") as file:
                found = False
                for i in file:
                    if search in i:
                        print(i.strip())
                        found = True

                if not found:
                    print("No entry found for this date or keyword !")

        except FileNotFoundError:
            print("Journal file not found.")
        except Exception as e:
            print("Error while searching:", e)

    def deleteJournal(self):
        try:
            if not os.path.exists(self.filename):
                print("No journal entries to delete.")
                return
            
            confirm=input("Are you sure you want to delete all entries? (yes/no): ").lower()
            
            if confirm == 'yes':
                os.remove(self.filename)
                print("All journal entries deleted.")
            else:
                print("Delete cancelled.")
        
        except Exception as e:
            print(f"An unexpected error While Deleting : {e}")

    def exit_program(self):
        print("Thank you for using Journal Manager. Goodbye !")

menu()
