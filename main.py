# ☕ Coffee Machine Program

# Coffee machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

# Menu with ingredients and prices
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}

def print_report():
    """Print current resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")

def is_resource_sufficient(drink):
    """Check if resources are enough to make the drink."""
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Ask the user to insert coins and return total value."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total

def is_transaction_successful(payment, drink_cost):
    """Return True if the payment is enough, handle refund/change."""
    if payment < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(payment - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        resources["money"] += drink_cost
        return True

def make_coffee(drink):
    """Deduct resources and serve the drink."""
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy! ☕")

# Machine loop
machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False
        print("Turning off the coffee machine. Goodbye!")
    elif choice == "report":
        print_report()
    elif choice in MENU:
        if is_resource_sufficient(choice):
            payment = process_coins()
            if is_transaction_successful(payment, MENU[choice]["cost"]):
                make_coffee(choice)
    else:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")
