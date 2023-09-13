import inflect

p = inflect.engine()

while True:
    try:
        name = input("Name: ")
        name_list = p.join({name})
        print(f"Adieu, adieu, to {name_list}")
    except EOFError:
        break
