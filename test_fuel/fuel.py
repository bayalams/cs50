def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            fraction = fraction.split("/")
            X = int(fraction[0])
            Y = int(fraction[1])

            percentage = round((X / Y) * 100)
            #print(type(percentage))
            return percentage

        except ZeroDivisionError:
            raise ZeroDivisionError
        except ValueError:
            raise ValueError
        except IndexError:
            raise IndexError


def gauge(percentage):
    if percentage in [99, 100]:
        return "F"
    elif percentage <= 1:
        return "E"
    elif percentage > 1 and percentage < 99:
        return f"{percentage}%"


if __name__ == "__main__":
    main()