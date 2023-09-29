def main():
    percentage = convert()
    print(gauge(percentage))


def convert():
    while True:
        try:
            fuel = input("Fraction: ")
            fuel = fuel.split("/")
            X = int(fuel[0])
            Y = int(fuel[1])

            percentage = round((X / Y) * 100)
            return percentage

        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        except IndexError:
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