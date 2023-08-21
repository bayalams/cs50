#o que falta:
#reprompt se o dia for mais do que 31
#reprompt se o mês for mais do que 12

class FormatError(Exception):
    pass

def main():
    while True:
        try:
            date = input("Date: ")
            #print(date)
            if "," in date:
                #print("type 1")
                new_date = parse_date_format_1(date)
                print(new_date)
            else:
                print("type 2")
                new_date_2 = str(parse_date_format_2(date))
                print(new_date_2)
        except FormatError:
            pass

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
    return str(months.index(month) + 1).zfill(2) #para imprimir com o zero antes

def parse_date_format_1(s):

    list_of_elements = s.replace(",", "").split(" ")
    day = list_of_elements[1]
    month = list_of_elements[0]
    year = list_of_elements[2]

    date_format(day, month)

    return f"{year}-{month_from_string_to_int(month):02d}-{day:02d}"

def parse_date_format_2(s):
    list_of_elements = s.split("/")
    #print(list_of_elements)

    day = int(list_of_elements[1])
    #print(f"day: {day}")
    month = int(list_of_elements[0])
    #print(f"month: {month}")
    year = int(list_of_elements[2])
    #print(f"year: {year}")

    date_format(day, month)

    return f"{year}-{(month):02d}-{day:02d}"

def date_format(day, month):
    print(f"day ={day}")
    print(f"month ={month}")

    if day > 31:
        raise FormatError
    elif month > 12:
        raise FormatError

    return

main()