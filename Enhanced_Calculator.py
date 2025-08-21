# Importing Modules
import math

# Defining Functions
def get_valid_number(message):
    while True:
        try:
            num = float(input(message))
            return num
        except ValueError:
            print("I think Calculator only works with NUMBERS\nEnter Numbers")
def get_valid_choice(message, valid_list):
            choice = int(get_valid_number(message))
            while choice not in valid_list:
                print("Invalid choice!\nTry Again")
                choice = int(get_valid_number(message))
            return choice
            
# Assigning Variables
history = []
valid_choice = [1,2,3,4,5,6,7,8,9,10]

# Main Calculator
print("=== Enhanced Calculator ===")
menu = '''
1. Add
2. Subtract
3. Multiply
4. Divide
5. Work with Power
6. Work with Roots
7. Work with Percentages
8. Show History
9. Clear History
10. Exit'''
print(menu)
choice = get_valid_choice("Choose an option (1-10): ", valid_choice)
while choice != 10:
    if choice == 1:
        num_1 = get_valid_number("Enter first number: ")
        num_2 = get_valid_number("Enter  second number: ")
        result= round(num_1 + num_2, 2)
        history.append(f"{num_1} + {num_2} = {result}")
        print(f"The answer is: {result}")
    elif choice == 2:
        num_1 = get_valid_number("Enter first number: ")
        num_2 = get_valid_number("Enter  second number: ")
                
        result = round(num_1 - num_2, 2)
        history.append(f"{num_1} - {num_2} = {result}")
        print(f"The answer is: {result}")
    elif choice == 3:
        num_1 = get_valid_number("Enter first number: ")
        num_2 = get_valid_number("Enter  second number: ")
                    
        result = round(num_1 * num_2, 2)
        history.append(f"{num_1} * {num_2} = {result}")
        print(f"The answer is: {result}")
    elif choice == 4:
        num_1 = get_valid_number("Enter first number: ")
        num_2 = get_valid_number("Enter second number: ")
        while num_2 == 0:
            print("Numbers aren't divisible by 0, try again.")
            num_2 = get_valid_number("Enter second number(Again): ")
        result = round(num_1 / num_2, 2)
        history.append(f"{num_1} / {num_2} = {result}")
        print(f"The answer is: {result}")
    elif choice == 5:
        power_choice = get_valid_number("Power Options\n1.Square\n2.Cube\n3.x^y\nChoose 1-3: ")
        if power_choice == 1:
            num_1 = get_valid_number("Enter first number: ")    
            result = round(num_1 ** 2, 2)
            history.append(f"{num_1}^2 = {result}")
            print(f"{num_1}^2 = {result}")
        elif power_choice == 2:
            num_1 = get_valid_number("Enter first number: ")    
            result = round(num_1 ** 3, 2)
            history.append(f"{num_1}^3 = {result}")
            print(f"{num_1}^3 = {result}")
        elif power_choice == 3:
            num_1 = get_valid_number("Enter first number: ")
            num_2 = get_valid_number("Enter second number: ")
            result = round(num_1 ** num_2, 2)
            history.append(f"{num_1}^{num_2} = {result}")
            print(f"{num_1}^{num_2} = {result}")
    elif choice == 6:
        root_choice = get_valid_number("Root Options\n1.Square\n2.Cube\n3.y√x\nChoose 1-3: ")
        if root_choice == 1:
            num_1 = get_valid_number("Enter first number: ")    
            result = round(num_1 ** (1/2), 2)
            history.append(f"√{num_1} = {result}")
            print(f"√{num_1} = {result}")
        elif root_choice == 2:
            num_1 = get_valid_number("Enter first number: ")    
            result = round(num_1 ** (1/3), 2)
            history.append(f"3√{num_1} = {result}")
            print(f"3√{num_1} = {result}")
        elif root_choice == 3:
            num_1 = get_valid_number("Enter x number: ")
            num_2 = get_valid_number("Enter y number: ")    
            result = round(num_1 ** (1/num_2), 2)
            history.append(f"{num_2}√{num_1} = {result}")
            print(f"{num_2}√{num_1} = {result}")
    elif choice == 7:# this is for percentage function
        percent_choice = get_valid_number("Percent Options\n1.Find X% of Y\n2.What percent is X of Y\nChoose 1-2: ")
        if percent_choice == 1:
            num_1 = get_valid_number("Enter x (%): ")
            num_2 = get_valid_number("Enter y ")
            result = round(num_1/100 * num_2, 2)
            history.append(f"{num_1}% of {num_2} = {result}")
            print(f"{num_1}% of {num_2} = {result}")
        elif percent_choice == 2:
            num_1 = get_valid_number("Enter x : ")
            num_2 = get_valid_number("Enter y : ")
            result = round((num_1/num_2) * 100, 2)
            history.append(f"{num_1} is {result}% of {num_2}")
            print(f"{num_1} is {result}% of {num_2}")
            
    elif choice == 8:
        print("===HISTORY===")
        if bool(history):
            for calculations in history:
                print(calculations)
        else:
            print("There is nothing to show here!")
    elif choice == 9:
        history = []
        print("History Cleared")
    print("=== Enhanced Calculator ===")
    print(menu)
    choice = get_valid_choice("Choose an option (1-10): ", valid_choice)
print("Goodbye!")