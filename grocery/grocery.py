# grocery list in all uppercase
# sorted alphabetically by item
# prefixing each line with the number of times the user inputted that item.


while True:
    try:
        item = input()
        item = item.upper()
    except EOFError:
        break

    list_item = []
    list_item.append(item)
    print(list_item)