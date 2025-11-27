class Customer:
    def __init__(self,name,age,city):
        self.age = age
        self.name = name
        self.city = city

    def eligibility(self):
        if self.age>25:
            return True
        return False

cus = Customer("Kanishq",26,"Coimbatore")
if cus.eligibility():
    print("Eligible")
else:
    print("Not Eligible")
