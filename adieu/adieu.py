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

#print only the final list, outside of the loop
adieu_list = p.join(name_list)
print(f"Adieu, adieu, to {adieu_list}")

