def filter_dict(dict):
    result = {}
    for key, value in dict.items():
        if value > 40000:
            result[key] = value
    return result

dict = {"Kevin":34000 , "Mohan":100000 , "Rohan":50000}
print(filter_dict(dict))

