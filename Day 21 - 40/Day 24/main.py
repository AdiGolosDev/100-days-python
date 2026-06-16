# file = open("my_file.txt")

# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt", mode="a") as file:
    # contents = file.read()
    # print(contents)
    file.write("\nNew text again.")

# w mode also creates a new file if one of the corresponding name
# doesn't exist
