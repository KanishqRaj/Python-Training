from flask import Flask , request , jsonify
import pandas as pd
import pymysql

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "Kanishq@0610",
    database = "employee_flask"
)

df = pd.read_sql("SELECT * FROM employee", conn)
conn.close()
print(df)