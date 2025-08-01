students = ["Hermione", "Harry", "Ron"]

# Basic
"""
gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})
"""

# List comprehension: -> [{},{},{}]
gryffindors1 = [{"name": student, "house": "Gryffindor"} for student in students]
print(gryffindors1)

gryffindors2 = {student: "Gryffindor" for student in students} 
print(gryffindors2)