
import pytest
from bank import value

def main():
    test_value_num()
    test_value_hello()
    test_value_else()

def test_value_num():
    assert value("3") == 100
    assert value("10") == 100
    assert value("30") == 100


def test_value_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hellomotto") == 0

def test_value_else():
    assert value("What's up?") == 100
    assert value("cenas") == 100

if __name__ == "__main__":
    main()