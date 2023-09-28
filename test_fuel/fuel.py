def main():
    fraction = input("Fraction: ")
    print(type(fraction))
    convert(fraction)
    # gauge(percentage)


def convert(fraction):

    while True:
        try:
            fraction = fraction.split("/")
            print(fraction)
            print(type(fraction))
            X = int(fraction[0])
            Y = int(fraction[1])
            percentage = round((X / Y) * 100)
            print(percentage)

        except ZeroDivisionError:
            pass
        except ValueError:
            pass

    return percentage

# def gauge(percentage):

#     if percentage in [99, 100]:
#         print("F")
#         return "F"
#     elif percentage <= 1:
#         print("E")
#         return "E"
#     elif percentage > 1 and percentage < 99:
#         print(f"{percentage}%")
#         return f"{percentage}%"


if __name__ == "__main__":
    main()

