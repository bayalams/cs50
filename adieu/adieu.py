name_list = []

while True:
    try:
        name = input("Name: ")
        print(f"1.{name}")
        name_list.join(name)
        print(name_list)
    except EOFError:
        break

