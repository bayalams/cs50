coke_price = 50

amount_due = coke_price

while amount_due <= coke_price and amount_due > 0:
    insert_coin = int(input("Insert coin: "))
    amount_due = amount_due - insert_coin

    if insert_coin != 10 and insert_coin != 25 and insert_coin != 5:
        amount_due = coke_price
        print("Amount Due: 50")

    elif amount_due > 0:
        print(f"Amount Due: {amount_due}")
    else:
        change_owed = abs(amount_due)
        print(f"Change Owed: {change_owed}")
















