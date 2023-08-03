#1. somar até 50 cents - def ammount_due
#2. a partir de 50 cents, subtrair def change_owed

amount = int(input("Insert coin: "))
coke_price = 50

if amount != 10 and amount != 25 and amount != 5:
    print("Error: Machine only accepts coins of 5, 10 or 25 cents.")
    exit(-1)

amount_due = coke_price - amount

while True:
    amount_due = coke_price - amount
    break

amount_due = amount_due - amount







