class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def totalcost(self):
        return self.price * self.quantity

p1 = Product("Moisturizer",62,7)
print(p1.totalcost())
