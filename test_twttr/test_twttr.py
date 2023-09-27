
from twttr import shorten
import pytest

def main():

    test_shorten_lower()
    test_shorten_upper()
    ommit_numbers()

def test_shorten_lower():
    assert shorten("macaco") == "mcc"
    assert shorten("beatriz") == "btrz"


def test_shorten_upper():
    assert shorten("MACACO") == "MCC"
    assert shorten("BEATRIZ") == "BTRZ"

def ommit_numbers():
    assert shorten("BEATRIZ2") == "BTRZ2"

if __name__ == "__main__":
    main()