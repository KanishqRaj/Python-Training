from traceback import print_tb


class Student_Marks:
    def __init__(self, name, m1,m2,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return self.m1 + self.m2+self.m3

    def percentage(self):
        return self.total()*100/300

    def grade(self):
        if self.percentage()>90:
            return "A"
        elif self.percentage()>80:
            return "B"
        elif self.percentage()>70:
            return "C"
        elif self.percentage()>60:
            return "D"

    def print_info(self):
        print(self.total())
        print(self.percentage())
        print(self.grade())

st = Student_Marks("Kanishq",96,89,95)
st.print_info()
