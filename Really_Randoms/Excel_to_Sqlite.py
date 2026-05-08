import pandas as pd
import sqlite3

# --- SETTINGS ---
excel_file = r"D:\Code\Really_Randoms\students.xlsx"
sheet_name = 0
database_file = "my_database.db"
table_name = "my_table"

# --- READ EXCEL ---
df = pd.read_excel(excel_file, sheet_name=sheet_name)
print(f"✅ Read {len(df)} rows and {len(df.columns)} columns from Excel")
print(f"Columns: {list(df.columns)}")

# --- WRITE TO SQLITE ---
conn = sqlite3.connect(database_file)
df.to_sql(table_name, conn, if_exists="replace", index=False)
conn.close()

print(f"✅ Data saved to '{database_file}' in table '{table_name}'")