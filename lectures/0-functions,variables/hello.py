name = input("Your full name: ").strip()

# printing is a side effect
print("hello, " + name + ".")
print("hello,", name.strip(), ".")
print(f"hello, {name}.")

# str methods
print(name, name, name, sep=";", end="\n")
print(f"{name.capitalize()}")
print(f"{name.title()}")
print(f"{name.upper()}")
print(f"{name.lower()}")

first, last = name.split(" ")
print(f"first name: {first}")
print(f"last name: {last}")
