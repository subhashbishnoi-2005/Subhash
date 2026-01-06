import math
def my_factorial():
    Ent_Num=int(input("enter a number Whose Factorial you Want:"))
    print(f"Factorial:{math.factorial(Ent_Num)}")


def CompoundInt():
    amt=float(input("Enter Principal Amount :"))
    Rate_Of_Int=float(input("Enter Rate Of Interest (in %) :"))
    Duration=int(input("Enter Time (in years) :"))
    final_Amt=amt*(1+Rate_Of_Int/100)**Duration
    print(f"Compound Interest :{final_Amt}")


def trigno():
    Ent_angle=float(input("Enter the number in degree :"))
    radians=math.radians(Ent_angle)
    print(f"Degree {Ent_angle} sin is :{math.sin(radians)}")
    print(f"Degree {Ent_angle} cos is :{math.cos(radians)}")
    print(f"Degree {Ent_angle} tan is :{math.tan(radians)}")

def areaofshape():
        n = float(input("Enter value: "))
        print("Area of Circle:", round(math.pi * n * n, 2))
        print("Area of Square:", n * n)
        print("Area of Rectangle:", n * n)
        print("Area of Triangle:", 0.5 * n * n)

def Area_Circle():
    r=int(input("Enter radius:"))
    area = math.pi * r ** 2
    print(f"Area of circle: {area}")
def Area_rect():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print(f"Area of rectangle: {area}")

def Area_Tri():
        b = float(input("Enter base : "))
        h = float(input("Enter height : "))
        area = 0.5 * b * h
        print(f"Area of triangle: {area}")
def Square():
     s=float(input("Enter Num:"))
     sq=s*s
     print(f"Square of num is:{sq}")
def areaofshape():
        print("Area Of Geomatric Shapes")
        print("1. Area of Circle")
        print("2. Area of Rectangle")
        print("3. Area of Triangle")
        print("4. Square ")
        print("5. Exit from Area of Geomatric")
        while True:
            Geo=int(input("Enter Your Choice:"))
            match Geo:
                 case 1:
                      Area_Circle()
                 case 2:
                      Area_rect()
                 case 3:
                      Area_Tri()
                 case 4:
                      Square()
                 case 5:
                      print("Exit")
                      break
