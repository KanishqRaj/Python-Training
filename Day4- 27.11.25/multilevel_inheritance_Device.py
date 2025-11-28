class Device:
    def __init__(self,Brand):
        self.Brand=Brand

    def powerOn(self):
        print(f"{self.Brand} is on")

    def powerOff(self):
        print(f"{self.Brand} is off")

class Computer(Device):
    def __init__(self,brand,cpu,price):
        super().__init__(brand)
        self.cpu=cpu
        self.price=price

    def displayInfo(self):
        print(f"{self.Brand} contains the CPU : {self.cpu} , Price: {self.price}")

    def WarrantyInfo(self,years):
        self.years=years
        print(f"{self.Brand} has warranty for {self.years} years")

class Laptop(Computer):
    def __init__(self,cpu,processor,name,price,brand):
        super().__init__(cpu,price,brand)
        self.processor=processor
        self.name=name

    def displayCPU(self):
        print(f"{self.Brand} has CPU : {self.cpu}")

    def displayProcessor(self):
        print(f"{self.Brand} has processor : {self.processor}")

l = Laptop("RX8508","I7","Elite",143000,"HP")
l.displayCPU()
l.powerOn()
l.displayProcessor()
l.WarrantyInfo(4)
l.displayProcessor()
