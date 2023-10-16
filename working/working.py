import re
hours = input("Hours: ")

hours_pattern = re.search(r"^(\d{1,2}):\d{2}\s[APM]{2}(\d+)('AM'|'PM')$", hours)
print(hours_pattern.group(1))

if hours_pattern:
    hours1, hours2 = hours_pattern.group(1), hours_pattern.group(3)
    print(hours1, hours2)
else:
    pass