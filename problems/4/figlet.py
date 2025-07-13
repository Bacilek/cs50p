from pyfiglet import Figlet
from sys import argv, exit
from random import choice

figlet = Figlet()
argc = len(argv)

if argc == 2 or argc > 3:
    exit("Invalid usage")

fonts = figlet.getFonts()
if argc == 3:
    flag, font = argv[1], argv[2]
    if flag not in ['-f', "--font"] or font not in fonts:
        exit("Invalid usage")
else:
    font = choice(fonts)
figlet.setFont(font=font)

text = input("Input: ")
print(figlet.renderText(text))

