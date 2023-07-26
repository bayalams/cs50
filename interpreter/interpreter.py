expression = input("expression: ")
if len(expression.split(" ")) != 3:
    print("error: the input expression should contain two operands and one operator. usage example: 1 + 1.")
    print(f'debug: {expression} {expression.split(" ")}')
    exit(-1)

list_expression = expression.split(" ")
print(list_expression)

x = list_expression[0]
y = list_expression[1]
z = list_expression[2]

print(x)
print(y)
print(z)

if x.isnumeric() != True:
    print('x must be a numeric character. For example: 1, 3.1, 1999')
    print(f'debug: {x}')
    exit(-1)

if y not in ['+', '-', '*', '/']:
    print('y must be an operator. For example: +, -, *, /')
    print(f'debug: {y}')
    exit(-1)

if z.isnumeric() != True:
    print('z must be a numeric character. For example: 1, 3.1, 1999')
    print(f'debug: {z}')
    exit(-1)

x = float(x)
z = float(z)

if y == '+':
    print(x + z)
elif y == '-':
    print(x - z)
elif y == '*':
    print(x * z)
elif y == '/':
    print(x / z)
else:
    print('error: input not supported')