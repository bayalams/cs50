expression = input("expression: ")
if len(expression.split(" ")) != 3:
    print("error: the input expression should contain two operands and one operator, with a space between operand and operator and operator and operand. Usage example: 1 + 1.")
    print(f'debug: {expression} {expression.split(" ")}')
    exit(-1)

list_expression = expression.split(" ")
#print(list_expression)

x = list_expression[0]
y = list_expression[1]
z = list_expression[2]

# print(x)
# print(y)
# print(z)

if x.isnumeric() != True:
    print('error: x must be a numeric character. For example: 1, 3.1, 1999')
    print(f'debug: {x}')
    exit(-1)

if y not in ['+', '-', '*', '/']:
    print('error: y must be an operator. For example: +, -, *, /')
    print(f'debug: {y}')
    exit(-1)

if z.isnumeric() != True:
    print('error: z must be a numeric character. For example: 1, 3.1, 1999')
    print(f'debug: {z}')
    exit(-1)

x = float(x)
z = float(z)

if y == '/' and z == 0:
    print('error: float cannot be divided by 0')
    print(f'debug: operator = {y} and second operand = {z}')
    exit(-1)

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
    exit(-1)