from datetime import datetime, timedelta, date

def expiring_soon(dates):
    today = date.today()
    return [d for d in dates if (datetime.strptime(d,'%Y-%m-%d').date() - today).days <= 15]

print(expiring_soon(['2025-12-10' , '2026-01-01']))