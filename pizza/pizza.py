import sys
from tabulate import tabulate
import csv

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)

#the input call must come after the conditions for the input to be valid, otherwise the code breaks
menu = sys.argv[1]
prices = []

if not menu.endswith("csv"):
    print("Not a cvs file")
    sys.exit(1)

with open(menu) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #must append to a list instead of just printing so that the date is stored before being formated
        prices.append(row)

#must include headers, which are the keys of the dictionary, because they chance with each file
print(tabulate(prices, headers = "keys"))





