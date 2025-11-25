num = int(input("Enter a digit : "))

reversed_num = 0
digit = 0

while num > 0:
    digit = num % 10
    num //= 10
    reversed_num = reversed_num * 10 + digit

print(reversed_num)
