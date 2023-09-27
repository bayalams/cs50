from plates import is_valid

def test_length():
    assert is_valid("mmcsdwd") == False
    assert is_valid("cs50") == True
    assert is_valid("c") == False

def test_char_type():
    assert is_valid("cs50") == True
    assert is_valid("3erf") == False
    assert is_valid("34rf") == False

