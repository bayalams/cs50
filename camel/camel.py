case = "pythonIsTheBest"
uppercase_letter = ""

for i in case:
    if i.isupper():
        uppercase_letter = i

for i in case:
    if i == uppercase_letter:
        case = case.replace(uppercase_letter, "_" + uppercase_letter)

case = case.lower()
print(case)