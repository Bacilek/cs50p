from requests import get, RequestException
from sys import argv, exit
from json import dumps

API = "d153651114853e2f07e8fb953b5a167b450432a51fe5e40144caaf414b7af760"

def main():
    if len(argv) != 2:
        exit("One command-line argument required")

    try:
        n = float(argv[1])
    except ValueError:
        exit("Float value required")

    try:
        response = get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API}")
    except RequestException:
        exit("Request error")

    # UNFORMATED
    # print(response.json())


    # FORMATED
    # print(dumps(response.json(), indent=2))

    o = response.json()
    btc_price = float(o["data"]["priceUsd"])
    print(f"${btc_price * n:,.4f}")


if __name__ == "__main__":
    main()
