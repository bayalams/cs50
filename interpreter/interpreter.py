expression = input("expression: ")
if len(expression.split(" ")) != 3:
    print("error: the input expression should contain two operands and one operator. usage example: 1 + 1.")
    print(f'debug: {expression} {expression.split(" ")}')
    exit(-1)

x, y, z = expression.split(" ")






