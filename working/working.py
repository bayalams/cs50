import re
hours = input("Hours: ")

hours_pattern = re.search(r"^(\d+)(AM | PM)(\d+)(AM | PM)$", hours)
