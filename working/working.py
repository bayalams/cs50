#falta o 0 antes da hora se for só 1 dígito

import re

def main():
    hours = input("Hours: ")
    print(convert(hours))

def convert(hours):
    hours_pattern = re.search(r"^(\d{1,2}(:\d{2})?\s(?:AM|PM))\sto\s(\d{1,2}(:\d{2})?\s(?:AM|PM))$", hours)

    if hours_pattern:
        hours1, hours2 = hours_pattern.group(1), hours_pattern.group(3)
        print(hours1, hours2)
    else:
        pass


    split_hours1 = re.split(r":|\s", hours1)
    split_hours2 = re.split(r":|\s", hours2)

    print(split_hours1, split_hours2)

    if len(split_hours1) == 3:
        hour1, minutes1, half1 = split_hours1
    else:
        minutes1 = '00'

    if len(split_hours2) == 3:
        hour2, minutes2, half2 = split_hours2
    else:
        minutes2 = '00'


    if half1 == "PM":
        hour1 = int(hour1) + 12
    elif half2 == "PM":
        hour2 = int(hour2) + 12
    else:
        pass
    

    if len(hour1) == 1 or len(hour2) == 1:
        return f"0{hour1}:{minutes1} to 0{hour2}:{minutes2}"
    else:
        return f"{hour1}:{minutes1} to {hour2}:{minutes2}"
if __name__ == "__main__":
    main()