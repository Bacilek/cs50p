def main():
    while True:
        fraction = input("Fraction: ")

        try:
            num, den = fraction.split('/', maxsplit=1)
            num = int(num)
            den = int(den)
        except ValueError:
            print("ValueError")
            continue

        try:
            res = num/den
        except ZeroDivisionError:
            print("ZeroDivisionError")
            continue

        res = round(num / den * 100)
        if res > 100:
            continue
        elif res < 0:
            continue
        elif res <= 1:
            print('E')
        elif res >= 99:
            print('F')
        else:
            print(f"{res}%")
        break


main()
