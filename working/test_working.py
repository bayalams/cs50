import pytest
from working import split_hours, convert

def main():
    test_split_hours()
    test_convert()


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


@pytest.mark.parametrize("invalid_split_hours1, invalid_split_hours2",
                         [(['9', '1', 'AM'], ['5', '00', 'PM']),
                          (['9', '00', 'AM'], ['5', 'XM']),
                          (['25', '00', 'PM'], ['12', '59', 'AM'])])

def test_convert_invalid(invalid_split_hours1, invalid_split_hours2):
    with pytest.raises(ValueError):
        convert(invalid_split_hours1, invalid_split_hours2)


if __name__ == "__main__":
    main()