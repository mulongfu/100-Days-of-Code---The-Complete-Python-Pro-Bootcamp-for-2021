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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

not_end = True
total_money = 0


def check_enough_money(choice, coins):
    return round(sum(coins) - MENU[choice]["cost"], 2)


def resource_is_enough(choice):
    for i in MENU[choice]["ingredients"]:
        if resources[i] < MENU[choice]["ingredients"][i]:
            return False, i
    return True, 0


while not_end:

    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${total_money}")
        continue

    elif choice == "off":
        not_end = True

    else:
        resource_enough, resource = resource_is_enough(choice)
        if resource_enough:
            print("Please insert coins.")
            quarter = float(input("how many quarters?: ")) * 0.25
            dimes = float(input("how many dimes?: ")) * 0.1
            nickles = float(input("how many nickles?: ")) * 0.05
            pennies = float(input("how many pennies?: ")) * 0.01

            user_coins_change = check_enough_money(
                choice, [quarter, dimes, nickles, pennies]
            )

            if user_coins_change < 0:
                print("Sorry that's not enough money. Money refunded.")

            else:
                print(f"Here is ${user_coins_change} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")
                total_money += MENU[choice]["cost"]
                for i in MENU[choice]["ingredients"]:
                    resources[i] -= MENU[choice]["ingredients"][i]
        else:
            print(f"Sorry there is not enough {resource}.")
