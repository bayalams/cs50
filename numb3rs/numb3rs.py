import re

ip_address = input("IPv4 Address: ")
print(ip_address)

matches = re.search(r"(.+)\.(.+)\.(.+)\.(.+)", ip_address):
    print(matches.group(1))
    print(matches.group(2))
    print(matches.group(3))
    print(matches.group(4))
else:
    pass

    # if re.group(1) and re.group(2) and re.group(3) and re.group(4) <= 255:
    #     print("valid")
    # else:
    #     print("invalid")