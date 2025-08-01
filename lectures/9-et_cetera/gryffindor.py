students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


# List comprehension
gryffindors_comprehension = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors_comprehension):
    print(gryffindor)


print("--------------------------------------------------------")

# filter
def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors_filter = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors_filter, key=lambda s: s["name"]):
    print(gryffindor["name"])
