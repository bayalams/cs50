
from twttr import shorten
import pytest

def main():

    test_shorten_lower()
    test_shorten_upper()
    test_ommit_numbers()

def test_shorten_lower():
    assert shorten("macaco") == "mcc"
    assert shorten("beatriz") == "btrz"


def test_shorten_upper():
    assert shorten("MACACO") == "MCC"
    assert shorten("BEATRIZ") == "BTRZ"

def test_ommit_numbers():
    assert shorten("BEATRIZ2") == "BTRZ2"

def test_ommit_punctuation():
    assert shorten("What's up?") == "Wht's p?"
    assert shorten("Hello, David, I'm Bea!") == "Hll, Dvd, 'm B!"

if __name__ == "__main__":
    main()