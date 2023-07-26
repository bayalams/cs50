expression = input("expression: ")
if len(expression.split(" ")) != 3:
    print("error")
    exit(-1)

x, y, z = expression.split(" ")
