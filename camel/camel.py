case  = "camelCase"
uppercase_letter = ""

for i in case:
    if i.isupper():
        uppercase_letter = i

print(uppercase_letter)

for uppercase_letter in case:
    case = case.replace(uppercase_letter, "_" + uppercase_letter)

print(case)