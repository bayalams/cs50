# grocery list in all uppercase
# sorted alphabetically by item
# prefixing each line with the number of times the user inputted that item.

dict_item_count = {}
dict_grocery_list = {}
sorted_item_list = []

while True:
    try:
        item = input()
        item = item.upper()
        if item in dict_item_count.keys():
            dict_item_count[item] = dict_item_count[item] + 1
        else:
            dict_item_count[item] = 1

    except KeyError:
        pass
    except EOFError:
        break

sorted_item_list = sorted(dict_item_count.keys())

for item, count in dict_item_count.items():
    dict_grocery_list[count] = item

for k, v in dict_grocery_list.items():
    print(k, v)



