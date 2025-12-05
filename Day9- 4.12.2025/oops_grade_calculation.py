class Student():
    def __init__(self,id, name, marks):
        self.name = name
        self.marks = marks
        self.id = id

    def garde_calculation(self):
        if self.marks > 90:
            grade = "A"
        elif self.marks > 80:
            grade = "B"
        elif self.marks > 70:
            grade = "C"
        elif self.marks > 60:
            grade = "D"
        else:
            grade = "F"
        return grade

st = Student(1,"Kanishq",98)
print(st.garde_calculation())