# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

plate = input("Plate: ")
plate = plate.upper()
print(plate)

for i in plate:
        if not (i.isalpha() or i.isnumeric()):
            print("2. Invalid")
        elif len(plate) < 2 or len(plate) > 6:
            print("1. Invalid.")
        else:
            for i in plate[:2]:
                if i.isalpha() != True:
                    ("3. Invalid.")



else:
    print("valid")













