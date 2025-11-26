a = {1,2,3,4,5}
b = {6,8,9}
def isdisjoint(a,b):
    for x in a:
        for y in b:
            if x==y:
                return True
    return False
print(isdisjoint(a,b))