class Student:
    # "def underscore underscore" -> "dunder" function
    # __init__ = function initializing an instance of a class (object), "self" argument represents that new object
    def __init__(self, name, house, patronus):
        # if name == ""
        if not name:
            raise ValueError("Error: Missing name.")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Error: Invalid House.")
        self.name = name
        self.house = house
        self.patronus = patronus
    # when a function wants to see my object as a string (print, ...)
    def __str__(self):
        return f"{self.name} from {self.house} with {self.patronus}"


def main():
    student = get_student()
    # name == "" and/or house not in valid houses
    if student is not None:
        print(student) # __str__
    else:
        print("Student creation failed")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    try:
        return Student(name, house, patronus)  # constructor call -> instantiate Student object
    except ValueError as e:
        print(e)  # prints the raises
        return None


if __name__ == "__main__":
    main()