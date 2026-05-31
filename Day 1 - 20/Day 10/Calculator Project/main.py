import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

calc = {"+": add,
        "-": subtract,
        "*": multiply,
        "/": divide}

def calculate():
    print(art.logo)
    first = int(input("Please enter the first number: \n"))
    again = True
    while again:
        again = False
        operation = input("Please enter the mathematical operation you would like to use: \n+, -, * or /\n")
        second = int(input("Please enter the second number: \n"))

        result = calc[operation](first, second)
        print(f"The result is {result}\n")

        user_decision = input("Would you like to continue working with the previous result or clear all calculations?\n"
                 "enter 1 for continue\n"
                 "enter 2 for clear\n"
                 "enter anything else for terminating the program\n")
        if user_decision == "1":
            again = True
            first = result
        elif user_decision == "2":
            first = 0
            second = 0
            result = 0
            calculate()
        else:
            return

calculate()
