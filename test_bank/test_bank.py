
import pytest
from bank import value

def main():
    test_value_num()
    test_value_hello()
    test_value_else()

def test_value_num():
    return assert value("3") == "$10"

def test_value_hello():
    return assert value("hello") == "$0"

def test_value_else():
    return assert value("What's up?") == "$100"

if __name__ == "__main__":
    main()