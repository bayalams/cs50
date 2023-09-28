def main():
    fraction()
    gauge(percentage)

def fraction():
    while True:
        try:
            fuel = input("Fraction: ")
            fuel = fuel.split("/")
            X = int(fuel[0])
            Y = int(fuel[1])
            print(X, Y)

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
            print("F")
        elif percentage <= 1:
            print("E")
        elif percentage > 1 and percentage < 99:
            print(f"{percentage}%")


if __name__ == "__main__":
    percentage = fraction()
    main()