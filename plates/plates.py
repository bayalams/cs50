# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        return
    else:
        print("Invalid")
        return


def is_valid(plate):

    if length(plate) and char_type(plate) and initial_char_type(plate) and nested_number(plate):
        return True


def length(plate):

    if len(plate) < 2 or len(plate) > 6:
        return False
    else:
        return True

def char_type(plate):

    for i in plate:
        if not i.isalnum():
            return False
        else:
            return True

def initial_char_type(plate):

    for j in plate[:2]:
        if j.isalpha() != True:
            return False
        else:
            return True


def nested_number(plate):

    for i in plate:
        if i.isnumeric():
            a = i
            for j in plate[:a]:
                if j.isalpha():
                    return False
                else:
                    pass
            return True
        else:
            pass
    return True

main()


















