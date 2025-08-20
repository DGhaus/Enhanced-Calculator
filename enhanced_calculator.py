history = []
valid_choice = [1,2,3,4,5,6,7]
print("=== Enhanced Calculator ===")
print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Show History\n6. Clear History\n7. Exit")
choice = int(input("Choose an option (1-7): "))
while choice != 7:
    while choice not in valid_choice:
        print("invalid choice\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Show History\n6. Clear History\n7. Exit")
        choice = int(input("Choose an option (1-7): "))
    if choice == 1:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter  second number: "))

        sum = num_1 + num_2
        history.append(f"{num_1} + {num_2} = {sum}")
        print(f"The answer is: {sum}")
    elif choice == 2:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter  second number: "))

        result = num_1 - num_2
        history.append(f"{num_1} - {num_2} = {result}")
        print(f"The answer is: {result}")
    elif choice == 3:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter  second number: "))

        result = num_1 * num_2
        history.append(f"{num_1} * {num_2} = {result}")
        print(f"The answer is: {result}")
    elif choice == 4:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter  second number: "))
        if num_2 == 0:
            print("numbers aren't divisible by 0")
        else:
            result = num_1 / num_2
            history.append(f"{num_1} / {num_2} = {result}")
            print(f"The answer is: {result}")
    elif choice == 5:
        print("===HISTORY===")
        if history:
            for calculations in history:
                print(calculations)
        else:
            print("There is nothing to show here!")
    elif choice == 6:
        history = []
        print("History Cleared")
    print("=== Enhanced Calculator ===")
    choice = int(input("Choose an option (1-7): "))
    if choice == 7:
        print("Goodbye!")
        exit()