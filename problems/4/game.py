from random import randint
from sys import exit


def main():
    while True:
        try:
            n = int(input("Level: "))
            break
        except ValueError:
            continue

    res = randint(1, n)
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue
        if guess < res:
            if guess <= 0:
                continue
            print("Too small!")
        elif guess > res:
            print("Too large!")
        else:
            print("Just right!")
            exit()


if __name__ == "__main__":
    main()
