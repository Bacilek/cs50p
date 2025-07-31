class Account:
    def __init__(self):
        self._balance = 0  # ._ -> private to instance variable, read only! (no change from outsie)
    
    @property  # getter
    def balance(self):
        return self._balance
    
    @balance.setter  # setter: changing instance property outside of code
    def balance(self , n):
        self._balance = n
    
    def deposit(self, n):
        self._balance += n
    
    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print(f"Balance: {account.balance}")
    account.deposit(100)
    account.withdraw(50)
    print(f"Balance: {account.balance}")
    account.balance = 500  # "setted"
    print(f"Balance: {account.balance}")


if __name__ == "__main__":
    main()
    