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

    guess = int(input("Guess: "))
    if guess > 0 or guess != int:
        pass

    while guess != random_number:
        try:
            if guess < random_number:
                if guess < 1:
                    guess = int(input("Guess-1: "))
                    if guess > 0 or guess != int:
                        pass
                else:
                    print("paragem 1")
                    print("Too small!")
                    guess = int(input("Guess1: "))
                    if guess > 0 or guess != int:
                        pass
            elif guess > random_number:
                print("paragem 2")
                print("Too large!")
                guess = int(input("Guess2: "))
                if guess > 0 or guess != int:
                    pass
            else:
                print("Just right!")
                break
        except ValueError:
            pass



if __name__ == "__main__":
    random_number = guess_range()
    guess_number(random_number)