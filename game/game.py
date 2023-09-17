import random


level = int(input("Level: "))
random_number = random.randint(1, level)
print(f"Random number: {random_number}")
guess = int(input("Guess: "))
