from plates import is_valid

def main():
    test_length()
    test_char_type()
    test_initial_char_type()
    test_first_number_is_zero()
    test_numbers_in_middle()


def test_length():
    assert is_valid("mmcsdwd") == False
    assert is_valid("cs50") == True
    assert is_valid("c") == False

def test_char_type():
    assert is_valid("cs50") == True
    assert is_valid("3erf") == False
    assert is_valid("34rf") == False

def test_initial_char_type():
    assert is_valid("cs50") == True
    assert is_valid("23de") == False
    assert is_valid("c342") == False

def test_first_number_is_zero():
    assert is_valid("cs50") == True
    assert is_valid("cs05") == False

def test_numbers_in_middle():
    assert is_valid("cs50") == True
    assert is_valid("cs50d") == False


if __name__ == "__main__":
    main()