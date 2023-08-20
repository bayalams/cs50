def month_from_string_to_int(month):
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

    month = month.title()
    return str(months.index(month) + 1).zfill(2)



def parse_date_format_1(s):
    list_of_elements = s.replace(",", "").split(" ")

    day = list_of_elements[1]
    month = list_of_elements[0]
    year = list_of_elements[2]

    return f"{year}-{month_from_string_to_int(month)}-{day}"


def parse_date_format_2(s):
    pass


date = input("Date: ")
print(date)

if "," in date:
    print("type 1")
    new_date = parse_date_format_1(date)
    print(new_date)
else:
    print("type 2")

