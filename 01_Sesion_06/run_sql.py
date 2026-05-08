import sqlite3
import os

db_path = 'NovaMarket_S06_Angel.db'
sql_path = '03_Laboratorio_S06.sql'

print(f"Executing {sql_path} on {db_path}...")

with open(sql_path, 'r', encoding='utf-8') as f:
    sql_script = f.read()

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    cursor.executescript(sql_script)
    conn.commit()
    print("Success!")
except Exception as e:
    print("Error:", e)
finally:
    conn.close()
