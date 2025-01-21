import sqlite3
import json

# Connect to SQLite database
conn = sqlite3.connect(r'C:\Users\Gachombaj\3D Objects\G MOTIONS\G_motionscommerce\db.sqlite3')
cursor = conn.cursor()

# Fetch all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Dictionary to store all data
db_data = {}

# Loop through each table and fetch data
for table in tables:
    table_name = table[0]
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = [column[1] for column in cursor.fetchall()]
    db_data[table_name] = [dict(zip(columns, row)) for row in rows]

# Close the connection
conn.close()

# Write to JSON file
with open('output.json', 'w') as json_file:
    json.dump(db_data, json_file, indent=4)

