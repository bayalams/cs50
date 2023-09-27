def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        return
    else:
        print("Invalid")
        return


def is_valid(plate):

    if (
        length(plate) and
        char_type(plate) and
        initial_char_type(plate) and
        first_number_is_zero(plate) and
        numbers_in_middle(plate)
    ):
        return True
    else:
        return False


def length(plate):

    if len(plate) < 2 or len(plate) > 6:
        print("must be between 2 and 6 digits long.")
        return False
    else:
        return True

def char_type(plate):

    for i in plate:
        if (not i.isalpha() or i.isnumeric()):
            pass
        else:
            return False
    return True

def initial_char_type(plate):

    for j in plate[:2]:
        if j.isalpha() != True:
            return False

    return True

def first_number_is_zero(plate):

    for ele in plate:
        print(ele, ele.isnumeric(), ele=='0')
        if ele.isnumeric():
            if ele == '0':
                return False
            else:
                return True

    return True

def numbers_in_middle(plate):

    # INVALID: cs34c
    # VALID: cs345
    for idx, i in enumerate(plate):
        if i.isnumeric():
            if plate[idx:].isnumeric():
                return True
            else:
                return False


if __name__ == "__main__":
    main()




































