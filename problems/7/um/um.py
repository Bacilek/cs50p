import re

def main():
    print(count(input("Input: ")))


def count(s):
    pattern = r"\bum\b"  # \b -> whole word only
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
