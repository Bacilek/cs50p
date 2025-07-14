def main():
    text = "Adieu, adieu, "
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break

    first_name, last_name = names[0], names[len(names) - 1]
    for name in names:
        if name == first_name:
            text += f"to "
        elif name == last_name:
            if len(names) == 2:
                text += f" and "
            else:
                text += f", and "
        else:
            text+= f", "
        text += f"{name}"

    print("")
    print(text)


if __name__ == "__main__":
    main()
