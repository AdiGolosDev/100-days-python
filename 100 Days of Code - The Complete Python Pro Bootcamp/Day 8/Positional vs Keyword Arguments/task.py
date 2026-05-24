# Functions with input

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"What is it like in {location}?")

greet_with_name("Jack Bauer", "Germany")

def multiple_inputs(a, b, c):
    print(f"This function prints out three different things:\nfirst: {a}\nsecond: {b}\nthird: {c}")

multiple_inputs("string", 2, 3.3253)

greet_with_name(location="Japan", name="Ado")