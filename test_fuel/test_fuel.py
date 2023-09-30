import fuel
import pytest

def main():
    test_convert()

def test_convert():
    assert convert("1/3") == "33%"
    with pytest.raises(ZeroDivisionError):
        convert("0")

if __name__ == "__main__":
    main()