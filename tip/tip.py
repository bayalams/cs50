def main():

    dollars = dollars_to_float(input("How much was dinner? "))
    percentage = percentage_to_float(input("What percentage do you want to tip? "))
    tip = dollars * percentage
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):

    d = input("insert ammount: ")
    d = float(d.replace("$", ""))
    print(d)
    return d

def percentage_to_float(p):

    p = input("insert percentage: ")
    p = float(p.replace("%", ""))
    p = (p/100)
    print(p)
    return p



