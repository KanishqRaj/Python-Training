class Notification:
    def send(self,message):
        print("Sending notification ", message)


class EmailNotification(Notification):
    def send(self,message):
        print("Sending email ", message)

class PushNotification(Notification):
    def send(self,message):
        print("Sending push notification ", message)

class SMSNotification(Notification):
    def send(self,message):
        print("Sending sms notification ", message)

n1 = EmailNotification()
n1.send("Your order is out for delivery")
n2 = PushNotification()
n2.send("Your order is out for delivery")
n3 = SMSNotification()
n3.send("Your order is out for delivery")
