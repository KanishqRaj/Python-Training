class Transaction:
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance
        self.transaction = []

    def deposit(self,amount):
        self.balance += amount
        self.transaction.append(f"Deposited amount : {amount},Current balance : {self.balance}")

    def withdraw(self,amount):
        if self.balance<amount:
            print("Not enough money")
        else:
            self.balance -= amount
            self.transaction.append(f"Amount withdrawn : {amount}, Current Balance : {self.balance}")

    def current_balance(self):
        return self.balance

    def show_transaction(self):
        print(self.transaction)

tr = Transaction("Kanishq",1000)
tr.deposit(1000)
tr.withdraw(500)
print(tr.current_balance())
print(tr.show_transaction())



