meal_price = float(input("how much was the meal? "))
percentage = float(input("what percentage would you like to tip? "))

tip = meal_price * (percentage/100)
print(tip)

def dollars_to_float(d):
    d = input("insert ammount: $")
    d = float(d)

def