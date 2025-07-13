MONTHS = [
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
    while True:
        date = input("Date: ")
        if '/' in date:
            try:
                month, day, year = date.split('/')
            except ValueError:
                continue
        elif ',' in date:
            try:
                month, day, year = date.replace(',', '').split(' ')
                month = MONTHS.index(month) + 1
            except ValueError:
                continue
        else:
            continue

        try:
            month, day, year = int(month), int(day), int(year)
        except ValueError:
            continue

        if 1 <= day <= 31 and 1 <= month <= 12:
            print(f"{year:04}-{month:02}-{day:02}")
            break
        else:
            continue

main()
