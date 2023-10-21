import pytest
from working import find_pattern, convert

def main():
    test_find_pattern()
    #test_convert()

def test_find_pattern():
    hours = "9:00 AM to 5:00 PM"
    split_hours1, split_hours2 = find_pattern(hours)
    assert split_hours1 == ['9','00', 'AM']
    assert split_hours2 == ['5', '00', 'PM']
    # hours = "9 AM to 5 PM"
    # assert split_hours1 == ['9', 'AM']
    # assert split_hours2 == ['5', 'PM']
    with pytest.raises(ValueError):
        hours = "9 AM - 5 PM"
    with pytest.raises(ValueError):
        "10:7 AM - 5:1 PM"
    with pytest.raises(ValueError):
        "09:00 to 17:00"

#def test_convert():

if __name__ == "__main__":
    main()