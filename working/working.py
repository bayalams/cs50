import re
hours = input("Hours: ")

hours_pattern = re.search(r"^(\d+)(AM | PM)(\d+)(AM | PM)$", hours)

if hours_pattern:
    hours1, hours2 = hours_pattern.group(1), hours_pattern.group(3)
    print(hours1, hours2)
else:
    pass