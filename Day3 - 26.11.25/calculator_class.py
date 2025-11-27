class Calculator:

    def addition(self,a,b):
        return a+b

    def subtraction(self,a,b):
        return b-a

    def multiplication(self,a,b):
        return a*b

    def division(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            print("Division by zero")

a = 34
b = 0
ops = Calculator()
print(ops.addition(a,b))
print(ops.subtraction(a,b))
print(ops.multiplication(a,b))
print(ops.division(a,b))
