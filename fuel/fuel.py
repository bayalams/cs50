while True:
    try:
        fuel = input("Fraction: ")
        fuel = fuel.split("/")

        X = int(fuel[0])
        Y = int(fuel[1])

        percentage = int((X / Y) * 100)
        print(f"{percentage}%")

        if

    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ValueError:
        print("ValueError")
    except Exception as ex:
        print(f"An exception of type {type(ex).__name__} occurred. Arguments:\n{ex.args}")