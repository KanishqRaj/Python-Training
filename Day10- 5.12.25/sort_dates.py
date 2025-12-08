from datetime import datetime, timedelta, date

def sort_dates(date_list):
    return sorted(date_list, key = lambda x: datetime.strptime(x, '%Y-%m-%d'))

print(sort_dates(['2025-10-01' , '2024-08-03' , '2025-10-02']))