try:
    num = int(input("Enter a number : "))
    x = 10/num

except ZeroDivisionError:
    print("Division by zero is not possible")