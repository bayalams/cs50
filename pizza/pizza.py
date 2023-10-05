import sys
from tabulate import tabulate
import csv

menu = sys.argv[1]

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif not menu.endswith("csv"):
    print("Not a cvs file")
    sys.exit(1)

with open(menu) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["Small"], row["Large"])

print(row)