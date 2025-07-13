def main():
    get_house("Ron")

def compare(x, y):
    if x < y:
        print("x < y")
    elif x > y:
        print("x > y")
    else:
        print("x == y")

    if x == y:
        print("x == y")
    else:
        print("x != y")

def is_even(n):
    return n % 2 == 0

def get_house(name):
    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Unknown")

main()
