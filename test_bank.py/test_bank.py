
import pytest
from bank import value

def main():
    test_value_num()

def test_value_num():

    with pytest.raises(SystemExit):
        value("3")


def test_value_hello():

    assert value("hello") == "$

if __name__ == "__main__":
    main()