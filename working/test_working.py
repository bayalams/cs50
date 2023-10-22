import pytest
from working import split_hours, convert

def main():
    test_split_hours()
    #test_convert()

@pytest.mark.parametrize("input_hours, expected_split1, expected_split2", [
    ("9:00 AM to 5:00 PM", ['9', '00', 'AM'], ['5', '00', 'PM']),
    ("9 AM to 5 PM", ['9', 'AM'], ['5', 'PM']),
    ("12:00 PM to 12:00 AM", ['12', '00', 'PM'], ['12', '00', 'AM'])
])

def test_split_hours(input_hours, expected_split1, expected_split2):
    split_hours1, split_hours2 = split_hours(input_hours)
    assert split_hours1 == expected_split1
    assert split_hours2 == expected_split2

@pytest.mark.parametrize("split_hours1, split_hours2, expected_output", [
    (['9', '00', 'AM'], ['5', '00', 'PM'], "09:00 to 17:00"),
    (['9', 'AM'], ['5', 'PM'], "09:00 to 17:00"),
    (['12', '00', 'PM'], ['12', '00', 'AM'], "12:00 to 00:00")
])

def test_convert(split_hours1, split_hours2, expected_output):
    result = convert(split_hours1, split_hours2)
    assert result == expected_output

@pytest.mark.parametrize("split_hours1, split_hours2, [
    (['9', '1', 'AM'], ['5', '76', 'PM']),
    (['23', 'AM'], ['15', 'PM'])
])

def test_convert_invalid_hours(invalid_hours):
    with pytest.raises(ValueError):
        convert(invalid_hours)



if __name__ == "__main__":
    main()