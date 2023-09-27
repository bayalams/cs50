def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        return
    else:
        print("Invalid")
        return


def is_valid(plate):

    if length(plate) and char_type(plate) and initial_char_type(plate) and first_number_is_zero(plate) and numbers_in_middle(plate):
        return True


def length(plate):

    if len(plate) < 2 or len(plate) > 6:
        print("must be between 2 and 6 digits long.")
        return False
    else:
        return True

def char_type(plate):

    for i in plate:
        if i.isalpha() or i.isnumeric():
            pass
        else:
            print("No periods, spaces, or punctuation marks are allowed.")
            return False
    return True

def initial_char_type(plate):

    for j in plate[:2]:
        if j.isalpha() != True:
            print("The first 2 digits must be letters.")
            return False
        else:
            return True

def first_number_is_zero(plate):

    for ele in plate:
        if ele.numeric() and ele == 0:
            return False
        else:
            return True

def numbers_in_middle(plate):

    # cs34c
    for i in plate:
        if i.isnumeric():
            if plate['c':].isnumeric():
                return True


# def nested_number(plate):

#     a = -1

#     for i in plate:
#         a = a + 1
#         if i.isnumeric():
#             if i == "0":
#                 print(f"check 1: {i}")
#                 print("the first number cannot be a 0")
#                 return False
#             for j in plate[a:]:
#                 if j.isalpha():
#                     print(f"check 2: {i, j}")
#                     print("Numbers cannot be used in the middle of a plate; they must come at the end.")
#                     return False
#                 else:
#                     pass
#             return True
#         else:
#             pass

#     return True

main()


















