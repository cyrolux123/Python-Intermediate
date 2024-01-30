import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="abc",
    passwd="password",
)

mycursor = mydb.cursor()
mycursor.execute("insert into student (name, age, grade, address) values ('John', 20, 90, '123 Main Street')")
mycursor.execute("insert into student (name, age, grade, address) values ('John', 20, 90, '123 Main Street')")
mycursor.execute("insert into student (name, age, grade, address) values ('John', 20, 90, '123 Main Street')")
mycursor.execute("insert into student (name, age, grade, address) values ('John', 20, 90, '123 Main Street')")
mycursor.execute("insert into student (name, age, grade, address) values ('John', 20, 90, '123 Main Street')")
mycursor.execute("insert into student (name, age, grade, address) values ('John', 20, 90, '123 Main Street')")
mycursor.execute("insert into student (name, age, grade, address) values ('John', 20, 90, '123 Main Street')")
mydb.commit()
mydb.close()