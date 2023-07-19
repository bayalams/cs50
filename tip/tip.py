meal_price = float(input("how much was the meal? "))
percentage = float(input("what percentage would you like to tip? "))
percentage = percentage/100

tip = meal_price * percentage
print(tip)