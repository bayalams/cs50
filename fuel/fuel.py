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

    #problemas:
#:( input of 10/3 results in reprompt
    #expected program to reject input, but it did not
#:( input of 2/3 yields output of 67%
    #expected "67%", not "66%\n"