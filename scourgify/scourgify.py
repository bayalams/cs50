import sys
import csv

names_before = sys.argv[1]
#names_after = sys.argv[2]

with open(names_before) as csvfile_1:
    reader = csv.DictReader(csvfile_1)
    for row in reader:
        print(row)