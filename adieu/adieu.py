import inflect

p = inflect.engine()
name_list = []

while True:
    try:
        name = input("Name: ")
        print(f"1.{name}")
        name_list = p.join([f"2.{name}"])
        print(name_list)
    except EOFError:
        break

