while True:
    try:
        fuel = input("Fraction: ")
        fuel = fuel.split("/")

        X = int(fuel[0])
        Y = int(fuel[1])

        percentage = int((X / Y) * 100)

        if percentage >= 99:
            print("F")
        elif percentage <= 1:
            print("E")
        else:
            print(f"{percentage}%")

        if X > Y:
            pass

    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ValueError:
        print("ValueError")
    except Exception as ex:
        print(f"An exception of type {type(ex).__name__} occurred. Arguments:\n{ex.args}")