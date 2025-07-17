# file open & close
"""
name = input("Name: ")
file = open("names.txt", 'a')
file.write(f"{name}\n")
file.close()
"""

# with file
"""
name = input("Name: ")
with open("names.txt", 'a') as file:
    file.write(f"{name}\n")
"""

# readlines
"""
with open("names.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(f"hello, {line.rstrip()}")  # end=""
"""

# most clean
"""
with open("names.txt", 'r') as file:
    for line in file:
        print(f"hello, {line.rstrip()}")
"""

# sorted (gotta pre-save)
"""
names = []
with open("names.txt") as file:  # 'r' is default
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
"""

# reverse sorted & more compact
with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print(f"hello, {line.rstrip()}")