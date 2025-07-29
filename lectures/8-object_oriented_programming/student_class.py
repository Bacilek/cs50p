class Student:
    # "def underscore underscore" -> "dunder" function
    # __init__ = function initializing an instance of a class (object), "self" argument represents that new object
    def __init__(self, name, house, patronus):
        # if name == ""
        if not name:
            raise ValueError("Error: Missing name.")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Error: Invalid House.")
        if not patronus:
            raise ValueError("Error: Missing patronus")
        self.name = name
        self.house = house
        self.patronus = patronus

    # when a function wants to see my object as a string (print, ...)
    def __str__(self):
        return f"{self.name} from {self.house} with a {self.patronus} patronus."
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell Terrier":
                return "🐶"
            case _:
                return "🪄"
    
    # can call this without creating an instance/object
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, house, patronus)


def main():
    student = Student.get()

    # name, house & patronus valid
    if student is not None:
        print(student) # __str__
        print(f"Expecto Patronum! {student.charm()}")
    # name == "" and/or house not in valid houses
    else:
        print("Student creation failed")


if __name__ == "__main__":
    main()