#dá erro nos testes mas funciona; https://submit.cs50.io/check50/0465a5d16f4dae6fd2dc2dd219f1f9f6165d903c

import inflect
p = inflect.engine()

name_list = []
adieu_list = []

while True:
    try:
        name = input("Name: ")
        #print(f"1.{name}")
        name_list.append(name)
        #print(name_list)
    except EOFError:
        break


adieu_list = p.join(name_list)
print(f"Adieu, adieu, to {adieu_list}")

