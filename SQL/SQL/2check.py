import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PassSQL@123"
)

mycursor = mydb.cursor()
#Check if Database Exists
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)