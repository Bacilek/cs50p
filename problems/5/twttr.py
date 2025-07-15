VOWELS = {'a', 'e', 'i', 'o', 'u'}


def main():
    twitter = input("Twitter: ")
    print(f"Twttr: {shorten(twitter)}")


def shorten(twitter):
    twttr = ""
    for word in twitter:
        for letter in word:
            if letter.lower() not in VOWELS:
                twttr += letter
    return twttr



if __name__ == "__main__":
    main()