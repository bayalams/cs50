menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

order = input("Item: ")
order = order.title()

if order in menu:
    price = menu[order]
    price = "{:.2f}".format(price)
    print(f"${price}")

total = 0

for price in menu:
    total = total + float(price)
    print(price)


#while True:
  #  order = input("Item: ")
   # order = order.title()
    #total = total +
   # if order == "Exit":
    #    pass
    #    break