def main():
    list = {}
    while True:
        try:
            curr = input().upper()
        except EOFError:
            break
        if curr not in list:
                list[curr] = 1
        else:
            list[curr] += 1

    for item in sorted(list):
        print(f"{list[item]} {item}")

main()
