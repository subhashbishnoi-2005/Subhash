import random
import string
def RandomNum():
    NUM=random.randint(1, 101)
    print("Random Number :-",NUM)


def RandomList():
    n = int(input("Enter list size: "))
    my_list = [random.randint(1, 100) for i in range(n)]
    print(" List:-", my_list)



def RandomPass():
    p = int(input("Enter password length: "))
    password = ""
    for i in range(p):
        password += random.choice(string.ascii_letters + string.digits)
    print("Generated Password:", password)

def RandomOTP():
    Otp=""
    for i in range(4):
        Otp += random.choice(string.digits)
    print("OTP:-",Otp)


