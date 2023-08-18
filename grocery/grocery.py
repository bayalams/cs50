# grocery list in all uppercase
# sorted alphabetically by item
# prefixing each line with the number of times the user inputted that item.

list_item = []

while True:
    try:
        item = input()
        item = item.upper()
        list_item.append(item)
    except EOFError:
        break
    except TypeError:
        pass

    print(list_item)

    for item in list_item:
        