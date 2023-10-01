from fuel import convert, gauge
import pytest

def main():
    test_convert()

def test_convert():
    assert convert("1/3") == 33
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(IndexError):
        convert("1")
    with pytest.raises(ValueError):
        convert("cat")


if __name__ == "__main__":
    main()