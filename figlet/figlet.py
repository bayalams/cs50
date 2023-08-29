from pyfiglet import Figlet
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    print (figlet.renderText(input("Input: ")))
    sys.exit()
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f":
        print("Invalid usage")
        sys.exit()
    elif sys.argv[2] not in fonts:
        print("Invalid Usage")
        sys.exit()
    else:
        figlet.setFont(font=sys.argv[2])
        print (figlet.renderText(input("Input: ")))
        sys.exit()
else:
    print("Invalid usage")
    sys.exit(-1)