def remove_duplicates(values):
    return list(dict.fromkeys(values))

values = [100,200,300,200,300,400,500,600]
corrected_list = remove_duplicates(values)
print(corrected_list)