from datetime import datetime, timedelta, date

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

a = is_leap_year(2004)
if a:
    print("Yes")
else:
    print("Not a leap year")