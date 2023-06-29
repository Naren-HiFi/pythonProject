# TODO: 1. Create the coffee menu that includes the costs and resources that are needed to prepare coffee
# Complete Code

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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: Create a global varaible with init value 0 to modify the value to calculate the cost.
profit = 0

# TODO: 2. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
continue_serve_coffee = False


def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if (order_ingredients[item] > resources[item]):
            print(f'“ Sorry there is not enough {item}')
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25;
    total += int(input("How many dimes?: ")) * 0.10;
    total += int(input("How many nickels?: ")) * 0.05;
    total += int(input("How many pennies?: ")) * 0.01;
    return total
def is_transaction_successful(money_received,drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

while not continue_serve_coffee:
    coffee_machine_user_input = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 3. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if coffee_machine_user_input == 'off':
        continue_serve_coffee = True

    # TODO: 4. Print report of all the coffee machine resources
    elif coffee_machine_user_input == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Water: {resources["coffee"]}g')
        print(f'Money: ${profit}')

    else:
        drink = MENU[coffee_machine_user_input]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(coffee_machine_user_input,drink["ingredients"])



    # if coffee_machine_user_input == 'report':
    #     money = 0
    #     for key in MENU:
    #
    #         if key == 'espresso':
    #             print(f'Money: ${MENU[key].get("cost")}')
    #         elif key == 'latte':
    #             print(f'Money: ${MENU[key].get("cost")}')
    #         elif key == 'cappuccino':
    #             print(f'Money: ${MENU[key].get("cost")}')
    #         else:
    #             print(f'Money: ${money}')

# TODO: 5. Check whether the resources are sufficient to make drink order.

"""
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
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
ssf

def is_resource_sufficient(order_ingredients):
   
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
  
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
   
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

# Completed

"""
# Done