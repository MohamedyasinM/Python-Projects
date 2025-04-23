MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0,
}

def choose_coffee(coffee):
    for inc in MENU[coffee]["ingredients"]:
        if resources[inc] <= MENU[coffee]["ingredients"][inc]:
            return "There is no stock left"
    # if resources["water"] < MENU[coffee]["ingredients"]["water"] or resources["milk"] < MENU[coffee]["ingredients"]["milk"] or resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
    #     return "There is no stock left"
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total  = quarters+dimes+nickles+pennies
    anp = 0
    for i in MENU:
        if coffee == i:
            if MENU[i]["cost"] <= total:

                resources["water"] -= MENU[i]["ingredients"]["water"]
                resources["milk"] -= MENU[i]["ingredients"]["milk"]
                resources["coffee"] -= MENU[i]["ingredients"]["coffee"]
                resources["money"] += MENU[i]["cost"]

                print( f"Enjoy your {coffee} thanks")
                anp = total - MENU[i]["cost"]
                return f"here is you balance amount {anp:.2f}"
            else:
                return f"you are giving not enough money so Money refunded {total} of your given money and the prize of the {coffee}  is {MENU[i]["cost"]}"

st = True
while st :
    qn = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    if qn =="report":
        print(f"Water : {resources["water"]}\nmilk : {resources["milk"]}\ncoffee : {resources["coffee"]}\nAmount : {resources["money"]}")
    elif qn =="espresso" or qn=="latte" or qn == "cappuccino":
        ans = choose_coffee(qn)
        print(ans)
    else:
        print("Out ")
        st = False

    print("\n" * 2)