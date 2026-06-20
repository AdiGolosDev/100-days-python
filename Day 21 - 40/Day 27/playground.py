# unlimited args *args
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2,3,4,5,6,7,8,9,10,1))

# key-word arguments kwargs
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    
    def __init__(self, **kw):
        self.make = kw.get("make") # better to use kw.get("something") instead of kw["something"] because get returns none if not found
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)
