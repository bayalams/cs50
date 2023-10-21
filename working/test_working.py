import pytest
from working import find_pattern, convert

def main():
    test_find_pattern()
    test_convert()

def test_find_pattern():
    assert "9:00 AM to 5:00 PM" == True
    assert "9 AM to 5 PM" == True

def test_convert():

if __name__ == "__main__":
    main()