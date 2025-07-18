from sys import argv, exit
from tabulate import tabulate
import csv

def main():
    if len(argv) != 2:
        exit(f"Usage: python {argv[0]} FILENAME!")
    if not argv[1].endswith('.csv'):
        exit("Error: File should be a CSV file.")

    filename = argv[1]
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader, None)  # Skip the header row
            print(tabulate(reader, headers, tablefmt="grid"))
    except FileNotFoundError:
        exit(f"Error: File '{filename}' not found.")


if __name__ == "__main__":
    main()
