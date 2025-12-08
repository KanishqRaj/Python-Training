from datetime import datetime

def count_mondays(attendance):
    return sum(1 for day in attendance if datetime.strptime(day,'%Y-%m-%d %H:%M:%S').weekday() == 0)

attendance = ["2025-12-01 09:00:00", "2025-12-02 10:00:00", "2025-12-08 08:30:00"]
print(count_mondays(attendance))