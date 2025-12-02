def calculator(num1,num2,operator):
    try:
        a = float(num1)
        b = float(num2)
    except ValueError:
        print("Enter a valid number")

    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        try:
            return a/b
        except ZeroDivisionError:
            print("Division by zero")

print(calculator(1,2,"+"))
print(calculator(1,2,"-"))
print(calculator(1,2,"*"))
print(calculator(1,0,"/"))

