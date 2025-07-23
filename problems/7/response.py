import validators

def main():
    email = input("Email: ").strip()
    print("Valid") if validators.email(email) else print("Invalid")


if __name__ == "__main__":
    main()
