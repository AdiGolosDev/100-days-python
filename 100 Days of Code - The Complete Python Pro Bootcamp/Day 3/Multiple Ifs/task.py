print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child ticket: $5.")
        bill = 5
    elif age <= 18:
        print("Student ticket: $7.")
        bill = 7
    else:
        print("Adult ticket: $12.")
        bill = 12

    wants_photo = input("Would you like to take a photo? (y/n)")
    if wants_photo == "y":
        bill += 3

    print("Your bill is: $", bill)

else:
    print("Sorry you have to grow taller before you can ride.")


