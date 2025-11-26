numbers = (33,20,30,60,50)
max = numbers[0]
min = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
    if numbers[i] < min:
        min = numbers[i]

print(max , min)