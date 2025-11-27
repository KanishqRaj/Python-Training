class Percentage:
    def __init__(self,name,m1,m2,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return self.m1 + self.m2 + self.m3

    def percentage(self):
        return self.total()*100/300

    def display(self):
        print ("percentage : ",self.percentage())

percent = Percentage("Kanishq",77,87,92)
percent.display()