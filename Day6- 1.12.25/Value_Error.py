try:
    num = int(input("Enter a number : "))
    x = 10/num
    print(x)

except ValueError:
    print("Please enter a number")

except ZeroDivisionError:
    print("Division by zero is not possible")