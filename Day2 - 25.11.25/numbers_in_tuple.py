def print_integers(tup):
    for n in tup:
        if isinstance(n,int):
            print(n)
        elif isinstance(n,tuple):
            print_integers(n)

tup = (10, (20, 30), (40, (50, 60)))
print_integers(tup)


