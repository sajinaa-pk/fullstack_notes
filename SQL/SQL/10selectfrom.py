#Select From

'''
Select From a Table
To select from a table in MySQL, use the "SELECT" statement:

'''

#Select all records from the "customers" table, and display the result:

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PassSQL@123",
  database="studentform"
 
)
mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)