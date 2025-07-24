def main():
    greeting = input("Greeting: ").lstrip().lower()
    if greeting[0] == 'h':
        if greeting[1:5] == "ello":
            print("$0")
        else:
            print("$20")
    else:
        print("$100")


main()
