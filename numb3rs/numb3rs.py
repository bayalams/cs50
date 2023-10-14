import re

ip_address = input("IPv4 Address: ")
print(ip_address)

if re.search(r"(.+)/.(.+)/.(.+)/.(.+)"):
    print(re.group(1))
    print(re.group(2))
    print(re.group(3))
    print(re.group(4))

    # if re.group(1) and re.group(2) and re.group(3) and re.group(4) <= 255:
    #     print("valid")
    # else:
    #     print("invalid")