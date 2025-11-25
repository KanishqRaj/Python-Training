num = int(input("Enter a digit : "))

count = 0

while num>0:
    num = int(num/10)
    count += 1

print(count)
