class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid Deposit Amount")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Kanishq",200000)
acc.deposit(10000)
print(acc.get_balance())
acc.withdraw(100000)
print(acc.get_balance())


print(dir(acc))


