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

for i in range(0, letter_count):
    password.append(random.choice(letters))

for i in range(0, number_count):
    password.append(random.choice(numbers))

for i in range(0, symbol_count):
    password.append(random.choice(symbols))

print(f"The characters to be used in the password are: {password}\n")

random.shuffle(password)
new_password = ""

for char in password:
    new_password += char

# password_copy = password[:]
#     # copies over entire list
#     # apparently this is a shallow copy, but it doesn't matter since my list doesn't have other lists within it
#     # a = copy.deepcopy(b) does a full copy
#
#
# for x in range(len(password)): # better readibility than previous { for character in password: }
#                                # since character in password doesn't do anything except loop once for every character
#     current = random.choice(password_copy)
#     new_password += current
#     password_copy.remove(current)
#
print(f"Your new randomly generated password is: {new_password}")
