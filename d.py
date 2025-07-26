import pandas as pd
import sqlite3

conn = sqlite3.connect('app.db')
df = pd.read_sql_query("SELECT * FROM users", conn)
print(df)
conn.close()
