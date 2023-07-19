s = 'this shit is :('
for i in s:
    if i == ":(":
        s = s.replace(":(", "🙁")
    elif i == ":)":
        s = s.replace(":)", "🙂")
print(s)

