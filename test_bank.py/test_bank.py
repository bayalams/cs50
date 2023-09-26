
import pytest
from bank import value

def main():
    test_value_num()
    test_value_num(

def test_value_num():

    with pytest.raises(SystemExit):
        value("3")


def test_value_hello():

    assert value("hello") == "$0"


def test_value_else():

    assert value("What's up?") == "$100"


if __name__ == "__main__":
    main()