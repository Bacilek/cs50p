def main():
    total = 0
    while total < 50:
        print(f"Amount Due: {50 - total}")
        curr = int(input("Insert Coin: "))
        if curr in [5, 10, 25]:
            total += curr
    print(f"Change Owed: {total - 50}")


main()
