from datetime import datetime, date, timedelta

today = date.today()
print(today)

print(today.year)
print(today.month)
print(today.day)

now = datetime.now()
print(now)

dob = date(2003,10,6)
print(dob)

formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted)