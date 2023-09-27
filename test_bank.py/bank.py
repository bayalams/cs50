
def main():

    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):

    greeting = greeting.lower().strip()

    if not greeting.isalpha():
        exit(1)
    elif greeting[0:5] == "hello":
        return "$0"
    elif greeting[0] == "h":
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()



