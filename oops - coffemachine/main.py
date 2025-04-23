from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cc = CoffeeMaker()
mm = MoneyMachine()
menu = Menu()

machine = False

while machine :
    coffee = str(input(f"What would you like? ({menu.get_items()}):"))
    if coffee == "off":
        print("There is no more coffee for you")
        machine = False
    elif coffee == "report":
        print(cc.report())
        print(mm.report())
    else:
        drink = menu.find_drink(coffee)
        if cc.is_resource_sufficient(drink) and  mm.make_payment(drink.cost)  :
            cc.make_coffee(drink)
