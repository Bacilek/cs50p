class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts."

    # operator overloading -> overloading the '+' operator
    def __add__(self, other):  # self (left of the operator) and other (right of the operator)
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25) 
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley  # self = potter, other = weasley
print(total)