class Person:
    def __init__(self,name):
        self.name = name

class Employee(Person):
    def __init__(self,name,empId):
        super().__init__(name)
        self.empId = empId

e = Employee("Kanishq",2)
print(e.name , e.empId)