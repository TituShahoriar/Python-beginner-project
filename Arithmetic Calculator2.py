def arithmetic_calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")

    operation = int(input())

    if operation == 1:
        result = num1 + num2
        symbol = "+"
    elif operation == 2:
        result = num1 - num2
        symbol = "-"
    elif operation == 3:
        result = num1 * num2
        symbol = "*"
    elif operation == 4:
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
        symbol = "/"
    elif operation == 5:
        result = num1 % num2
        symbol = "%"
    elif operation == 6:
        result = num1 ** num2
        symbol = "^"
    else:
        print("Invalid operation.")
        return

    print(f"{num1} {symbol} {num2} = {result}")

arithmetic_calculator()