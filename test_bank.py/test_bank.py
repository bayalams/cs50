
import pytest
from bank import value

def main():
    test_value_num()

def test_value_num():

    with pytest.raises(SystemExit):
        test_value("3")

if __name__ == "__main__":
    main()