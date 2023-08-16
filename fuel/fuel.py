fuel = input("Fraction: ")
fuel = fuel.split("/")
print(fuel)

percentage = (int(fuel[0]) / int(fuel[1])) * 100
print(percentage)