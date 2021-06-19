from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = Menu()
money = MoneyMachine()
coffee_maker = CoffeeMaker()

coffee_available = True
while coffee_available:
    print('''

   _____         __   __              __  __         _
  / ____|       / _| / _|            |  \/  |       | |
 | |      ___  | |_ | |_  ___   ___  | \  / |  __ _ | | __ ___  _ __
 | |     / _ \ |  _||  _|/ _ \ / _ \ | |\/| | / _` || |/ // _ \| '__|
 | |____| (_) || |  | | |  __/|  __/ | |  | || (_| ||   <|  __/| |
  \_____|\___/ |_|  |_|  \___| \___| |_|  |_| \__,_||_|\_\\___||_|



    ''')
    print("Welcome to the coffee maker.\nEnter your choice of coffee from the given option to get it.")
    option = coffee.get_items()
    choice = input(f" What would you like? ({option}):").lower()
    if choice == "off":
        coffee_available = False
    elif choice == "report":
        coffee_maker.report()
        money.report()
    else:
        drink = coffee.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
