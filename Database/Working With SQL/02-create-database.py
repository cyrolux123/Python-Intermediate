import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user = "abc",
    passwd = "password"
)
mycursor = mydb.cursor()
mycurser.execute("create database mydatabase")
mydb.close()