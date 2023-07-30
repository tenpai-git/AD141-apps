#!/usr/bin/python3

# Functions 

def add(num1, num2):
    return print(int(num1) + int(num2))

def multiply(num1, num2):
    return print(int(num1) * int(num2))

def subtract(num1, num2):
    return print(int(num1) - int(num2))

def divide(num1, num2):
    return print(int(num1) / int(num2))

def print_menu():
#    menu = "{0:>4}"
#    menu_list = menu_options.values()
#    print (menu_list)
#    for item in menu_list:
#        print(menu.format(str(item)))
    print(menu_options.items())

# Dictionary of Menu Options
menu_options = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide,
}

print("Calculator Options: ")

for key in menu_options:
    print(f"{str(key):>4}. {menu_options[key].__name__.capitalize()}")

while True:
    choice = input("Select a menu item (or exit): ")
    selected_option = menu_options.get(choice)

#    print(f"Choice is {choice}")
#    print(f"selected_option is {selected_option}")

    if selected_option is not None:
        num1 = input("Select the first number to apply the operation: ")
        num2 = input("Select the second number to apply the operation: ")
        selected_option(num1, num2)

    else:
        print("Exiting.")
        break
