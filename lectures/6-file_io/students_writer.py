import csv
name, home = input("Name: "), input("Home: ")

with open("students_writer.csv", 'a') as file:
    writer = csv.writer(file)
    writer.writerow([name, home])