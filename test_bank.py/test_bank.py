from bank import value

def test_value(greeting):

    if not greeting.isalpha():
        print("Wrong")

test_value(greeting)