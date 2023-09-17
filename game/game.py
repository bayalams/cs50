import random

while True:
    try:
        level = int(input("Level: "))
        random_number = random.randint(1, level)
    except ValueError:
        
    else:
        print(f"Random number: {random_number}")
        guess = int(input("Guess: "))
        if guess < random_number:
            print("Too small!")
        elif guess > random_number:
            print("Too large!")
        else:
            print("Just right!")
