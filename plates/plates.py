# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

plate = input("Plate: ")
plate = plate.upper()
print(plate)


if len(plate) < 2 or len(plate) > 6:
    print("1. Invalid.")

else:
    for i in plate:
        if not (i.isalpha() or i.isnumeric()):
            print("2. Invalid")
        else:
            pass

    for j in plate[:2]:
        if j.isalpha() != True:
            print ("3. Invalid.")
            break
        else:
            print("Valid.")


# if len(plate) % 2 == 0:
#     middle_even = plate[(len(plate) // 2) - 1] + plate[(len(plate) // 2)]
#     print(f"Middle Even: {middle_even}")
# else:
#     middle_odd = plate[len(plate) // 2]
#     print(f"Middle Odd: {middle_odd}")
















