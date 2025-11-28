class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def StartEngine(self):
        print(f"{self.brand} Engine Started")

    def StopEngine(self):
        print(f"{self.brand} Engine Stopped")

class Car(Vehicle):
    def __init__(self,brand,model):
        self.model = model
        super().__init__(brand)

    def drive(self):
        print(f"{self.model} Driving")

    def park(self):
        print(f"{self.model} Parked")

c = Car("Suzuki","Fronx")

c.StartEngine()
c.drive()
c.StopEngine()
c.park()
