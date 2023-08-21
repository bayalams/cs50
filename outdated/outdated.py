#o que falta:
#reprompt se o dia for mais do que 31
#reprompt se o mês for mais do que 12

class FormatError(Exception):
    pass

def main():
    while True:
        try:
            date = input("Date: ")

            if "," in date:
                new_date = parse_date_format_1(date)
                print(new_date)
            else:
                new_date_2 = str(parse_date_format_2(date))
                print(new_date_2)
        except FormatError:
            pass
        # except Exception as e:
        #     print(e, type(e))


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
    day = int(list_of_elements[1])
    month = list_of_elements[0]
    year = int(list_of_elements[2])
    aux_month = month_from_string_to_int(month)


    date_format(day, aux_month)

    return f"{year}-{month_from_string_to_int(month):02d}-{day:02d}"

def parse_date_format_2(s):
    list_of_elements = s.split("/")

    day = int(list_of_elements[1])
    month = int(list_of_elements[0])
    year = int(list_of_elements[2])

    date_format(day, month)

    return f"{year}-{(month):02d}-{day:02d}"

def date_format(day, month):

    if day > 31:
        raise FormatError
    elif month > 12:
        raise FormatError

    return

main()