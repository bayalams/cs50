def fraction():

    fuel = input("Fraction: ")
    fuel = fuel.split("/")

    X = int(fuel[0])
    Y = int(fuel[1])

    if X > Y:
        pass

    return int((X / Y) * 100)

while True:
    try:
        percentage = fraction()

        if percentage >= 99:
            print("F")
        elif percentage <= 1:
            print("E")
        else:
            print(f"{percentage}%")

        exit(0)

    except ZeroDivisionError:
        pass
    except ValueError:
        pass