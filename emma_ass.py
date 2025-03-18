def addition(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero!"
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

def calc():
    print("Welcome to calculation")
    result = None
    while True:
        print("1. Addition\n2. Subtraction\n3. Division\n4. Multiplication")
        choice = input("Please choose an operation (1-4): ")
        
        if result is None:
            try:
                num1 = float(input("First number: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue
        else:
            num1 = result
            print(f"Using previous result: {num1}")
        
        try:
            num2 = float(input("Second number: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if choice == "1":
            result = addition(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == "3":
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        elif choice == "4":
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        else:
            print("Invalid choice!")
            result = None
        
        response = input("Perform another operation? (yes/no): ").lower()
        if response == "no":
            break

calc()