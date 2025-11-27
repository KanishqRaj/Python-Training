class Student:
    pass

s1 = Student()
s2 = Student()

class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age

s3 = Student("kanishq",22)
s4 = Student("Raj",23)

print(s3.name,s4.age)