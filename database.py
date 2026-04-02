import sqlite3
conn= sqlite3.connect("student.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")
cursor.execute("insert into student values(1,'amit',80)")
cursor.execute("insert into student values(2,'Neha',80)")
cursor.execute("insert into student values(3,'ram',80)")
conn.commit()
cursor.execute("select * from student")
rows=cursor.fetchall()
print("student records:")
for row in rows:
    print (row)

conn.close()