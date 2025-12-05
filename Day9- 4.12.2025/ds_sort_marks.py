def sorted_marks(marks):
    sorted_marks = sorted(marks.items() , key = lambda x:x[1] , reverse = True)
    return sorted_marks[:2]

stud_marks = {
    'A':80,
    'B':79,
    'C':92, }
print(sorted_marks(stud_marks))