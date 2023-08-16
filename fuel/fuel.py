#X or Y is not an integer
# X is greater than Y, or Y is 0, instead prompt the user again.

try:
    fuel = input("Fraction: ")
    fuel = fuel.split("/")
    #print(fuel)

    X = int(fuel[0])
    Y = int(fuel[1])

    percentage = int((X / Y) * 100)
    print(f"{percentage}%")
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
except Exception:
    print('Outra')