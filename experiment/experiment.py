import random

def generate_random_integer(num_digits):
    # Calculate the minimum and maximum values for the specified number of digits
    min_value = 10**(num_digits - 1)
    max_value = 10**num_digits - 1

    # Generate a random integer within the specified range
    random_number = random.randint(min_value, max_value)

    return random_number

# Example: Generate a random 3-digit integer
num_digits = 3
random_integer = generate_random_integer(num_digits)
print(f"Random {num_digits}-digit integer: {random_integer}")
