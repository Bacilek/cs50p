import csv

students = []

with open("students_reader.csv") as file:
    reader = csv.reader(file)  # deals with commas, quotes & corner cases in .csv file for me
    for name, home in reader:
        students.append({"name": name, "home": home})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
