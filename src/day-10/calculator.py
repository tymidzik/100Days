from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def subtract(n1, n2):
    return n1 - n2


operations = {
    "+": add,
    "*": multiply,
    "/": divide,
    "-": subtract
}


def calculator():
    num1 = float(input("What is the first number?\n"))

    go = True
    while go:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation:\n")
        num2 = float(input("What is the next number?\n"))

        operation = operations[operation_symbol]
        answer = operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        to_continue = input(
            f"Type 'y' to continue calculating with {answer} or 'n' to exit. To start a new operation press 'o'\n")
        if to_continue == "n":
            go = False
        elif to_continue == "o":
            go = False
            calculator()
        else:
            num1 = answer


calculator()
