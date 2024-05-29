#Check if Table Exists
'''
You can check if a table exist by listing all tables in your database with the "SHOW TABLES" statement:
'''
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PassSQL@123",
  database="studentform"
 
)
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)