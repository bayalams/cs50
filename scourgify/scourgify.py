import sys
import csv
from pprint import pprint

names_before = sys.argv[1]
names_after = sys.argv[2]

before_list = []
names_list = []
house_list=[]

with open(names_before) as csvfile_1:
    reader = csv.DictReader(csvfile_1)
    for row in reader:
        pprint(row)






# with open(names_after, "w", ) as csvfile_2:
#     fieldnames = ["first", "last", "house"]
#     writer = csv.DictWriter(csvfile_2, fieldnames = fieldnames)