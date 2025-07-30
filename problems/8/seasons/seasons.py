from datetime import date
from re import fullmatch
from sys import exit
from inflect import engine

p = engine()

def main():
    birth = input("Date of Birth: ")
    pattern = r"(\d{4})-(\d{2})-(\d{2})"

    if not (match := fullmatch(pattern, birth)):
        exit("Error: Invalid date.")

    # two date instances that can be subtracted from each other )thanks to overriden '-' in date class)
    today = date.today()
    birth = date(int(match.group(1)), int(match.group(2)), int(match.group(3)))

    print(f"{date_to_text(today, birth)} minutes")


def date_to_text(today, birth):
    delta_minutes = (today - birth).days * 24 * 60 # delta days into delta minutes
    minutes_in_text = p.number_to_words(delta_minutes, andword="").capitalize()
    return minutes_in_text


if __name__ == "__main__":
    main()
