def main():
    case = input("write input: ")
    snake_case(case)


def snake_case(case):

    uppercase_letter = []

    if not case.isalpha():
        print("Error: case must be comprised of letters. For example: camelCase")
        exit(-1)

    for i in case:
        if i.isupper():
            uppercase_letter.append(i)

    for i in case:
        if i in uppercase_letter:
            case = case.replace(i, "_" + i)

    case = case.lower()
    print(case)
    return case

main()

