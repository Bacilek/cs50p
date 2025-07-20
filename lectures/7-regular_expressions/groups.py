import re

locations = {"+1": "United States and Canada", 
             "+62": "Indonesia",
             "+420": "Czech Republic",
             "+505": "Nicaragua"}

def main():
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    if match := re.search(pattern, number):
        country_code = match.group("country_code")
        print(f"Call from {locations[country_code]}.")
    else:
        print("invalid")


if __name__ == "__main__":
    main()