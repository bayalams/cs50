date = input("Date: ")
date = date.title()
date_list = date.replace(",", " ").split()
print(date_list)


months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

if date_list[0] in months:
    date_month = date_list[0]

print(date_month)

