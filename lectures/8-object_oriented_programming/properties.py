class Student:
    # "def underscore underscore" -> "dunder" function
    # __init__ = function initializing an instance of a class (object), "self" argument represents that new object
    def __init__(self, name, house, patronus):
        self.name = name
        self.house = house  # uses setter
        self.patronus = patronus

    # when a function wants to see my object as a string (print, ...)
    def __str__(self):
        return f"{self.name} from {self.house} with a {self.patronus} patronus."

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Error: Missing name.")
        self._name = name  # var with '_' at start -> don't touch it!! (dont overwrite it)

    # getter: gets an attribute
    @property
    def house(self):
        return self._house  # to not be confuse var house with def house
    
    # setter: sets some value
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Error: Invalid house.")
        self._house = house
    
    @property
    def patronus(self):
        return self._patronus
    
    @patronus.setter
    def patronus(self, patronus):
        if not patronus:
            raise ValueError("Error: Missing patronus.")
        self._patronus = patronus
    
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


def main():
    student = get_student()

    # name, house & patronus valid
    if student is not None:
        print(student) # __str__
        print(f"Expecto Patronum! {student.charm()}")
    # name == "" and/or house not in valid houses
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