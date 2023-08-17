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


total = 0

if order in menu:
    price = float(menu[order])
    print(price)


#while True:
  #  order = input("Item: ")
   # order = order.title()
    #total = total +
   # if order == "Exit":
    #    pass
    #    break