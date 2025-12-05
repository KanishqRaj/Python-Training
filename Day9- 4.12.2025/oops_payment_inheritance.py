class Payment:
    def process_payment(self):
        print("Init Payment")

class CreditCard(Payment):
    def process_payment(self):
        print("Your payment has been processed through Credit Card")

class UPI(Payment):
    def process_payment(self):
        print("Your payment has been processed through UPI")

up = UPI()
up.process_payment()
cc = CreditCard()
cc.process_payment()


