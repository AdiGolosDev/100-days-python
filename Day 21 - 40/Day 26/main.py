# list comprehension
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers] # [new_item for item in list]
print(new_list)

name = "Klokan"
letters_list = [letter for letter in name]
print(letters_list)

new_num_list = [number * 2 for number in range(1, 5)]
print(new_num_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_cap_names = [name.upper() for name in names if len(name) > 4]
print(long_cap_names)
