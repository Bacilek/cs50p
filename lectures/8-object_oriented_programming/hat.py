from random import choice

# not really worth making class for sorting hat since there only exists one -> no template needed
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod  # class method -> can be called without instantiating the class
    def sort(cls, name):  # cls: reference to the class itself
        house = choice(cls.houses)
        print(f"{name} has been sorted into the {house} house!")


Hat.sort("Harry")  # no instantiating/no object