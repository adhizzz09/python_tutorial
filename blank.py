import sqlite3

conn=sqlite3.connect('student.db')
cursor=conn.cursor()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS students
        (
            id INTEGER PRIMARY KEY,
            name TEXT ,
            marks INTEGER
        )
        """)

cursor.execute("INSERT INTO students (id,name,marks) VALUES (1,'Purva',85)")
cursor.execute("INSERT INTO students (id,name,marks) VALUES (2,'hetvi',89)")
cursor.execute("INSERT INTO students (id,name,marks) VALUES (3,'harshda',65)")
cursor.execute("INSERT INTO students (id,name,marks) VALUES (4,'ria',75)")
conn.commit()
cursor.execute("SELECT * FROM students")

rows=cursor.fetchall()
print("stundent details:")
for row in rows:
    print(rows)
conn.close()
