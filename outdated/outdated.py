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

def parse_date_format_1(s):
    list_of_elements = s.replace(",", "").split(" ")

    day = list_of_elements[1]
    month = list_of_elements[0]
    year = list_of_elements[2]

    print(day, month, year)

    for pila, m in enumerate(months):

        if m.lower() == month.lower():
            month = pila + 1

    print(f"{day}-{month}-{year}")



def parse_date_format_2(s):
    pass


date = input("Date: ")
print(date)

if "," in date:
    print("type 1")
    parse_date_format_1(date)
else:
    print("type 2")

