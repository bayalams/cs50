case = "pythonIsTheBest"
uppercase_letter = []

for i in case:
    if i.isupper():
        uppercase_letter.append(i)

for i in case:
    if i in uppercase_letter:
        case = case.replace(uppercase_letter, "_" + uppercase_letter)

case = case.lower()
print(case)