import random

def guess_range():

    while True:
        try:
            level = int(input("Level: "))
            random_number = int(random.randint(1, level))
            print(f"Random number: {random_number}")
            return random_number

        except ValueError:
            pass

def guess(random_number):

    while guess != random_number:
        guess = int(input("Guess: "))
        if guess < random_number:
            print("Too small!")
        elif guess > random_number:
            print("Too large!")
        else:
            print("Just right!")


if __name__ == "__main__":
    random_number = guess_range()
    guess(random_number)