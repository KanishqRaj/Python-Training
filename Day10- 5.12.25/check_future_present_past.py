from datetime import datetime

str = input("Enter a date in format YYYY-MM-DD: ")
given_date = datetime.strptime(str, "%Y-%m-%d")
today = datetime.today()
if given_date == today:
    print("It is today's date")

elif given_date > today:
    print("It is future")

else:
    print("It is past")