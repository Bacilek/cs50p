def main():
    text = input("Input: ")
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    print(f"Output: {text}")


main()
