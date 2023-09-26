
from twttr import shorten
import pytest

def main():

    test_shorten_lower()
    test_shorten_upper()
    test_shorten_num()

def test_shorten_lower():

    assert shorten("macaco") == "mcc"


def test_shorten_upper():

    assert shorten("MACACO") == "MCC"

def test_shorten_num():

    with pytest.raises(SystemExit):
        shorten("3")


if __name__ == "__main__":
    main()