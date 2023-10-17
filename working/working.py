#falta o 0 antes da hora se for só 1 dígito

import re

def main():
    hours = input("Hours: ")
    print(convert(hours))

def convert(hours):
    hours_pattern = re.search(r"^(\d{1,2}:\d{2}?\s(?:AM|PM))\sto\s(\d{1,2}:\d{2}?\s(?:AM|PM))$", hours)

    if hours_pattern:
        hours1, hours2 = hours_pattern.group(1), hours_pattern.group(2)
        print(hours1, hours2)
    else:
        pass

    hour1, minutes1, half1 = re.split(r":|\s", hours1)
    hour2, minutes2, half2 = re.split(r":|\s", hours2)

    print(hour1, minutes1, half1)

    if half1 == "PM":
        hour1 = int(hour1) + 12
    elif half2 == "PM":
        hour2 = int(hour2) + 12
    else:
        pass

    #print(f"{hour1}:{minutes1} to {hour2}:{minutes2}")
    return f"{hour1}:{minutes1} to {hour2}:{minutes2}"

if __name__ == "__main__":
    main()