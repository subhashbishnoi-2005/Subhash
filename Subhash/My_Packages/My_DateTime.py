import  datetime
import time
def currentDateTime():
        now=datetime.datetime.now()
        currentDandT=now.strftime("%d-%m-%Y %I:%M:%S %p")
        print(f"Current Date and Time :{currentDandT}")
def differenceTwoDates():
        try:
                first_date = input("Enter First Date (yyyy-mm-dd): ").strip()
                second_date = input("Enter Second Date (yyyy-mm-dd): ").strip()

                d1 = datetime.datetime.strptime(first_date, "%Y-%m-%d")
                d2 = datetime.datetime.strptime(second_date, "%Y-%m-%d")

                diff = d2 - d1
                print(f"Difference: {diff.days} days")
        except ValueError:
                print("Invalid date ! please enter like format.")
def formatDate():
    print("Date Formatting:")
    print("1. DD/MM/YYYY")
    print("2. MM-DD-YYYY")
    print("3. Full date & time")
    print("4. Day name format")

    choice = input("Enter your choice: ")

    now = datetime.datetime.now()
    try:
        choice = int(choice)
    except ValueError:
        print("Error: Please enter a number (1-4)")
        return

    match choice:
        case 1:
            print(f"Date: {now.strftime('%d/%m/%Y')}")
        case 2:
            print(f"Date: {now.strftime('%m-%d-%Y')}")
        case 3:
            print(f"Date & Time: {now.strftime('%Y/%m/%d %H:%M:%S')}")
        case 4:
            print(f"Date: {now.strftime('%A, %B %d, %Y')}")
        case _:
            print("Invalid choice.")

def stop_watch():
        n = int(input("Enter how many seconds to run stopwatch:-"))
        sec = 0
        while True:
                print(f"\rRunning Time: {sec} seconds", end="")
                time.sleep(1)
                sec += 1
                if sec > n:
                        break
        print("Stopwatch stopped!")

def count_down():
    n = int(input("Enter countdown time in seconds: "))
    while n >= 0:
        print(f"\rTime Left: {n} seconds", end="")
        time.sleep(1)
        n -= 1
    print("Countdown finished!")












