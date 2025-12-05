def reversed(list1):
    result = []
    for i, item in enumerate(list1):
        if i%2!=0:
            if  isinstance(item, str):
                result.append(item[::-1])
            elif isinstance(item, list):
                result.append(item[::-1])
            else:
                result.append(item)
        else:
            result.append(item)
    return result


list1 = ["hello" , "python" , [1,2,3], [4,5,6]]
print(reversed(list1))