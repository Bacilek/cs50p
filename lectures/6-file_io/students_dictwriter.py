import csv
name, home = input("Name: "), input("Home: ")

with open("students_dictwriter.csv", 'a') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})