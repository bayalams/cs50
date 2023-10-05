import sys

menu = sys.argv[1]

if len(sys.argv) > 2:
    sys.exit(1)
elif not menu.endswith("cvs"):
    sys.exit(1)
