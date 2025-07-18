from sys import argv, exit


def main():
    if len(argv) != 2:
        exit(f"Usage: python {argv[0]} FILENAME!")
    if not argv[1].endswith('.py'):
        exit("Error: File should be a Python script.")

    filename = argv[1]
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        exit(f"Error: File '{filename}' not found.")

    n = 0
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            n += 1

    print(f"Number of non-empty, non-comment lines: {n}")


if __name__ == "__main__":
    main()
