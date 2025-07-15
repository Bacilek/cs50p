from random import randint

INTERVALS = {1: (0, 9),
             2: (10, 99),
             3: (100, 999)}

def main():
    level = get_level()

    score = 0
    for _ in range(10):
        mistakes = 0

        x, y = generate_integer(level), generate_integer(level)
        res = x + y

        while mistakes < 3:
            try:
                user = int(input(f"{x} + {y} = "))
            except ValueError:
                mistakes += 1
                print("EEE")
                continue

            if user == res:
                break
            mistakes += 1
            print("EEE")

        if mistakes < 3:
            score += 1
        elif mistakes == 3:
            print(f"{x} + {y} = {res}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level in [1, 2, 3]:
            return level


def generate_integer(level):
    min, max = INTERVALS[level]
    return (randint(min, max))


if __name__ == "__main__":
    main()