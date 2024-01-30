import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="abc",
    passwd="password",
)

mycursor = mydb.cursor()
mycursor.execute("select * from student")
#mycursor.execute("select * from student where name = 'John'")
for i in mycursor.fetchall():
    print(i)
mydb.close()