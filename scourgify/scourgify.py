import sys
import csv
from pprint import pprint
from tabulate import tabulate

names_before = sys.argv[1]
names_after = sys.argv[2]

before_list = []
names_list = []
house_list=[]

#open the file and split the names into last and first
with open(names_before, "r") as csvfile_1:
    reader = csv.DictReader(csvfile_1)
    for row in reader:
        full_name = row["name"]
        house = row["house"]
        last, first = full_name.split(",")



with open(names_after, "w", ) as csvfile_2:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(csvfile_2, fieldnames = fieldnames)