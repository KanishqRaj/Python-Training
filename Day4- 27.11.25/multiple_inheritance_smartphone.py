class Camera:
    def __init__(self,megapixels):
        self.megapixels = megapixels

    def capture(self):
        print("The camera Captures")

    def stop(self):
        print("The camera stops Capturing")

class Phone:
    def __init__(self,size,phoneNumber):
        self.size = size
        self.phoneNumber = phoneNumber

    def displaySize(self):
        print(f"This phone's size is {self.size} inches")

    def displayPhoneNumber(self):
        print(f"This phone's phone number is {self.phoneNumber}")

class SmartPhone(Camera,Phone):
    def __init__(self,phoneNumber,size,megapixels,model):
        Phone.__init__(self,size,phoneNumber)
        Camera.__init__(self,megapixels)
        self.model = model

    def AllInfo(self):
        print(f"This phone's model is {self.model} and has {self.size} inches with {self.megapixels} megapixels camera and has a phone number {self.phoneNumber}")


sp = SmartPhone(814860,7,48,"S23")
sp.capture()
sp.stop()
sp.displaySize()
sp.displayPhoneNumber()
sp.AllInfo()