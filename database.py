import sqlite3

connection = sqlite3.connect("feedback.db")
cursor = connection.cursor()

cmd = """
CREATE TABLE IF NOT EXISTS FEEDBACK(
        id integer primary key,
        fullname text not null,
        usn varchar(10) not null,
        contact varchar(10) not null,
        email text not null,
        message text not null
        )
"""
cursor.execute(cmd)
connection.commit()

cmd = "INSERT INTO FEEDBACK(fullname,usn,contact,email,message)values(?,?,?,?,?)"
#cursor.execute(cmd,('Manvitha','abcd123','9019948881','smanvitha205@gmail.com','This is good time to learn DevOps!'))
#cursor.execute(cmd,('Manya','abc11','9019945733','smanvitha5@gmail.com','This is good time to learn python'))
connection.commit()

f = cursor.execute("SELECT * FROM FEEDBACK").fetchall()
print(f)

connection.close()
