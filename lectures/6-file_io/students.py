students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(',')
        student = {"name": name, "house": house}  # student["name"], student["house"] = name, house
        students.append(student)

# Sorted by key "name", nahrazeno lambdou
"""
def get_name(student):
    return student["name"]
"""

for student in sorted(students, key=lambda student: student["name"]): # lambda
    print(f"{student['name']} is in {student['house']}")


