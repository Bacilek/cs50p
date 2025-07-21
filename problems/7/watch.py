import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    pattern = r"https?://(?:www\.)?youtube\.com/embed/(\w+)\".+$"
    if match := re.search(pattern, s):
        return f"https://youtu.be/{match.group(1)}"
    else:
        return "None"


if __name__ == "__main__":
    main()