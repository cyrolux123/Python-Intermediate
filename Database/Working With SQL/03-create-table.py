import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="abc",
    passwd="password",
)

mycursor = mydb.cursor()

# Create the "student" table
mycursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, grade FLOAT, address VARCHAR(255))")
mydb.close()