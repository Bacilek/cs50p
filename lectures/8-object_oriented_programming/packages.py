class Package:
    def __init__(self, id, sender, recipient, weight):
        if id < 0:
            raise ValueError("Error: Invalid ID.")
        if not sender or not recipient:
            raise ValueError("Error: Missing sender or receiver.")
        if weight <= 0:
            raise ValueError("Error: Invalid weight.")
        self.id = id
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
    
    def __str__(self):
        return f"Package {self.id} is from {self.sender} to {self.recipient} with weight of {self.weight} kilograms and costs ${self.calculate_cost(5)}."        

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg
        
        
def main():
    packages = [
        Package(1, "Alice", "Bob", 10),
        Package(2, "Charlie", "Dave", 5),
        Package(3, "Eve", "Frank", 2.5)
    ]
    
    for package in packages:
        print(package)


main()