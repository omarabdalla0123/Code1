import sqlite3
##to create the data base
conn = sqlite3.connect("MydataBase.db")
cursor = conn.cursor()

## to create a table on the data base
cursor.execute(""" CREATE TABLE IF NOT EXISTS MyTable (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age TEXT,
               grade TEXT)""")

conn.commit()

##to insert (add data) on the Table
cursor.execute("INSERT INTO MyTable (name,age,grade) VALUES (?,?,?)", ("Ahmed", "40", "C"))
conn.commit()

##to select data from the Table
cursor.execute("SELECT * FROM MyTable")


cursor.execute("SELECT * FROM MyTable WHERE name=?", ("Omer",))
conn.commit()


##to Update the data
cursor.execute("UPDATE MyTable SET grade =? WHERE name=?" ,("A", "Ahmed"))
conn.commit()


##to DELETE the data
cursor.execute("DELETE FROM MyTable WHERE id=?", ("4",))
conn.commit()