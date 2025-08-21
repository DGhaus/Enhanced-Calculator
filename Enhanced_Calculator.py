# Enhanced Calculator 🧮
# Author: DGhaus
# Description: A simple Python calculator with history tracking, powers, roots, and percentages.

# ===== Importing Modules =====
import math

# ===== Helper Functions =====
def get_valid_number(message):
    """Keep asking user until a valid number is entered."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("❌ Invalid input! Please enter a NUMBER.")

def get_valid_choice(message, valid_list):
    """Keep asking until the user enters a valid choice from valid_list."""
    choice = int(get_valid_number(message))
    while choice not in valid_list:
        print("❌ Invalid choice! Try again.")
        choice = int(get_valid_number(message))
    return choice

# ===== Calculator Operations =====
def add(history):
    a = get_valid_number("Enter first number: ")
    b = get_valid_number("Enter second number: ")
    result = round(a + b, 2)
    history.append(f"{a} + {b} = {result}")
    print(f"✅ Result: {result}")

def subtract(history):
    a = get_valid_number("Enter first number: ")
    b = get_valid_number("Enter second number: ")
    result = round(a - b, 2)
    history.append(f"{a} - {b} = {result}")
    print(f"✅ Result: {result}")

def multiply(history):
    a = get_valid_number("Enter first number: ")
    b = get_valid_number("Enter second number: ")
    result = round(a * b, 2)
    history.append(f"{a} * {b} = {result}")
    print(f"✅ Result: {result}")

def divide(history):
    a = get_valid_number("Enter first number: ")
    b = get_valid_number("Enter second number: ")
    while b == 0:
        print("❌ Cannot divide by 0. Try again.")
        b = get_valid_number("Enter second number (again): ")
    result = round(a / b, 2)
    history.append(f"{a} / {b} = {result}")
    print(f"✅ Result: {result}")

def power(history):
    choice = int(get_valid_number("Power Options:\n1. Square\n2. Cube\n3. x^y\nChoose 1-3: "))
    if choice == 1:
        x = get_valid_number("Enter number: ")
        result = round(x ** 2, 2)
        history.append(f"{x}^2 = {result}")
        print(f"✅ {x}^2 = {result}")
    elif choice == 2:
        x = get_valid_number("Enter number: ")
        result = round(x ** 3, 2)
        history.append(f"{x}^3 = {result}")
        print(f"✅ {x}^3 = {result}")
    elif choice == 3:
        x = get_valid_number("Enter base (x): ")
        y = get_valid_number("Enter exponent (y): ")
        result = round(x ** y, 2)
        history.append(f"{x}^{y} = {result}")
        print(f"✅ {x}^{y} = {result}")

def root(history):
    choice = int(get_valid_number("Root Options:\n1. Square Root\n2. Cube Root\n3. y√x\nChoose 1-3: "))
    if choice == 1:
        x = get_valid_number("Enter number: ")
        result = round(x ** 0.5, 2)
        history.append(f"√{x} = {result}")
        print(f"✅ √{x} = {result}")
    elif choice == 2:
        x = get_valid_number("Enter number: ")
        result = round(x ** (1/3), 2)
        history.append(f"3√{x} = {result}")
        print(f"✅ 3√{x} = {result}")
    elif choice == 3:
        x = get_valid_number("Enter x: ")
        y = get_valid_number("Enter y: ")
        result = round(x ** (1/y), 2)
        history.append(f"{y}√{x} = {result}")
        print(f"✅ {y}√{x} = {result}")

def percentage(history):
    choice = int(get_valid_number("Percent Options:\n1. Find X% of Y\n2. What percent is X of Y\nChoose 1-2: "))
    if choice == 1:
        x = get_valid_number("Enter X (%): ")
        y = get_valid_number("Enter Y: ")
        result = round((x / 100) * y, 2)
        history.append(f"{x}% of {y} = {result}")
        print(f"✅ {x}% of {y} = {result}")
    elif choice == 2:
        x = get_valid_number("Enter X: ")
        y = get_valid_number("Enter Y: ")
        result = round((x / y) * 100, 2)
        history.append(f"{x} is {result}% of {y}")
        print(f"✅ {x} is {result}% of {y}")

def show_history(history):
    print("\n=== HISTORY ===")
    if history:
        for record in history:
            print(record)
    else:
        print("📭 No history yet!")

def clear_history(history):
    history.clear()
    print("🗑️ History cleared!")

# ===== Main Program =====
def calculator():
    history = []
    menu = """
=== Enhanced Calculator ===
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Roots
7. Percentages
8. Show History
9. Clear History
10. Exit
"""
    valid_choices = list(range(1, 11))

    while True:
        print(menu)
        choice = get_valid_choice("Choose an option (1-10): ", valid_choices)

        if choice == 1: add(history)
        elif choice == 2: subtract(history)
        elif choice == 3: multiply(history)
        elif choice == 4: divide(history)
        elif choice == 5: power(history)
        elif choice == 6: root(history)
        elif choice == 7: percentage(history)
        elif choice == 8: show_history(history)
        elif choice == 9: clear_history(history)
        elif choice == 10:
            print("👋 Goodbye!")
            break

# ===== Run Program =====
if __name__ == "__main__":
    calculator()
