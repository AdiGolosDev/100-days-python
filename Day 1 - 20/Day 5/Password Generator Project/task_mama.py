import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letter_count = int(input("How many letters would you like in your password?\n"))
number_count = int(input(f"How many numbers would you like?\n"))
symbol_count = int(input(f"How many symbols would you like?\n"))

password = []
for lc in range(0,letter_count):
    password.append(random.choice(letters))
for nc in range(0,number_count):
    password.append(random.choice(numbers))
for sc in range(0,symbol_count):
    password.append(random.choice(symbols))

random.shuffle(password)

new_password = ""
for i in password:
    new_password += i

print(new_password)

