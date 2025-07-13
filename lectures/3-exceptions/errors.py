# ValueError: int != str
try:
    x = int(input("What's x: "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

# NameError: x not assigned
try:
    x = int(input("What's x: "))
except NameError:
    print("x not assigned")
else:
    print(f"x is {x}")

# try successful -> else. try excepted -> except
while True:
    try:
        x = int(input("What's x: "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")

# same, but more concise and put into function
def get_int():
    while True:
        try:
            return int(input("What's x: "))
        except ValueError:
            print("x is not an integer")
