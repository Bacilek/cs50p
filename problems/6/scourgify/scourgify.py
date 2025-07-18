import csv

from sys import argv, exit

def main():
    if len(argv) != 3:
        exit(f"Usage: python {argv[0]} INPUT OUTPUT!")
    if not argv[1].endswith('.csv') or not argv[2].endswith('.csv'):
        exit("Error: Both input and output files should be CSV files.")

    input_filename = argv[1]
    output_filename = argv[2]

    try:
        with open(input_filename, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
    except FileNotFoundError:
        exit(f"Error: The file {input_filename} does not exist.")

    try:
        with open(output_filename, 'w', newline='') as file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()

            for row in data:
                last, first = row["name"].split(", ")
                house = row["house"]
                writer.writerow({"first": first, "last": last, "house": house})
    except IOError:
        exit(f"Error: Could not write to the file {output_filename}.")
 

if __name__ == "__main__":
    main()
