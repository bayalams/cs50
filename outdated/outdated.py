date = input("Date: ")
date = date.title()
date_list = date.replace(",", " ").split()
print(date_list)


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

if date_list[0] in months:
    print(date_list[0])