def main():

    greeting = input("Greeting: ")


def value(greeting):

    greeting = greeting.lower().strip()

    if greeting[0:5] == "hello":
        print("$0")
    elif greeting[0] == "h":
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()



