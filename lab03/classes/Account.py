class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
        return
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
            return



name = str(input("Write your name: "))
balance = int(input("Write your started balance: "))
acc = Account(name, balance)
currentBalance=acc.balance
while True:
    decision=input("Whould you like to 'deposit' or 'withdraw' your balance?('x' for exit)")
    if decision=='x':
        print('Your current balance:', currentBalance)
        currentBalance=acc.balance
        break
    elif decision=='deposit':
        dep=int(input('Value of deposit:'))
        acc.deposit(dep)
        currentBalance=acc.balance
    elif decision=='withdraw':
        wit=int(input('Value of withdraw:'))
        acc.withdraw(wit)
        currentBalance=acc.balance
    else:
        print("Use 'deposit','withdraw' or 'x'")
