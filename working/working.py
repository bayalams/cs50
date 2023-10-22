
import re

def main():
    hours = input("Hours: ")
    split_hours1, split_hours2 = split_hours(hours)
    print(split_hours1, split_hours2)
    if split_hours1 and split_hours2:
        print(convert(split_hours1, split_hours2))
    else:
        print("Invalid time format.")


def split_hours(hours):
    hours_pattern = re.search(r"^(\d{1,2}(:\d{2})?\s(?:AM|PM))\sto\s(\d{1,2}(:\d{2})?\s(?:AM|PM))$", hours)

    #see if input matches required pattern and retrieve the grouped information
    if hours_pattern:
        hours1, hours2 = hours_pattern.group(1), hours_pattern.group(3)
        print(hours1, hours2)
    else:
        raise ValueError

    #split the given hours in hour, minutes and AM/PM
    split_hours1 = re.split(r":|\s", hours1)
    split_hours2 = re.split(r":|\s", hours2)

    return split_hours1, split_hours2

def convert(split_hours1, split_hours2 ):

    #if the input has three sections, i.e hours, minutes and AM/PM, return them, otherwise, if there is not minutes group, minutes = 00
    if len(split_hours1) == 3:
        hour1, minutes1, half1 = split_hours1
        print(hour1, minutes1, half1)
        if int(minutes1) > 59:
            raise ValueError
    else:
        hour1, half1 = split_hours1
        minutes1 = "00"

    if len(split_hours2) == 3:
        hour2, minutes2, half2 = split_hours2
        print(hour2, minutes2, half2)
        if int(minutes2) > 59:
            raise ValueError
    else:
        hour2, half2 = split_hours2
        minutes2 = "00"

    if int(hour1) > 12 or int(hour2) > 12:
        raise ValueError


    #if it's PM and not noon, add 12 to the hours to turn it into the 24 hour format
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