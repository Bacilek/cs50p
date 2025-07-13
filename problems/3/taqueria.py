MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = 0
    while True:
        try:
            price = get_price(input("Item: "))
        except EOFError:
            print()
            break
        if price == 0:
            continue
        total = add_price(price, total)
        print(f"Total: ${total:0.2f}")


def get_price(item):
    return MENU.get(item.lower().title(), 0)


def add_price(price, total):
    return total + price


main()
