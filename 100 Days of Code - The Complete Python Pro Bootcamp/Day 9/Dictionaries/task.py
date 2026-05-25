programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over and over again",
                          }

print(programming_dictionary["Bug"])

# can be used to edit existing entries as well
programming_dictionary["Error"] = "Something that appears from time to time and you hate it, but it's actually your best friend"

print(programming_dictionary["Error"])

empty_dictionary = {}

#Looping through dictionaries
for key in programming_dictionary:
    print(key) #prints out key
    print(programming_dictionary[key]) #prints out key's value
