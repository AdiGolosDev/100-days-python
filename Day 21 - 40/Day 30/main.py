#  This results with traceback error/ no file found:
#  with open("a_file.txt") as file:
#     file.read()

# try:
# except:
# else:
# finally:

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["this key doesn't exist"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally: # not often used, but can be used to execute something despite everything else not working
#     # raise TypeError # can create your own errors
#     raise TypeError("This is an error that I made up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("C'mon man you're not godzilla.")

bmi = weight / height ** 2
print(bmi)
