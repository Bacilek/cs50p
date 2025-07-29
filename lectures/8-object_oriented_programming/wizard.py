class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Error: Missing name.")
        super().__init__(name) 
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    pass


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    pass


wizard = Wizard("Albus Dumbledore")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")