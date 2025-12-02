a = int(input("Enter a number : "))
b = int(input("Enter another number : "))
try:
    print(a/b)
except ZeroDivisionError:
    print("The second number cannot be zero")

