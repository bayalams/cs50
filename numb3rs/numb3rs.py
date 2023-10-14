import re

def main():
    ip_address = input("IPv4 Address: ")
    if matches:
        print("True")
    else:
        print("False")

def validate(ip_address):
    pattern = r"^(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)$"
    matches = re.search(pattern, ip_address)

if __name__ == "__main__":
    matches = validate(ip_address)
    main()