string = input("Enter a string: ")
v_count = 0
c_count = 0
d_count = 0
v_Set = 'aeiouAEIOU'
for char in string:
    if char in v_Set:
        v_count += 1
    elif char.isalpha():
        c_count += 1
    elif char.isdigit():
        d_count += 1

print("Vowels : ", v_count , "Consonants : ", c_count, "Digits : ", d_count)
