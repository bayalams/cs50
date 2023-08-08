# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

plate = input("Plate: ")
plate = plate.upper()
print(plate)

if len(plate) < 2 or len(plate) > 6:
    print("Error: The plate must be between 2 and 6 characters long.")
elif plate[:2] != isalpha():
    print("Error: All vanity plates must start with at least two letters.")





