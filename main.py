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


def is_resources_sufficient(order_ingredients):
    """Returns false if resources is not sufficient to make the drink and true otherwise"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns total inserted coins"""
    print("Please insert coins")
    quarter = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarter + dimes + nickles + pennies
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return true if payment is accepted, or false if insufficient money"""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change of ${change}")
        return True
    else:
        print("Sorry that’s not enough money. Money refunded.")
        return False


def make_coffee(ordered_drink, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {ordered_drink}")


# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# Check the user’s input to decide what to do next
# The prompt should show every time action has completed, e.g. once the drink is dispensed
# The prompt should show again to serve the next customer

continue_ordering = True
while continue_ordering:
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine.
    # Your code should end execution when this happens
    if user_order == "off":
        continue_ordering = False

    # TODO 3. Print report.
    # When the user enters “report” to the prompt, a report should be generated that shows the current resource values.
    elif user_order == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")


    # TODO 4. Check resources sufficient?
    # When the user chooses a drink, the program should check if there are enough resources to make that drink
    # E.g. if Latte requires 200ml water but there is only 100ml left in the machine.
    # It should not continue to make the drink but print: “Sorry there is not enough water”
    # The same should happen if another resource is depleted, e.g. milk or coffee

    # TODO 5. Process coins.
    # If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
    # Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    # Calculate the monetary value of the coins inserted.
    # E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

    # TODO 6. Check transaction successful?
    # Check that the user has inserted enough money to purchase the drink they selected.
    # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say
    # “Sorry that’s not enough money. Money refunded.”
    # But if the user has inserted enough money, then the cost of the drink gets added to the machine as
    # the profit and this will be reflected the next time “report” is triggered. E.g.

    # TODO 7. Make Coffee.
    # If the transaction is successful and there are enough resources to make the drink the user selected,
    # then the ingredients to make the drink should be deducted from the coffee machine resources.

    else:
        drink = MENU[user_order]
        if is_resources_sufficient(drink["ingredients"]):
            total_coins_inserted = process_coins()
            if is_transaction_successful(total_coins_inserted, drink['cost']):
                make_coffee(user_order, drink['ingredients'])

