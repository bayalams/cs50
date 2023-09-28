def main():
    convert()
    print(gauge(percentage))


#convert expects a str in X/Y format as input, wherein each of X and Y is an integer,
# and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.
# If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
# If Y is 0, then convert should raise a ZeroDivisionError.
def convert():
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


#gauge expects an int and returns a str that is:


def gauge(percentage):
    if percentage in [99, 100]:
        return "F"
    elif percentage <= 1:
        return "E"
    elif percentage > 1 and percentage < 99:
        return f"{percentage}%"


if __name__ == "__main__":
    percentage = convert()
    main()