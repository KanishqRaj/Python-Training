from datetime import datetime, timedelta

def calculate_delivery_date(od,tl):
    order_date = datetime.strptime(od, '%Y-%m-%d')
    delivery_date = order_date + timedelta(days=tl)
    return delivery_date

order_date = "2025-12-01"
timeline = 4
estimated = calculate_delivery_date(order_date,timeline)
print(estimated)