from numb3rs import validate
import pytest

def main():
    test_validate()

def test_validate():
    assert validate("192.168.1.1")
    assert validate("255.255.255.255")
    assert validate("127.0.0.1")
    assert not validate("192.168.1.256")
    assert not validate("192.168.1")
    assert not validate("256.256.256.256")
    assert not validate("300.300.300.300")
    assert not validate("abcd")

if __name__ == "__main__":
    main()