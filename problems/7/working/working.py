import re

"""
9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
"""

def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    hours = r"((?:1[0-2])|(?:[0-9]))"
    minutes = r"(?::([0-5][0-9]))?"
    pattern = fr"^{hours}{minutes} (AM|PM) to {hours}{minutes} (AM|PM)$"

    if not (match := re.fullmatch(pattern, s)):
        raise ValueError("Invalid Pattern")

    from_h, from_min, to_h, to_min = int(match.group(1)), match.group(2), int(match.group(4)), match.group(5)

    from_h = twelves(from_h, match.group(3))
    to_h = twelves(to_h, match.group(6))

    from_min = int(from_min) if from_min is not None else 0
    to_min = int(to_min) if to_min is not None else 0

    return f"{from_h:02}:{from_min:02} to {to_h:02}:{to_min:02}"


def twelves(h, period):
    if period == "AM":
        return 0 if h == 12 else h
    else:
        return 12 if h == 12 else h + 12


if __name__ == "__main__":
    main()
