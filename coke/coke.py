#1. somar até 50 cents - def ammount_due
#2. a partir de 50 cents, subtrair def change_owed

amount = int(input("Insert coin: "))

if amount != 10 and amount != 25 and amount != 5:
    print("Error: Machine only accepts coins of 5, 10 or 25 cents.")
    exit(-1)

coke_price = 50
amount_due = coke_price - amount

while amount_due > 0:
    print(f"amount due: {amount_due}")
    break




