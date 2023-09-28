def main():
    fraction()
    gauge(percentage)

def fraction():
    while True:
        try:
            fraction = input("Fraction: ")
            fraction = fraction.split("/")
            X = int(fraction[0])
            Y = int(fraction[1])

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