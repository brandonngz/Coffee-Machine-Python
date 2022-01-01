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


def assign_resources(choice):
    if choice == "espresso":
        water = MENU[choice]['ingredients']['water']
        coffee = MENU[choice]['ingredients']['coffee']
        return water, coffee
    else:
        water = MENU[choice]['ingredients']['water']
        milk = MENU[choice]['ingredients']['milk']
        coffee = MENU[choice]['ingredients']['coffee']
        return water, milk, coffee


# TODO 4: Check resources sufficient?
def checking_resources(menu_cost_ingredient, resources_left):
    if len(menu_cost_ingredient) > 2:
        if menu_cost_ingredient[0] <= resources_left[0] and menu_cost_ingredient[1] <= resources_left[1] and menu_cost_ingredient[2] <= resources_left[2]:
            return True
        else:
            return False
    else:
        if menu_cost_ingredient[0] <= resources_left[0] and menu_cost_ingredient[1] <= resources_left[1]:
            return True
        else:
            return False


# TODO 6: Check transaction successful?
def check_transaction(q, d, n, p, user_answer):
    quarters = 0.25 * q
    dimes = 0.10 * d
    nickles = 0.05 * n
    pennies = 0.01 * p
    bucks_by_customer = quarters + dimes + nickles + pennies

    coffee_cost = MENU[user_answer]['cost']
    ingredients_portions = assign_resources(user_answer)
    if user_answer == 'espresso':
        if bucks_by_customer >= coffee_cost:
            resources['water'] = resources['water'] - ingredients_portions[0]
            resources['coffee'] = resources['coffee'] - ingredients_portions[1]
            change = bucks_by_customer - coffee_cost
            return f'Here is your change: {change:.2f}', True
        else:
            return False
    if user_answer == 'cappuccino' or user_answer == 'latte':
        if bucks_by_customer >= coffee_cost:
            resources['water'] = resources['water'] - ingredients_portions[0]
            resources['milk'] = resources['milk'] - ingredients_portions[1]
            resources['coffee'] = resources['coffee'] - ingredients_portions[2]
            change = bucks_by_customer - coffee_cost
            return f'Here is your change: {change:.2f}', True
        else:
            return False
# COMPLETE THIS PART.


while True:
    # TODO 1: Prompt user by Asking "What would you like?" (espresso/latte/cappuccino):
    user_input = input("What would you like? (espresso/latte/cappuccino): | admin options: report/off ")

    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
    if user_input == 'off' or user_input == '':
        print("Turning off the machine...")
        break
    # TODO 3: Print report:
    elif user_input == 'report':
        for key, value in resources.items():
            if key == 'coffee':
                print(f'{key}: {value}g')
            else:
                print(f'{key}: {value}ml')
    elif user_input != 'report':
        # Resources_left_machine
        converted = list(resources.values())

        MENU_cost = assign_resources(user_input)
        result = checking_resources(MENU_cost, converted)
        #  True or False answer.
        if result:
            # TODO 5: Process coins.
            quarters = int(input("Insert how many quarters do you want to pay with: $"))
            dimes = int(input("Insert how many dimes do you want to pay with: $"))
            nickles = int(input("Insert how many nickles do you want to pay with: $"))
            pennies = int(input("Insert how many pennies do you want to pay with :$"))
            # TODO 7: Make Coffee.
            change = check_transaction(quarters, dimes, nickles, pennies, user_input)
            if change[1]:
                print(f"Here is your {user_input}, and your {change[0]}")
            else:
                print(f'You have less than the cost of the coffee: {change}')
                break
        else:
            print("We don't have more resources..")
            break



