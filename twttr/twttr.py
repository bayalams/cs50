insert_string = input("Insert string: ")

print(insert_string)
vowels = "aeiouAEIOU"
consonants = []

for i in insert_string:
    if i not in vowels:
        consonants.append(i)

str_consonants = ''.join(consonants)
print(str_consonants)