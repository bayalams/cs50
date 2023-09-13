import inflect

p = inflect.engine()

while True:
    try:
        name = input("Name: ")
        p.join({name})
        print(f"Adieu, adieu, to {name}")
    except EOFError:
        break
