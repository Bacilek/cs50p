def main():
    pre = input("Input: ")
    post=""

    for word in pre:
        for letter in word:
            if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
                post += letter

    print(f"Output: {post}")

main()
