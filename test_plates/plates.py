def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        return
    else:
        print("Invalid")
        return


def is_valid(plate):

    print('is_valid', length(plate),
        char_type(plate),
        initial_char_type(plate),
        first_number_is_zero(plate),
        numbers_in_middle(plate))
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
        print(not i.isalpha(), i.isnumeric())
        if (not i.isalpha() or i.isnumeric()):
            print('entrou1')
            pass
        else:
            print('entrou2')
            return False

    print('entrou3')
    return True

def initial_char_type(plate):

    for j in plate[:2]:
        if j.isalpha() != True:
            return False

    return True

def first_number_is_zero(plate):

    for ele in plate:
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




































