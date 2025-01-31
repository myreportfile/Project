import art
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,

}
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number:"))
    while should_accumulate:
        for symbols in operations:
            print(symbols)
        operation_symbol = input("Choose any symbol:")
        num2 = float(input("What is the second number:"))
        Answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {Answer}")
        choice = input(f"Choose 'y' to continue with previous {Answer} or choose 'n' to restart calculation.")
        if choice == "y":
            num1 = Answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
calculator()







