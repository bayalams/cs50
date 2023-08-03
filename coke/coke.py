#1. somar até 50 cents - def ammount_due
#2. a partir de 50 cents, subtrair def change_owed

ammount = int(input("Insert coin: "))

if ammount != 10 and ammount != 25 and ammount != 5:
    print("Error: Machine only accepts coins of 5, 10 or 25 cents.")
    exit(-1)

coke_price = 50

ammount_due = coke_price - ammount
print(f"ammount due: {ammount_due}")



