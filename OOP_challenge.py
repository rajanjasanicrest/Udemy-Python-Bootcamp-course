class BankAccount():

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Money Deposited Successfully")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("You cannot withdraw amount that is greater than your balance!")
        else:
            self.balance -= amount
            print("Amount Withdrawb has been deducted from your account")

    def __str__(self):
        return f'Account Owner : {self.owner} \nAvailable balance : {self.balance}'
    
