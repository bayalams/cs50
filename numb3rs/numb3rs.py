import re

ip_address = input("IPv4 Address: ")
print(ip_address)

matches = re.search(r"(.+)\.(.+)\.(.+)\.(.+)", ip_address)
g1 = int(matches.group(1))
g2 = int(matches.group(2))
g3 = int(matches.group(3))
g4 = int(matches.group(4))
if matches:
    if g1<= 255 | g2<= 255 | g3<= 255 | g4<= 255:
        print("valid")
    else:
        print("Invalid")
else:
    print("Invalid")
