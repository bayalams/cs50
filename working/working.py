
import re

def main():
    hours = input("Hours: ")
    split_hours1, split_hours2 = find_pattern(hours)
    if split_hours1 and split_hours2:
        print(convert(split_hours1, split_hours2))
    else:
        print("Invalid time format.")


def find_pattern(hours):
    hours_pattern = re.search(r"^(\d{1,2}(:\d{2},[0-59])?\s(?:AM|PM))\sto\s(\d{1,2}(:\d{2})?\s(?:AM|PM))$", hours)

    if hours_pattern:
        hours1, hours2 = hours_pattern.group(1), hours_pattern.group(3)
        print(hours1, hours2)

    split_hours1 = re.split(r":|\s", hours1)
    split_hours2 = re.split(r":|\s", hours2)

    return split_hours1, split_hours2

def convert(split_hours1, split_hours2 ):
    if len(split_hours1) == 3:
        hour1, minutes1, half1 = split_hours1
        print(hour1, minutes1, half1)
    else:
        hour1, half1 = split_hours1
        minutes1 = "00"

    if len(split_hours2) == 3:
        hour2, minutes2, half2 = split_hours2
        print(hour2, minutes2, half2)
    else:
        hour2, half2 = split_hours2
        minutes2 = "00"


    if half1 == "PM" and int(hour1) != 12:
        hour1 = str(int(hour1) + 12)
    elif half1 == "AM" and hour1 == "12":
        hour1 = "00"


    if half2 == "PM" and int(hour2) != 12:
        hour2 = str(int(hour2) + 12)
    elif half2 == "AM" and hour2 == "12":
        hour2 = "00"


    return f"{hour1.zfill(2)}:{minutes1} to {hour2.zfill(2)}:{minutes2}"


if __name__ == "__main__":
    main()