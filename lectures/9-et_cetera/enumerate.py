students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(f"{i + 1}: {students[i]}")

for i, student in enumerate(students):
    print(f"{i + 1}: {student}")
