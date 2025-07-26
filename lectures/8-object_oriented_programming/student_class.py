class Student:
    # "def underscore underscore" -> "dunder" function
    # __init__ = function initializing an instance of a class (object), "self" argument represents that new object
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)  # constructor call -> instantiate Student object
    return student


if __name__ == "__main__":
    main()