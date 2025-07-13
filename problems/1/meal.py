def main():
    pre_conv = input("Time: ")
    post_conv = convert(pre_conv)

    if 7 <= post_conv <= 8:
        print("breakfast time")
    elif 12 <= post_conv <= 13:
        print("lunch time")
    elif 18 < post_conv < 19:
        print("dinner time")


def convert(time):
    h, m = time.split(':')
    return int(h) + int(m) / 60


if __name__ == "__main__":
    main()
