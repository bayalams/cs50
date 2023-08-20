def parse_date_format_1(s):
    print(s)
    print(s.replace(",", ""))
    day = s.replace(",", "").split(" ")
    month = ""
    year = ""



def parse_date_format_2(s):
    pass

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

date = input("Date: ")
print(date)

if "," in date:
    print("type 1")
    parse_date_format_1(date)
else:
    print("type 2")

