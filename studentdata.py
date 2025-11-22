import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

cmd = """
CREATE TABLE IF NOT EXISTS STUDENT(
      
        fullname text not null,
        usn varchar(10) not null primary key,
        sem integer not null,
        cgpa integer not null
        )
"""
cursor.execute(cmd)
connection.commit()

cmd = "INSERT INTO STUDENT(fullname,usn,sem,cgpa)values(?,?,?,?)"
#cursor.execute(cmd,('Siya','abc772',2,8))
#cursor.execute(cmd,('Sanya','abc100',2,9))
connection.commit()

f = cursor.execute("SELECT * FROM STUDENT").fetchall()
print(f)
r=cursor.execute("select * from student where fullname = ?",('Sanya',)).fetchall()
print(r)

connection.close()
