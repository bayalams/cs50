# grocery list in all uppercase
# sorted alphabetically by item
# prefixing each line with the number of times the user inputted that item.

list_item = []

while True:
    try:
        item = input()
        item = item.upper()
        list_item.append(item)
        sorted_list_item = sorted(list_item)
        print(sorted_list_item)
        count = sorted_list_item.count(item)
        print(count)

    except EOFError:
        break






    # except EOFError:
    #     break


