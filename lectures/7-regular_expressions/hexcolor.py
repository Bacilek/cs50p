import re

def main():
    hex = input("Hexadecimal color code: ")
    pattern = r"^#[a-f0-9]{6}$"

    if match := re.search(pattern, hex, re.IGNORECASE):
        print(f"valid, macthed with {match.group()}")
    else:
        print("invalid")

if __name__ == "__main__":
    main()