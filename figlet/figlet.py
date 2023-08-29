from pyfiglet import Figlet
import sys

figlet = Figlet()
print(len(sys.argv))

if len(sys.argv) == 1:
    print (figlet.renderText('text to render'))
    sys.exit()
elif len(sys.argv) == 3:
    print(sys.argv[2])
    figlet.setFont(font=sys.argv[2])
    print (figlet.renderText('text to render'))
    sys.exit()
else:
    print("Invalid usage")
    sys.exit()