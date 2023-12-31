#FALTA PASSAR NOS TESTES TODOS

import sys
import csv
from pprint import pprint

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
elif len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)

names_before = sys.argv[1]
names_after = sys.argv[2]


#open the file for writing
with open(names_after, "w") as csvfile_2:
    #DEFINE HEADERS
    fieldnames = ["first", "last", "house"]
    #DEFINE WRITER USING SAID HEADERS
    writer = csv.DictWriter(csvfile_2, fieldnames=fieldnames)
    #WRITE HEADERS ON FILE
    writer.writeheader()

    #open the file for reading
    with open(names_before, "r") as csvfile_1:
        reader = csv.DictReader(csvfile_1)

        #LOOP FOR SPLITING FIRST AND LAST NAME
        for row in reader:
            full_name = row["name"]
            house = row["house"]
            last, first = full_name.split(",")

            #MODULE FOR WRITING THE ACTUAL INFORMATION UNDER THE HEADER; MUST BE INDENTED BECAUSE OTHERWISE THE FILE WILL BE CLOSED
            writer.writerow({"first": first.strip(), "last": last.strip(), "house": house.strip()})




