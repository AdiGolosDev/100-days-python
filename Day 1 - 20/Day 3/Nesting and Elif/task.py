print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you? "))
    #seniors and children pay $5, <=18 pay 10, else pay 15
    if age <= 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $10")
    elif age >= 70:
        print("Please pay $5")
    else:
        print("Please pay $15")
else:
    print("Sorry you have to grow taller before you can ride.")
