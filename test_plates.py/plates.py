
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        return
    else:
        print("Invalid")
        return


def is_valid(plate):

    # if length(plate) and char_type(plate) and initial_char_type(plate) and nested_number(plate):
    #     return True

    # plate must be longer than two and shorter than 6
    if 2 < len(plate) < 6:
        return True
    elif for i in plate:
            if i.isalpha() or i.isnumeric():
                return True
    elif for j in plate[:2]:
        if j.isalpha() != True:
            return False
        else:
            return True


    a = -1

    for i in plate:
        a = a + 1
        if i.isnumeric():
            if i == "0":
                return False
            for j in plate[a:]:
                if j.isalpha():
                    return False
                else:
                    pass
            return True
        else:
            pass

    return True


if __name__ == "__main__":
    main()


















