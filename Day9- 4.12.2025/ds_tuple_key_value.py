def list_to_dict(lst):
    result = {}
    for key, value in lst:
        if key in result:
            return None
        result[key] = value
    return result

list1 = [('a',1) , ('b',2) , ('c',3)]
print(list_to_dict(list1))