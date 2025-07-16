from sys import exit


def main():
    percentage = convert(input("Fraction: "))
    print(f"Percentage: {percentage}%")

    res = gauge(percentage)
    print(f"Result: {res}")


def convert(fraction):
    x, y = fraction.split('/')
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError("ZeroDivisionError")
    if (x > y) or (x < 0 or y < 0):
        raise ValueError("ValueError")
    percentage = round(x / y * 100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()
