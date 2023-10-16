import re
hours = input("Hours: ")

hours_pattern = re.search(r"^(\d{1,2}:\d{2}\s(?:AM|PM))\sto\s(\d{1,2}:\d{2}\s(?:AM|PM))$", hours)

hour1, minutes1, half1 = re.split(r":|\s", hours1)
hour2, minutes2, half2 = re.split(r":|\s", hours2)

print(hour1, minutes1, half1)

if half1 == "PM":
    hour1 = int(hour1)
    hour1 = int(hour1 + 8)
else:
    pass

print(hour1, minutes1, half1)