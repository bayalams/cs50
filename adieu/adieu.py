import inflect
p = inflect.engine()


name_list = []

while True:
    try:
        name = input("Name: ")
        print(f"1.{name}")
        name_list = name_list.append(name)
        print(name_list)
    except EOFError:
        break

