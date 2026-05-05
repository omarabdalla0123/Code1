import sqlite3


conn = sqlite3.connect("myexe.db")
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT,   
               name TEXT,
               age TEXT,
               grade TEXT)""")

conn.commit()

cursor.execute("INSERT INTO students (name,age,grade) VALUES (?,?,?)", ("Omer","21","A+"))
conn.commit()

cursor.execute("INSERT INTO students (name,age,grade) VALUES (?,?,?)", ("Ahmed","18","B"))
conn.commit()

cursor.execute("INSERT INTO students (name,age,grade) VALUES (?,?,?)", ("Ali","30","C"))
conn.commit()


cursor.execute("SELECT * FROM students")


rows = cursor.fetchall()
for row in rows:
    print(row)


cursor.execute("UPDATE students SET grade=? WHERE name=?",("F","Ahmed"))
conn.commit()

cursor.execute("DELETE FROM students WHERE id=?", ("2",))


cursor.execute("SELECT * FROM students")


rows = cursor.fetchall()
for row in rows:
    print(row)

