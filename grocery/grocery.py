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

    except EOFError:
        break

for item in sorted_list_item:
    if item in dict_item_count.keys():
        dict_item_count[item] = dict_item_count[item] + 1
    else:
        dict_item_count[item] = 1

dict_grocery_list = {}

for item, count in dict_item_count.items():
    dict_grocery_list[count] = item

print(dict_grocery_list)
print(f"{dict_grocery_list[0]}, /n {dict_grocery_list[1]}")

    # except EOFError:
    #     break


