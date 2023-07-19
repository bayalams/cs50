s = input("Insert sentence. ")
s_1 =""

for i in s:
    if i == " ":
        s_1 = s.replace(" ", "...")

print(s_1)
