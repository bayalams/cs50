from plates import is_valid

def test_length():
    assert is_valid("mmcsdwd") == False
    assert is_valid("cs50") == True
    assert is_valid("c") == False



