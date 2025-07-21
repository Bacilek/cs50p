import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    octet = r"((2((5[0-5])|([0-4][0-9])))|(1[0-9]{2})|([1-9][0-9])|[0-9])"
    pattern = fr"{octet}\.{octet}\.{octet}\.{octet}"
    if match := re.fullmatch(pattern, ip):
        return True
    return False


if __name__ == "__main__":
    main()
