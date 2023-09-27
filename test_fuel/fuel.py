def main():
    fuel = input("Fraction: ")
    




def fraction():

    fuel = input("Fraction: ")
    fuel = fuel.split("/")

    X = int(fuel[0])
    Y = int(fuel[1])

    return round((X / Y) * 100)

while True:
    try:
        percentage = fraction()

        if percentage in [99, 100]:
            print("F")
            break
        elif percentage <= 1:
            print("E")
            break
        elif percentage > 1 and percentage < 99:
            print(f"{percentage}%")
            break

    except ZeroDivisionError:
        pass
    except ValueError:
        pass

