# grocery list in all uppercase
# sorted alphabetically by item
# prefixing each line with the number of times the user inputted that item.

list_item = []
dict_item_count = {}

while True:

    item = input()
    item = item.upper()
    list_item.append(item)
    count = list_item.count(item)
    print(count)




    # except EOFError:
    #     break


