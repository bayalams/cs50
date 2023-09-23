# grocery list in all uppercase
# sorted alphabetically by item
# prefixing each line with the number of times the user inputted that item.

list_item = []
dict_item_count = {}
dict_grocery_list = {}

while True:
    try:
        item = input()
        item = item.upper()
        list_item.append(item)
        sorted_list_item = sorted(list_item)

    except KeyError:
        pass
    except EOFError:
        exit(1)

#qual é o problema???

for item in sorted_list_item:
    if item in dict_item_count.keys():
        dict_item_count[item] = dict_item_count[item] + 1
    else:
        dict_item_count[item] = 1

result_grocery_list = []

for item, count in dict_item_count.items():
    result_grocery_list.append((count, item))

for count, item in result_grocery_list:
    print(count, item)



