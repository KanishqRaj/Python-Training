from datetime import datetime, timedelta, date

def calculate_age(str):
    dob = datetime.strptime(str, "%Y-%m-%d").date()
    today = date.today()
    age = today.year - dob.year - ((today.month , today.day) < (dob.month, dob.day))
    return age

str = input("Enter you DOB: ")
print(calculate_age(str))