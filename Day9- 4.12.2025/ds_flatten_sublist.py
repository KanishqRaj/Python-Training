nested_list = [[1,2],[2,3],[7,8]]
flattened_lit = [num for x in nested_list for num in x]
print(flattened_lit)