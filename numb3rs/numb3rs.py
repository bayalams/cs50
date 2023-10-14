import re

ip_address = input("IPv4 Address: ")
print(ip_address)

matches = re.search(r"(.+)\.(.+)\.(.+)\.(.+)", ip_address)
g1 = int(matches.group(1))
g2 = int(matches.group(2))
g3 = int(matches.group(3))
g4 = int(matches.group(4))

if g1<= 255 :
    print(g1)
    print("valid")
else:
    print("Invalid")
