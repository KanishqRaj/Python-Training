class Payment:
    def __init__(self, amount):
        self.amount = amount

    def paymentInfo(self):
        print(f"Payment Done for {self.amount}")

class UPIPayment(Payment):
    def __init__(self, amount,UpiId):
        super().__init__(amount)
        self.UpiId = UpiId

    def UPIPaymentInfo(self):
        print(f"UPI Payment Done for {self.amount} using the UPI ID : {self.UpiId}")

class CreditCardPayment(Payment):
    def __init__(self, amount,CreditCardId):
        super().__init__(amount)
        self.CreditCardId = CreditCardId

    def CreditCardPaymentInfo(self):
        print(f"Credit Card Payment done for {self.amount} using the Credit Card Number : {self.CreditCardId}")

class WalletPayment(Payment):
    def __init__(self, amount,WalletId):
        super().__init__(amount)
        self.WalletId = WalletId

    def WalletPaymentInfo(self):
        print(f"Payment Done for {self.amount} using the Wallet ID : {self.WalletId}")

wp = WalletPayment(30000,32234)
cp = CreditCardPayment(30000,222233334444)
up = UPIPayment(30000,"hihello@oksbi")
wp.WalletPaymentInfo()
cp.CreditCardPaymentInfo()
up.UPIPaymentInfo()
