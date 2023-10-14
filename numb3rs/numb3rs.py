import re

def main():
    #the purpose of this function is to see if the input fits the pattern returned from the function validate()
    ip_address = input("IPv4 Address: ")
    #define the variable matches in the main function, using the return value from validate()
    matches = validate(ip_address)
    if matches:
        print("True")
        return True
    else:
        print("False")
        return False

def validate(ip_address):
    #the only purpose of this function is to return the pattern
    pattern = r"^(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)$"
    return re.search(pattern, ip_address)

if __name__ == "__main__":
    main()