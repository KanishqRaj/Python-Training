def unique_tuples(tp):
    new_tp = ()
    for item in tp:
        if item not in new_tp:
            new_tp += (item,)
    return new_tp

tuples = ("Kanishq" , "Joseph", "Jack" ,"Jeff","Jason","Joseph")
print(unique_tuples(tuples))
