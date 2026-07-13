import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("sales.db")

# SQL Query
query = "SELECT * FROM sales LIMIT 10;"

# Read data
df = pd.read_sql_query(query, conn)

# Display output
print(df)

# Close connection
conn.close()