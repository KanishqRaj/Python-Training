class Bankaccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, Bankaccount):
            return self.balance + other.balance
        return  NotImplemented

    def __str__(self):
        return "Your Bank account has a balance of " + str(self.balance)

b = Bankaccount(100)
account1 = Bankaccount(200)
total = b + account1
print(total)