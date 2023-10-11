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

# Open the file for writing
with open(names_after, "w") as csvfile_2:
    # Define headers
    fieldnames = ["first", "last", "house"]
    # Define writer using said headers
    writer = csv.DictWriter(csvfile_2, fieldnames=fieldnames)
    # Write headers on file
    writer.writeheader()

    # Open the file for reading
    with open(names_before, "r") as csvfile_1:
        reader = csv.DictReader(csvfile_1)

        # Loop for splitting first and last name
        for row in reader:
            full_name = row["name"]
            house = row["house"]
            last, first = full_name.split(",")

            # Write the actual information under the header
            writer.writerow({"first": first.strip(), "last": last.strip(), "house": house})
