# grocery list in all uppercase
# sorted alphabetically by item
# prefixing each line with the number of times the user inputted that item.

list_item = []
dict_item_count = {}

while True:
    try:
        item = input()
        item = item.upper()
        list_item.append(item)
        sorted_list_item = sorted(list_item)
        print(sorted_list_item)

    except EOFError:
        break

for item, count in dict_item_count.items():
    if item in dict:
        count = count + 1


    # except EOFError:
    #     break


