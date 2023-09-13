import inflect


while True:
    try:
        name = input("Name: ")
        print(f"Adieu, adieu, to {name}")
    except EOFError:
        break
