#não funciona se só importar o módulo, porquê??

from fuel import fraction
from fuel import gauge
import pytest

def main():
    test_fraction()

def test_fraction():
    assert fraction("1/3") == "33%"
    with pytest.raises(ZeroDivisionError):
        fraction("0")

if __name__ == "__main__":
    main()