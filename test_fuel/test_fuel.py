from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1/3") == 33
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("10/r")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"

if __name__ == "__main__":
    main()