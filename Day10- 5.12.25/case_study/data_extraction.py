import pandas as pd
import pymysql

from datetime import datetime, date, timedelta

# 6) Connect Python to MySQL and load the subscriptions table into a DataFrame
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Kanishq@0610",
    database="subscription_app"
)
df = pd.read_sql("SELECT * FROM subscriptions", conn)
conn.close()
df["start_date"] = pd.to_datetime(df["start_date"])
df["expiry_date"] = pd.to_datetime(df["expiry_date"])
df["created_at"] = pd.to_datetime(df["created_at"])

##7.Convert created_date into %Y%M%D %H%M%S
df["created_time"] = df["created_at"].dt.strftime("%Y-%m-%d %H:%M:%S")

##8.Add column days_overdue
df["days_overdue"] =  df["days_left"].apply(lambda x:abs(x) if x<0 else 0)
print(df["days_overdue"])
