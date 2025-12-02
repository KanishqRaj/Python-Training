from traceback import print_exc


def conversion(list):
    result=[]
    for i in list:
        try:
            num = int(i)
            result.append(num)
        except ValueError:
            print("The value is invalid to convert")
    return result

converted = conversion(["hello" , "1.2" , "500"])
print(converted)

