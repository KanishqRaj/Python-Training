class Employee:
    def __init__(self,Name,Dep,EmpId,Salary):
        self.Name = Name
        self.Dep = Dep
        self.EmpId = EmpId
        self.Salary = Salary

    def display(self):
        print("Name:",self.Name)
        print("Dep:",self.Dep)
        print("Employee:",self.EmpId)
        print("Salary:",self.Salary)

emp1 = Employee("Kanishq" , "ET","002",2222)
emp1.display()