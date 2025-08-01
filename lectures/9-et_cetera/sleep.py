def main():
    n = int(input("Number of sheep: "))
    for s in sheep(n):
        print(s)


# n = 1 000 000 -> lags PC (gg RAM/CPU)
"""
def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock
"""


# n = 1 000 000 -> works fine
def sheep(n):
    for i in range(n):
        yield "🐑" * i  # yield: return, but one at a time -> loop keeps working, program is not waiting


if __name__ == "__main__":
    main()
