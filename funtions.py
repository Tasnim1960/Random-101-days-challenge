def happy_birthday(name,age):
    pi = 3.1416
    print(f"pi to decimal {pi: .3f}")
    print(f"happy birthday {name}")
    print(f"u r {age} years old")
    print("happy birthday to u")

happy_birthday("kaiser",22)

def add(x,y):
    z = x + y
    return z

def subtract(x,y):

    z=x-y
    return z

def devide(x,y):
    z = x/y
    return z
def multi(x,y):
    z=x*y
    return z

print(multi(12,5))
print(subtract(12,5))

def create_name(first,mid, last):
    first = first.capitalize()
    mid = mid.upper()
    last = last.capitalize()
    return first + " "+mid+" "  +last

full_name =create_name("kaiser","von","britton")

print(full_name)

class Car:
    def __init__(self, name:str,color:str, horsepower:int ) ->None:
        self.color = color
        self.name = name
        self.horsepower = horsepower
        self.details = f"{color} horsepower {horsepower}"

scorpio: Car = Car("scorpio","black", 180)
print(scorpio.name)

print(scorpio.details)