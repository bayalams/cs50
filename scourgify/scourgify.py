import sys
import csv

names_before = sys.argv[1]
names_after = sys.argv[2]

before_list= []

with open(names_before) as csvfile_1:
    reader = csv.reader(csvfile_1)
    for row in reader:
        before_list.append(row)

print(before_list)



with open(names_after, "w", ) as csvfile_2:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(csvfile_2, fieldnames = fieldnames)
