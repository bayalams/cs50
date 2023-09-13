import inflect

p = inflect.engine()
name_list = []

while True:
    try:
        name = input("Name: ")
        name_list = p.join([name])
        print(name_list)
    except EOFError:
        break

