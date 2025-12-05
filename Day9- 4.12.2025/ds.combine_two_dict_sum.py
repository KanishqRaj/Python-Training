dict1 = { 'a':1 , 'b':2 , 'c':3 }
dict2 = { 'a':1 , 'd':3 , 'e':4}
combined = {}
for key in set(dict1) | set(dict2):
    combined[key] = dict1.get(key, 0) + dict2.get(key, 0)
print(combined)