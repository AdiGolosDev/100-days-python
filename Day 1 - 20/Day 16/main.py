from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

on = True
while on:
    user_choice = input(f"Hello, what drink would you like?:\n{menu.get_items()}\n").lower()

    if user_choice == "off":
        on = False
        break
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif coffee_maker.is_resource_sufficient(menu.find_drink(user_choice)):
        print(f"The cost of {user_choice} is ${menu.find_drink(user_choice).cost}.")
        payment_made = money_machine.make_payment(menu.find_drink(user_choice).cost)
        if payment_made:
            coffee_maker.make_coffee(menu.find_drink(user_choice))
    else:
        print("Sorry, something went wrong.")