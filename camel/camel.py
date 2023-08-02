case  = "camelCase"
uppercase_letter = ""

for i in case:
    if i.isupper():
        uppercase_letter = i

print(uppercase_letter)

print(list(case))
upper_list = case.split(uppercase_letter)
print(upper_list)