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
while True:
    print("\n1.Insert")
    print("\n2.View")
    print("\n3.Exit")

    choice = int(input("Enter Choice:"))
    if choice==1:
        id=int (input("enter id:"))
        name=input("enter name:")
        marks=int(input("enter marks:"))
        cursor.execute("insert into students(?,?,?)"(id,name,marks))

    elif choice == 2:
        cursor.execute("select*from students")
        data=cursor.fetchall()
        print("student records:")
        for row in data:
            print (row)

    elif choice==3:
        break 
conn.close()


    