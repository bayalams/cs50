def fraction():

    fuel = input("Fraction: ")
    fuel = fuel.split("/")

    X = int(fuel[0])
    Y = int(fuel[1])

    return int((X / Y) * 100)

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

    #problemas:
#:( input of 10/3 results in reprompt
    #expected program to reject input, but it did not
#:( input of 2/3 yields output of 67%
    #expected "67%", not "66%\n"