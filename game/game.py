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

def guess_number(random_number):

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < random_number:
                print("Too small!")
                guess = int(input("Guess: "))
            elif guess > random_number:
                print("Too large!")
                guess = int(input("Guess: "))
            else:
                print("Just right!")
                break
        except ValueError:
            pass



if __name__ == "__main__":
    random_number = guess_range()
    guess_number(random_number)