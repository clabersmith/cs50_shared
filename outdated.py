months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    m = d = y = ""

    while(True):
        try:
            date = input("Date: ").strip()
            if "/" in date and len(date.split("/")) == 3:
                m, d, y = date.split("/")
                if(isValidDate(m, d, y)):
                    break

            elif " " in date and len(date.split(" ")) == 3:
                m, d, y = date.split(" ")
                if d.endswith(",") and m in months:
                    d = d.removesuffix(",")
                    m = str(months.index(m) + 1)

                    if(isValidDate(m, d, y)):
                        break

        except EOFError:
            break

    print(f"{int(y):04}-{int(m):02}-{int(d):02}")

def isValidDate(m, d, y):
    if m.isnumeric() and d.isnumeric() and y.isnumeric():
        if (int(m) > 0 and int(m) < 13) and (int(d) > 0 and int(d) < 32):
            return True

    return False

main()
