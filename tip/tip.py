

#meal_price = float(input("how much was the meal? "))
#percentage = float(input("what percentage would you like to tip? "))

#tip = meal_price * (percentage/100)
#print(tip)

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")