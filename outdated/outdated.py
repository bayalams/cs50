
class FormatError(Exception):
    pass

def main():
    while True:
        try:
            date = input("Date: ")

            if "," in date:
                new_date = parse_date_format_1(date)
                print(new_date)
                exit(1)
            elif "/" in date: #in some cases, when input doesn't enter either statement, it goes back to the loop, without raising an exception. Explain!!!!
                new_date_2 = str(parse_date_format_2(date))
                print(new_date_2)
                exit(1)

        except FormatError: #suspicion that this isn't necessary, it will never be a format error, only value and index, because of situation mentioned above
            print("FormatError")
            pass
        except ValueError:
            print("ValueError")
            pass
        except IndexError as e:
            print("IndexError")
            pass
        except Exception as e:
            print(e, type(e))


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
    return months.index(month) + 1

def parse_date_format_1(date):

    list_of_elements = date.replace(",", "").split(" ")
    day = int(list_of_elements[1])
    month = list_of_elements[0]
    year = int(list_of_elements[2])
    aux_month = month_from_string_to_int(month)

    date_format(day, aux_month)

    return f"{year}-{month_from_string_to_int(month):02d}-{day:02d}"

def parse_date_format_2(date):
    list_of_elements = date.split("/")

    day = int(list_of_elements[1])
    month = int(list_of_elements[0])
    year = int(list_of_elements[2])

    date_format(day, month)

    return f"{year}-{month:02d}-{day:02d}"

def date_format(day, month):

    if day > 31:
        raise FormatError
    elif month > 12:
        raise FormatError

    return

main()