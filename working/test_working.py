import pytest
from working import find_pattern, convert

def main():
    test_find_pattern()
    #test_convert()

@pytest.mark.parametrize("input_hours, expected_split1, expected_split2", [
    ("9:00 AM to 5:00 PM", ['9', '00', 'AM'], ['5', '00', 'PM']),
    ("9 AM to 5 PM", ['9', 'AM'], ['5', 'PM']),
    ("12:00 PM to 12:00 AM", ['12', '00', 'PM'], ['12', '00', 'AM'])
])

def test_find_pattern(input_hours, expected_split1, expected_split2):
    split_hours1, split_hours2 = find_pattern(input_hours)
    assert split_hours1 == expected_split1
    assert split_hours2 == expected_split2

@pytest.mark.parametrize("invalid_hours", [
    "9:00 AM - 5:00 PM", "19 AM to 25 PM",
    "13 AM to 23 PM", "5 AM - 9 PM", "2 to 3"
    ])

def test_find_pattern_invalid_input(invalid_hours):
    with pytest.raises(ValueError):
        find_pattern(invalid_hours)

def test_convert():

if __name__ == "__main__":
    main()