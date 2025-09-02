from pyfiglet import Figlet
import sys

def main():

    #get the font from the command line arg
    if len(sys.argv) == 2:
        print(f"font={sys.argv[1]}")

    while True:
        try:
            f = input("Input: ")
            figlet = Figlet()
            fontlist = figlet.getFonts()
            if f in fontlist:
                figlet.setFont(font='slant')
            print(figlet.renderText('test'))
            break
        except TimeoutError:
            break

main()
