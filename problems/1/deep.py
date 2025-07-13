def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if ans.lower().strip() in ["42", "forty-two", "forty two"]:
        print("yes")
    else:
        print("no")


main()
