def fraction():

    fuel = input("Fraction: ")
    fuel = fuel.split("/")

    X = int(fuel[0])
    Y = int(fuel[1])

    percentage = round((X / Y) * 100)


    if percentage in [99, 100]:
        print("F")
    elif percentage <= 1:
        print("E")
    elif percentage > 1 and percentage < 99:
        print(f"{percentage}%")


fraction()