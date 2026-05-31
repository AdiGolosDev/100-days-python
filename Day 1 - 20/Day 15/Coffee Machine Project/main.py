MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 100,
}

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

initial_money = 100

def print_report():
    for ingredient in resources:
        if ingredient == "money":
            print(f"{ingredient.title()}: ${resources[ingredient]}")
        elif ingredient == "coffee":
            print(f"{ingredient.title()}: {resources[ingredient]}g")
        else:
            print(f"{ingredient.title()}: {resources[ingredient]}ml")

def check_available(drink):
    available = True
    for ingredient in drink["ingredients"]:
        if drink["ingredients"][ingredient] > resources[ingredient]:
            available = False
            print(f"Sorry, there isn't enough {ingredient}\n")
    return available

def pay_for_drink(drink):
    print(f"Please insert the coins needed for the drink: ${drink['cost']}")
    quarters = int(input("How many quarters will you give? ")) * QUARTER
    dimes = int(input("How many dimes will you give? ")) * DIME
    nickels = int(input("How many nickels will you give? ")) * NICKEL
    pennies = int(input("How many pennies will you give? ")) * PENNY
    paid = quarters + dimes + nickels + pennies

    if paid < drink["cost"]:
        print("Sorry, that isn't enough money for the drink. Your money has been refunded.\n")
        return False
    elif paid == drink["cost"]:
        print(f"That is the perfect amount!\n")
        return True
    else:
        print(f"Great, your change is: ${(paid - drink['cost']):.2f}\n")
        return True

def deduct_ingredients(drink):
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]

turned_on = True
while turned_on:
    drink = None
    user_choice = input("What would you like? (espresso, latte, cappuccino): ").lower()
    if user_choice == "espresso":
        drink = MENU["espresso"]
    elif user_choice == "latte":
        drink = MENU["latte"]
    elif user_choice == "cappuccino":
        drink = MENU["cappuccino"]
    elif user_choice == "report":
        print_report()
    elif user_choice == "off":
        turned_on = False
        break
    else:
        print("That's not a valid option")

    if drink is not None:
        if check_available(drink):
            if pay_for_drink(drink):
                print(f"Here is your {user_choice}!")
                deduct_ingredients(drink)
    user_choice = ""
