import re

ip_address = input("IPv4 Address: ")
print(ip_address)

matches = re.search(r"(.+)\.(.+)\.(.+)\.(.+)", ip_address)
print(matches.group(1))
print(matches.group(2))
print(matches.group(3))
print(matches.group(4))

if matches.group(1) and matches.group(2) and matches.group(3) and matches.group(4) <= "255":
    print("valid")
else:
    print("Invalid")
