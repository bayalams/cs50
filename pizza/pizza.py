import sys
from tabulate import tabulate

menu = sys.argv[1]
print(menu)

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif not menu.endswith("cvs"):
    print("Not a CVS file")
    sys.exit(1)

#print(tabulate(menu))