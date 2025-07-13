def main():
    camel = input("camelCase: ")

    print("snake_case: ", end='')
    for word in camel:
        for letter in word:
            if letter == letter.upper():
                print(f"_{letter.lower()}", end='')
            else:
                print(letter, end='')
    print('\n')


main()
