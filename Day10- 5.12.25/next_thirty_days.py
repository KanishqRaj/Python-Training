from datetime import datetime, timedelta, date

def next_30_days():
    return [(date.today() + timedelta(days = i)).strftime("%Y-%m-%d") for i in range(30)]

print(next_30_days())