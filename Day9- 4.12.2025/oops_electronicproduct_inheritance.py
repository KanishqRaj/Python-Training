class Product:
    def __init__(self,name , price , id):
        self.name = name
        self.price = price
        self.id = id

class ElectronicProduct(Product):
    def __init__(self, name, price, id):
        super().__init__(name, price, id)
        self.name = name
        self.price = price
        self.id = id

    def extend_warranty(self,years):
        print(f"Warranty for the product {self.name} has been extended for {years} years")

ep = ElectronicProduct("Electronic Product", 100, 1)
ep.extend_warranty(10)

