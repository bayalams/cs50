from pyfiglet import Figlet
import sys

figlet = Figlet()

figlet.setFont(font=sys.argv[2])

print (figlet.renderText('text to render'))