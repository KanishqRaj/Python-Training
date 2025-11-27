class Car:
    def __init__(self,brand,model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand : ",self.brand)
        print("Model : ",self.model)
        print("Price : ",self.price)

car1 = Car("Suzuki","Baleno",1000000)
car2 = Car("Toyota","Fortuner",45000000)

car1.display()
print()
car2.display()