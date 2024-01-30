import mysql.connector
#import mysql.connector
#create user ''user'a'%' identified by 'password';
mydb = mysql.connector.connect(
    host="localhost",
    user = "abc",
    passwd = "password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("show databases")
for x in mycursor:
    print(x)