import sys
from tabulate import tabulate
import csv

menu = sys.argv[1]
prices = []

if len(sys.argv) > 2:
    print("Too many command-line arguments")
elif len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)
elif not menu.endswith("csv"):
    print("Not a cvs file")
    sys.exit(1)

with open(menu) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #must append to a list instead of just printing so that the date is stored before being formated
        prices.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})

print(tabulate(prices))





