import operator

# Define a dictionary of available operations and their corresponding functions
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "^": operator.pow
}

def arithmetic_calculator():
    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Display the available operations
    print("Choose an operation:")
    for symbol in operations:
        print(f"{symbol}")

    # Prompt the user to choose an operation
    operation = input()

    # Check if the chosen operation is valid
    if operation not in operations:
        print("Invalid operation.")
        return

    # Check if it is safe to perform the chosen operation (i.e., not dividing by zero)
    if operation == "/" and num2 == 0:
        print("Error: Cannot divide by zero.")
        return

    # Perform the chosen operation using the function from the operations dictionary
    result = operations[operation](num1, num2)

    # Print out the result
    print(f"{num1} {operation} {num2} = {result}")

# Run the arithmetic calculator
arithmetic_calculator()