##PRINT
print("Hello World")

##PRINT VARIABLES
name = "Kanishq"
Age = 22
Position = "Associate Software Engineer"
print(name, Age, Position)


##IF ELSE
mark = int(input("Enter your mark"))
if mark>=90:
    print("Grade A")
elif mark>=80:
    print("Grade B")
elif mark>=70:
    print("Grade C")
elif mark>=50:
    print("Just Pass")
else:
    print("Fail")


##FOR LOOP
for i in range(1,21):
    if i%2==0:
        print(i, "is even")
    else:
        print(i, "is odd")


##WHILE LOOP
counter = 5
while counter > 0:
    print(counter)
    counter -= 1


##CONTINUE
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

##BREAK
for i in range(1,11):
    if i==7:
        break
    print(i
