from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    font_list = figlet.getFonts()

    if len(sys.argv) == 2:
        sys.exit("either call with zero parameters for random font, or 2 parameters like -f slant to set font")
    if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "-font":
            f=sys.argv[2]
            if f not in font_list:
                sys.exit(f"font {f} not found")
        else:
            sys.exit("only -f or -font is supported")
    else:
        f = random.choice(font_list)

    input_string = input("Input: ")
    figlet.setFont(font=f)
    print(figlet.renderText(input_string))


main()
