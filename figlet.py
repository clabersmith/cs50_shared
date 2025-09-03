from pyfiglet import Figlet
import sys

def main():

    # get the font from the command line arg
    if len(sys.argv) == 2:
        f=sys.argv[1]
        print(f"font={f}")

        while True:
            try:
                input_string = input("Input: ")
                figlet = Figlet()
                fontlist = figlet.getFonts()
                if f in fontlist:
                    figlet.setFont(font=f)
                    print(figlet.renderText(input_string))
                    break

            except EOFError:
                break

main()
