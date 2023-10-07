import sys
import csv
from pprint import pprint

names_before = sys.argv[1]
names_after = sys.argv[2]

before_list = []
names_list = []
house_list=[]

with open(names_before) as csvfile_1:
    for line in csvfile_1:
        row = line.strip().split(",")
        print(row)
        last = row[0]
        first = row[1]
        # house = row[2]
        # print(f"last name: {last} | first name: {first} | house: {house}")


with open(names_after, "w", ) as csvfile_2:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(csvfile_2, fieldnames = fieldnames)