from pyfiglet import Figlet
import sys

figlet = Figlet()
fonts = figlet.getFonts()

print(len(sys.argv))

if len(sys.argv) == 1:
    print (figlet.renderText('text to render'))
    sys.exit()
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f":
        print("2.Invalid usage")
        sys.exit()
    elif sys.argv[2] not in fonts:
        print("1.Invalid Usage")
        sys.exit()
    else:
        figlet.setFont(font=sys.argv[2])
        print (figlet.renderText('text to render'))
        sys.exit()
else:
    print("3.Invalid usage")
    sys.exit()