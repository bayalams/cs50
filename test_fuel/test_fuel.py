import fuel
import pytest

def main():
    test_fraction()

def test_fraction():
    assert fraction("1/3") == "33%"
    with pytest.raises(ZeroDivisionError):
        fraction("0")
