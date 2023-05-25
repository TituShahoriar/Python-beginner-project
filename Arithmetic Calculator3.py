import operator

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "^": operator.pow
}

def arithmetic_calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose an operation:")
    for symbol in operations:
        print(f"{symbol}")

    operation = input()

    if operation not in operations:
        print("Invalid operation.")
        return

    if operation == "/" and num2 == 0:
        print("Error: Cannot divide by zero.")
        return

    result = operations[operation](num1, num2)

    print(f"{num1} {operation} {num2} = {result}")

arithmetic_calculator()