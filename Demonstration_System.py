# Program demonstrating unused Python keywords with user input

def demo_program():
    # 'as' - Alias import
    import math as m  # 'as' gives an alias to the math module
    print(f"Square root of 16 is: {m.sqrt(16)}")

    # Ask user for a number for the 'break' example
    print("\nExample of 'break':")
    user_num = int(input("Enter a number to break at (between 0 and 10): "))
    for i in range(5):
        if i == user_num:
            print(f"Breaking out of the loop at i = {i}")
            break  # Exits the loop when i is the user's number
        print(i)

    # 'and' - Logical operator
    print("\nExample of 'and':")
    x = int(input("Enter the value for x: "))
    y = int(input("Enter the value for y: "))
    if x < y and y < 30:
        print("Both conditions are true, x is less than y and y is less than 30.")

    # 'continue' - Skip the current iteration of a loop
    print("\nExample of 'continue':")
    for i in range(5):
        if i == 2:
            continue  # Skip the rest of the loop when i is 2
        print(i)

    # 'del' - Delete a variable or item from a collection
    print("\nExample of 'del':")
    my_list = [1, 2, 3, 4]
    print(f"Original list: {my_list}")
    del my_list[int(input('Enter index to delete (0-3): '))]  # Delete by user input
    print(f"List after deletion: {my_list}")

    # 'elif' - Else if for conditional branching
    print("\nExample of 'elif':")
    num = int(input("Enter a number: "))
    if num > 15:
        print("Number is greater than 15.")
    elif num == 10:
        print("Number is exactly 10.")
    else:
        print("Number is less than 10.")

    # 'false' - Python's False (Not directly used, but here's an example)
    print("\nExample of 'False':")
    is_active = False
    if not is_active:
        print("The status is False, so this condition is true.")

    # 'finally' - Used after try-except block
    print("\nExample of 'finally':")
    try:
        result = 10 / int(input("Enter a number to divide 10 by: "))
    except ZeroDivisionError:
        print("Caught division by zero error!")
    finally:
        print("This is the finally block, it always runs after try-except.")

    # 'lambda' - Anonymous function
    print("\nExample of 'lambda':")
    num = int(input("Enter a number to square: "))
    square = lambda x: x ** 2
    print(f"Square of {num} is: {square(num)}")

    # 'None' - Represents no value or a null value
    print("\nExample of 'None':")
    def return_none():
        return None
    result = return_none()
    print(f"Function returned: {result}")

    # 'nonlocal' - Used to modify a variable in an enclosing (but non-global) scope
    print("\nExample of 'nonlocal':")
    def outer():
        count = 0  # Local variable
        def inner():
            nonlocal count  # Modify count in outer's scope
            count += 1
            print(f"Count in inner: {count}")
        inner()
        print(f"Count in outer: {count}")
    outer()

    # 'not' - Logical negation
    print("\nExample of 'not':")
    is_raining = input("Is it raining? (yes/no): ").strip().lower() == 'yes'
    if not is_raining:
        print("It's not raining!")
    else:
        print("It's raining!")

    # 'or' - Logical operator
    print("\nExample of 'or':")
    is_sunny = input("Is it sunny? (yes/no): ").strip().lower() == 'yes'
    is_warm = input("Is it warm? (yes/no): ").strip().lower() == 'yes'
    if is_sunny or is_warm:
        print("Either sunny or warm (or both)")

    # 'pass' - Placeholder for future code
    print("\nExample of 'pass':")
    def empty_function():
        pass  # No operation here, just a placeholder
    empty_function()
    print("Pass keyword allows us to define empty functions or blocks of code.")

    # 'raise' - Raise an exception
    print("\nExample of 'raise':")
    try:
        raise ValueError("An error occurred!")
    except ValueError as e:
        print(f"Caught an exception: {e}")

    # 'return' - Exit function and return a value
    print("\nExample of 'return':")
    def add(x, y):
        return x + y
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = add(num1, num2)
    print(f"The result of adding {num1} and {num2} is: {result}")

    # 'True' - Python's True
    print("\nExample of 'True':")
    is_active = input("Is the system active? (yes/no): ").strip().lower() == 'yes'
    if is_active:
        print("The system is active.")

    # 'while' - A while loop
    print("\nExample of 'while':")
    count = int(input("Enter a number to start counting: "))
    while count < 3:
        print(f"Count is {count}")
        count += 1

    # 'with' - Context manager for handling file operations
    print("\nExample of 'with':")
    with open("example.txt", "w") as file:
        file.write(input("Enter a message to save to a file: ") + "\n")
    print("Message saved to file using 'with' context manager.")

    # 'yield' - Used to turn a function into a generator
    print("\nExample of 'yield':")
    def count_up_to(max):
        count = 1
        while count <= max:
            yield count
            count += 1
    
    max_count = int(input("Enter a number to count up to: "))
    counter = count_up_to(max_count)
    for number in counter:
        print(f"Yielded: {number}")

# It will run the  demonstration program with user input
demo_program()
