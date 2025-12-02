def safeListCheck(list,index):
    try:
        return list[index]
    except IndexError:
        print("Index out of range")

safeListCheck([1,3,4,5,5],7)