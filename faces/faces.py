s = 'this shit is :('
for i in s:
    if i == ":(" or i == ":)":
        i.replace(":(", "🙁") or i.replace(":)", "🙂")
print(s)

