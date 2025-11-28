class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def displayInfo(self):
        print(f"{self.name} has a price of {self.price}")

    def applyDiscount(self,discount):
        self.discount = (self.price - self.price*(discount/100))
        print(f"Discounted price is {self.discount}")

class ElectronicProduct(Product):
    def __init__(self,name,model,price):
        super().__init__(name,price)
        self.model = model

    def ExtendWarranty(self,years):
        self.years = years
        print(f"Warranty extended for {self.name} for {self.years} years")

ep = ElectronicProduct("Smartphone","S25 Edge",100000)
ep.displayInfo()
ep.applyDiscount(2)
ep.ExtendWarranty(5)