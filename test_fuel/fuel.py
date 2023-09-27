def main():
    fraction = input("Fraction: ")
    print(gauge(percentage))
    return


def convert(fraction):

    while True:
        try:
            fraction = fraction.split("/")
            X = int(fraction[0])
            Y = int(fraction[1])
            percentage = round((X / Y) * 100)
            return percentage
        except ZeroDivisionError:
            pass
        except ValueError:
            pass


def gauge(percentage):
    if percentage in [99, 100]:
        return "F"
    elif percentage <= 1:
        return "E"
    elif percentage > 1 and percentage < 99:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
