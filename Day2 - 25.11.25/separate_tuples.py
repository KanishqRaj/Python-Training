mixed = (1,44,"Hello" , 22, 32.5 , "World")
numbers = tuple(x for x in mixed if isinstance(x,(int,float)))
strings = tuple(x for x in mixed if isinstance(x,str))

print(numbers,strings)
