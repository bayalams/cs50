from pyfiglet import Figlet
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if sys.arg

print(len(sys.argv))

if len(sys.argv) == 1:
    print (figlet.renderText('text to render'))
    sys.exit()
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f":
        print("Invalid usage")
        sys.exit()
    else:
        figlet.setFont(font=sys.argv[2])
        print (figlet.renderText('text to render'))
        sys.exit()
else:
    print("Invalid usage")
    sys.exit()