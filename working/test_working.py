import pytest
from working import find_pattern, convert

def main():
    test_find_pattern_valid_input()
    #test_convert()

@pytest.mark.parametrize("input_hours, expected_split1, expected_split2", [
    ("9:00 AM to 5:00 PM", ['9', '00', 'AM'], ['5', '00', 'PM']),
    ("9 AM to 5 PM", ['9', 'AM'], ['5', 'PM']),
    ("12:00 PM to 12:00 AM", ['12', '00', 'PM'], ['12', '00', 'AM'])
])

def test_find_pattern_valid_input(input_hours, expected_split1, expected_split2):
    split_hours1, split_hours2 = find_pattern(input_hours)
    assert split_hours1 == expected_split1
    assert split_hours2 == expected_split2

def test_find_pattern_invalid_input():
    hours = "9 AM - 5 PM"
    with pytest.raises(ValueError):
        find_pattern(hours)
    # with pytest.raises(ValueError):
    #     "10:7 AM - 5:1 PM"
    # with pytest.raises(ValueError):
    #     "09:00 to 17:00"

#def test_convert():

if __name__ == "__main__":
    main()