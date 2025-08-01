def main():
    yell_phrase("This is CS50")

    yell_list(["This", "is", "CS50"])

    yell_both("This is CS50")
    yell_both("This", "is", "CS50")
    
    yell_map("This is CS50")
    yell_map("This", "is", "CS50")
    
    yell_comprehension("This is CS50")
    yell_comprehension("This", "is", "CS50")


def yell_phrase(phrase):
    print(phrase.upper())
    
    
def yell_list(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)  # don't prnit it as a list but as a sentence


def yell_both(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


def yell_map(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


def yell_comprehension(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()