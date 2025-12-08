from datetime import datetime, timedelta,date, time

start_day = date(2025,12,5)
duration = 28
expiry_date = start_day + timedelta(days=duration)
print("Your plan will expire on :",expiry_date)
