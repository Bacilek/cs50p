import csv

students = []

with open("students_dictreader.csv") as file:
    reader = csv.DictReader(file)  # get lines as a dictionary, needs specified keys on line 1 of .csv file (-> columns) 
    for student in reader:
        students.append({"name": student["name"], "home": student["home"], "house": student["house"]})


for student in sorted(students, key=lambda student: student["name "]):
    print(f"{student['name']} is from {student['home']} belongs to {student['house']}.")
